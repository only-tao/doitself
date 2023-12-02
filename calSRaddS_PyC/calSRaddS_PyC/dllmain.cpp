#define NPY_NO_DEPRECATED_API NPY_1_7_API_VERSION

#include <Python.h>
#include <math.h>
#include <numpy/arrayobject.h>
// you can don't use the precompiled header. configure in 项目-属性-c++=。找到项目属性 -> C/C++ -> 预编译头，然后将 "预编译头" 设置为 "不使用预编译头"。
static PyObject* calSquareRootAndSquare_PyC(PyObject* self, PyObject* args) {
    long N;
    PyObject* result;
    if (!PyArg_ParseTuple(args, "lO", &N,&result)) {
        return NULL;
    }
    if (!PyArray_Check(result)) {
        PyErr_SetString(PyExc_TypeError, "Second argument must be a NumPy array.");
        return NULL;
    }
    //double*  result= new double[N];
    // 获取 result 数组的指针
    double* result_data = (double*)PyArray_DATA((PyArrayObject*)result);

    for (long i = 0; i < N; i++) {
        result_data[i] = sqrt(i) + pow(i, 2);
    }

    Py_RETURN_NONE;
}

static PyMethodDef methods[] = {
    {"calSquareRootAndSquare_PyC", calSquareRootAndSquare_PyC, METH_VARARGS, "Calculate square root add square."},
    {NULL, NULL, 0, NULL}  // Sentinel
};

static struct PyModuleDef module = {
    PyModuleDef_HEAD_INIT,
    "calSquareRootAndSquare_PyC",  // Module name
    NULL,           // Documentation
    -1,             // Size of per-interpreter state or -1
    methods         // Methods table
};

PyMODINIT_FUNC PyInit_calSquareRootAndSquare_PyC(void) {
    import_array();
    return PyModule_Create(&module);
}
PyMODINIT_FUNC PyInit_calSquareRootAndSquare_PyCG(void) {
    import_array();
    return PyModule_Create(&module);
}
