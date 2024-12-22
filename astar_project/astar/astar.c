#include <Python.h>

static PyObject* say_hello(PyObject* self, PyObject* args) {
    return Py_BuildValue("s", "Hello from C extension!");
}

static PyObject* sum_integers(PyObject* self, PyObject* args) {
    PyObject *input_list;
    long sum = 0;

    // Parse the input argument as a Python list
    if (!PyArg_ParseTuple(args, "O", &input_list)) {
        return NULL;  // If the argument isn't a list, return an error
    }

    // Check if the input is indeed a list
    if (!PyList_Check(input_list)) {
        PyErr_SetString(PyExc_TypeError, "Expected a list of integers");
        return NULL;
    }

    // Iterate through the list and sum the integers
    Py_ssize_t size = PyList_Size(input_list);
    for (Py_ssize_t i = 0; i < size; i++) {
        PyObject *item = PyList_GetItem(input_list, i);
        if (!PyLong_Check(item)) {
            PyErr_SetString(PyExc_TypeError, "All elements must be integers");
            return NULL;
        }
        sum += PyLong_AsLong(item);
    }

    // Return the sum as a Python integer
    return PyLong_FromLong(sum);
}

static PyMethodDef ExampleMethods[] = {
    {"say_hello", say_hello, METH_VARARGS, "Say hello from C extension"},
    {"sum_integers", sum_integers, METH_VARARGS, "Sum the integers in a list"},
    {NULL, NULL, 0, NULL}  // Sentinel value
};

static struct PyModuleDef astar_astarmodule = {
    PyModuleDef_HEAD_INIT,
    "astar",  // Module name in the package
    "Example module",  // Module documentation
    -1,  // Size of the module state, -1 if the module keeps state in global variables
    ExampleMethods  // Method table
};

PyMODINIT_FUNC PyInit_astar(void) {
    return PyModule_Create(&astar_astarmodule);
}
