set(Adaptor_SRCS
    ${CMAKE_SOURCE_DIR}/src/InSituAdaptor.cpp
    )
add_library(CatalystMandelbulbAdaptor ${Adaptor_SRCS})
target_link_libraries(CatalystMandelbulbAdaptor vtkPVPythonCatalyst vtkParallelMPI)

add_executable(Mandelbulb 
     ${CMAKE_SOURCE_DIR}/src/Mandelbulb.cpp)

target_link_libraries(Mandelbulb LINK_PRIVATE CatalystMandelbulbAdaptor ${HDF5_LIBRARIES})
include(vtkModuleMacros)
include(vtkMPI)
vtk_mpi_link(Mandelbulb)
