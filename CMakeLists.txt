cmake_minimum_required(VERSION 3.3)
project(Mandelbulb CXX C)

enable_language(CXX)
find_package(ParaView 4.2 REQUIRED COMPONENTS vtkPVPythonCatalyst)
include("${PARAVIEW_USE_FILE}")
if(NOT PARAVIEW_USE_MPI)
  message(SEND_ERROR "ParaView must be built with MPI enabled")
endif()
find_package(MPI REQUIRED)
include_directories(${MPI_C_INCLUDE_PATH})

#find_package(HDF5 REQUIRED)
#include_directories(${HDF5_INCLUDE_DIRS})

add_subdirectory(bin)
