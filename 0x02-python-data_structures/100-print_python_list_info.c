#include "lists.h"

/*
The steps for interfacing Python with C using Ctypes. are:
write C code functions
compile the C code as a shared library
write some Python lines of code to “extract” the C functions from the library
run!
*/

void print_python_list_info(PyObject *p)
{
    printf("Python list has %d elements\n", PyList_Size(p));
    printf("Python list has %d bytes\n", PyList_Size(p) * sizeof(PyObject *));

    PyObject *item;
    int i;
    for (i = 0; i < PyList_Size(p); i++)
    {
        item = PyList_GetItem(p, i);
        printf("Python list element %d is %s\n", i, Py_TYPE(item)->tp_name);
    }

    printf("Python list has %d bytes\n", PyList_Size(p) * sizeof(PyObject *));
    return;

    
}

