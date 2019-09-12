cmake_minimum_required (VERSION 2.6)
project (learning-good-practices)

add_subdirectory(pybind11)
pybind11_add_module(addition functions/main.cpp)