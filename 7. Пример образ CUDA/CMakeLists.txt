cmake_minimum_required(VERSION 3.8 FATAL_ERROR)
project(main LANGUAGES CXX CUDA)
 
 
add_executable(${CMAKE_PROJECT_NAME} main.cu)
 
# We need to explicitly state that we need all CUDA files in the 
# particle library to be built with -dc as the member functions 
# could be called by other libraries and executables
set_target_properties(${CMAKE_PROJECT_NAME} PROPERTIES CUDA_SEPARABLE_COMPILATION ON)
