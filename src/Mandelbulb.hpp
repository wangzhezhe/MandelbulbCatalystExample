#include <iostream>
#include <fstream>
#include <cmath>
#include <vector>
#include <mpi.h>
#ifdef USE_HDF5
#include <hdf5.h>
#endif

class Mandelbulb {

    struct Vector {
        double x;
        double y;
        double z;
    };

    inline int& value_at(unsigned x, unsigned y, unsigned z) {
        auto width  = m_coord_x.size();
        auto height = m_coord_y.size();
        auto depth  = m_coord_z.size();
        return m_data[z + depth*(y + height*x)];
    }

    static inline double do_r(const Vector& v)
    {
        return std::sqrt(v.x*v.x + v.y*v.y + v.z*v.z);
    }

    static inline double do_theta(double n, const Vector& v)
    {
        return n * std::atan2(v.y,v.x);
    }

    static inline double do_phi(double n, const Vector& v)
    {
        return n * std::asin(v.z/do_r(v));
    }

    static int iterate(const Vector& v0, double order, unsigned max_cycles)
    {
        Vector v = v0;
        double n = order;
        int i;
        for(i=0; i < max_cycles && (v.x*v.x+v.y*v.y+v.z*v.z < 2.0); i++) {
            double r         = do_r(v);
            double theta     = do_theta(n,v);
            double phi       = do_phi(n,v);
            double rn        = std::pow(r,n);
            double cos_theta = std::cos(theta);
            double sin_theta = std::sin(theta);
            double cos_phi   = std::cos(phi);
            double sin_phi   = std::sin(phi);
            Vector vn = {
                rn * cos_theta * cos_phi,
                rn * sin_theta * cos_phi,
                -rn * sin_phi
            };
            v.x = vn.x + v0.x;
            v.y = vn.y + v0.y;
            v.z = vn.z + v0.z;
        }
        return i;
    }

    public:

    Mandelbulb(
            unsigned width,
            unsigned height,
            unsigned depth,
            int z_offset,
            float range=1.2,
            unsigned nprocs=1)
    : m_coord_x(width)
    , m_coord_y(height)
    , m_coord_z(depth+1)
    , m_extents(6)
    , m_origin(3)
    , m_data(width*height*(depth+1))
    , m_z_offset(z_offset)
    , m_range(range)
    , m_nprocs(nprocs) {
        for(int x = 0; x < width; x++)   m_coord_x[x] = (double)x;
        for(int y = 0; y < height; y++)  m_coord_y[y] = (double)y;
        for(int z = 0; z < depth; z++)   m_coord_z[z] = (double)(z+z_offset);
        m_extents[4] = 0;
        m_extents[5] = m_coord_x.size()-1;
        m_extents[2] = 0;
        m_extents[3] = m_coord_y.size()-1;
        m_extents[0] = z_offset;
        m_extents[1] = z_offset + m_coord_z.size() - 1;
        m_origin[1] = m_origin[2] = 0;
        m_origin[0] = z_offset;
    }

    Mandelbulb(const Mandelbulb&)            = default;
    Mandelbulb(Mandelbulb&&)                 = default;
    Mandelbulb& operator=(const Mandelbulb&) = default;
    Mandelbulb& operator=(Mandelbulb&&)      = default;
    ~Mandelbulb()                            = default;

    void compute(double order, unsigned max_cycles=100) {
        auto width  = m_coord_x.size();
        auto height = m_coord_y.size();
        auto depth  = m_coord_z.size();
        for(unsigned z = 0; z < depth;  z++)
        for(unsigned y = 0; y < height; y++)
        for(unsigned x = 0; x < width;  x++)
        {
            Vector v = {
                2.0*m_range*x/width - m_range,
                2.0*m_range*y/height - m_range,
                2.0*m_range*(z+m_z_offset)/((depth-1)*m_nprocs) - m_range
            };
            value_at(x,y,z) = iterate(v, order, max_cycles);
        }
    }

    void writeBIN(const std::string& filename) {
        std::ofstream ofile(filename.c_str(), std::ios::binary);
        ofile.write((char*)m_data.data(), sizeof(int)*m_data.size());
    }

#ifdef USE_HDF5
    void writeHDF5(const std::string& filename) {
        hid_t file, dataset, dataspace;
        hsize_t dims[3];
        herr_t status;

        file = H5Fcreate(filename.c_str(), H5F_ACC_TRUNC, H5P_DEFAULT, H5P_DEFAULT);
        if(file < 0) throw std::runtime_error("H5Fcreate failed");

        dims[0] = m_coord_x.size();
        dims[1] = m_coord_y.size();
        dims[2] = m_coord_z.size();
        dataspace = H5Screate_simple(3, dims, NULL);
        dataset = H5Dcreate(file, "mandelbulb", H5T_NATIVE_INT, dataspace, H5P_DEFAULT, H5P_DEFAULT, H5P_DEFAULT);
        status = H5Dwrite(dataset, H5T_NATIVE_INT, H5S_ALL, H5S_ALL, H5P_DEFAULT, m_data.data());
        H5Sclose(dataspace);
        H5Dclose(dataset);

        dims[0] = m_coord_x.size();
        dataspace = H5Screate_simple(1, dims, NULL);
        dataset = H5Dcreate(file, "coord_x", H5T_NATIVE_DOUBLE, dataspace, H5P_DEFAULT, H5P_DEFAULT, H5P_DEFAULT);
        status = H5Dwrite(dataset, H5T_NATIVE_DOUBLE, H5S_ALL, H5S_ALL, H5P_DEFAULT, m_coord_x.data());
        H5Sclose(dataspace);
        H5Dclose(dataset);

        dims[0] = m_coord_y.size();
        dataspace = H5Screate_simple(1, dims, NULL);
        dataset = H5Dcreate(file, "coord_y", H5T_NATIVE_DOUBLE, dataspace, H5P_DEFAULT, H5P_DEFAULT, H5P_DEFAULT);
        status = H5Dwrite(dataset, H5T_NATIVE_DOUBLE, H5S_ALL, H5S_ALL, H5P_DEFAULT, m_coord_y.data());
        H5Sclose(dataspace);
        H5Dclose(dataset);

        dims[0] = m_coord_z.size();
        dataspace = H5Screate_simple(1, dims, NULL);
        dataset = H5Dcreate(file, "coord_z", H5T_NATIVE_DOUBLE, dataspace, H5P_DEFAULT, H5P_DEFAULT, H5P_DEFAULT);
        status = H5Dwrite(dataset, H5T_NATIVE_DOUBLE, H5S_ALL, H5S_ALL, H5P_DEFAULT, m_coord_z.data());
        H5Sclose(dataspace);
        H5Dclose(dataset);

        H5Fclose(file);
    }
#endif

    unsigned int* GetExtents() const {
        return const_cast<unsigned int*>(m_extents.data());
    }

    double* GetOrigin() const {
        return const_cast<double*>(m_origin.data());
    }

    int* GetData() const {
        return const_cast<int*>(m_data.data());
    }

    int GetNumberOfLocalCells() const {
        return m_data.size();
    }

    private:

    std::vector<double> m_coord_x;
    std::vector<double> m_coord_y;
    std::vector<double> m_coord_z;
    std::vector<unsigned int> m_extents;
    std::vector<double> m_origin;
    std::vector<int>    m_data;
    const int           m_z_offset;
    const float         m_range;
    const unsigned      m_nprocs;
};

