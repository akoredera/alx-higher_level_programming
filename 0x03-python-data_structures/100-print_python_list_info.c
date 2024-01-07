#define PY_SSIZE_T_CLEAN
#include <Python.h>
void print_python_list_info(PyObject *p)
{
	Py_ssize_t len = PyList_Size(p);
	printf("[*] Size of the Python List = %zd\n", len);
	printf("[*] Allocated = %zd\n", sizeof(p));
	Py_ssize_t i;
	for(i = 0; i < len; i++)
	{
		PyObject *item = PyList_GetItem(p, i)
		printf("Element %zd: %s\n", i, PyTYPE(item)->tp_name);
	}
}
