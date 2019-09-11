cmake_minimum_required (VERSION 2.6)
project (learning-good-practices)

add_subdirectory(functions)
pybind11_add_module(add add.cpp)
