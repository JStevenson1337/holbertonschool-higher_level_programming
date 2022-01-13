#include <ctypes.h>
#include <stdio.h>
#include <cpython/initconfig.h>



void print_python_bytes(PyObject *p)
{
    Py_ssize_t i;
    Py_ssize_t size = PyBytes_Size(p);
    char *buf = PyBytes_AsString(p);
    for (i = 0; i < size; i++) {
        printf("%c", isprint(buf[i]) ? buf[i] : '.');
    }
    printf("\n");
}
