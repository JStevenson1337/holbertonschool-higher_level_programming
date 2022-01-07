#include "lists.h"

/*
The steps for interfacing Python with C using Ctypes. are:
write C code functions
compile the C code as a shared library
write some Python lines of code to “extract” the C functions from the library
run!
*/

void print_python_list_info(PyObject *p)

