#define PY_SSIZE_T_CLEAN
#include <python3.8/Python.h>
/**
 * print_python_list_info - print python list info
 * @p: list
 * Return: NULL
 */
void print_python_list_info(PyObject *p)
{
	Py_ssize_t len = PyList_Size(p);
	Py_ssize_t i;

	printf("[*] Size of the Python List = %zd\n", len);
	printf("[*] Allocated = %zd\n", sizeof(p));
	for (i = 0; i < len; i++)
	{
		PyObject *item = PyList_GetItem(p, i);

		printf("Element %zd: %s\n", i, Py_TYPE(item)->tp_name);
	}
}
