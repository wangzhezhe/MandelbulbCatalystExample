### Building

The first option is to install the Paraview by spack and then build this project.
For example on Cori cluster, we could install paraview by this way:

```
module load spack
spack install paraview@5.7.0+osmesa ^mesa~llvm %gcc@8.3.0
```

The second option is to build the paraview manually and then build this project.
This is an exmaple to build it on Cori cluster


1. load necessary modules and set the env

```
module load python3
module load spack
spack load cmake/r3gginj
spack load -r mesa/qozjngg
# for compiling vtk on cori
export CRAYPE_LINK_TYPE=dynamic
```


2. Swictch to the v5.7.0 for the paraview, then execute `cmake ~/cworkspace/src/ParaView/ -DCMAKE_CXX_COMPILER=CC -DCMAKE_C_COMPILER=cc`
(**It is important to use the CC and cc, please do not load other MPI and let the cmake find the MPIEXEC automatically**)
use `ccmake .` to set the necessary configurations, or using `-D` parameter to tell cmake direactly 

```
-DPARAVIEW_BUILD_QT_GUI=OFF 
-DPARAVIEW_ENABLE_PYTHON=ON 
-DPARAVIEW_ENABLE_CATALYST=ON 
-DPARAVIEW_USE_MPI=ON 
-DVTK_OPENGL_HAS_OSMESA:BOOL=TRUE 
-DVTK_USE_X:BOOL=FALSE
```

3. After building the paraview, please use following commands to build the mandlebulb (in our example, the build dir for paraview is `/global/cscratch1/sd/zw241/build_paraview/`)


```
cmake ~/cworkspace/src/MandelbulbCatalystExample/ -DCMAKE_CXX_COMPILER=CC -DCMAKE_C_COMPILER=cc -DParaView_DIR=/global/cscratch1/sd/zw241/build_paraview/
```


**other related issues**:

If there is error about the `unreference to uuid`, please add this into the CMakeLists `SET(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -luuid")`
