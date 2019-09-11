#include <pybind11/pybind11.h>


int adds(int i, int j) {
    return i + j;
}


namespace py = pybind11;

PYBIND11_MODULE(add, m) {
    // optional module docstring
    m.doc() = "pybind11 example plugin";
    
    // define add function
    m.def("add", &adds, "A function which adds two numbers");
    
}
