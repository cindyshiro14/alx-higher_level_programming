#include <Python.h>

/**
 * print_python_bytes - Print information about a Python bytes object
 * @p: Python bytes object
 */
void print_python_bytes(PyObject *p)
{
    int size, i;
    char *str;

    printf("[.] bytes object info\n");
    if (!PyBytes_Check(p))
    {
        printf("  [ERROR] Invalid Bytes Object\n");
        return;
    }

    size = (int)PyBytes_Size(p);
    str = PyBytes_AsString(p);

    printf("  size: %d\n", size);
    printf("  trying string: %s\n", str);

    if (size < 10)
        printf("  first %d bytes:", size + 1);
    else
        printf("  first 10 bytes:");

    for (i = 0; i <= size && i < 10; i++)
        printf(" %02x", str[i]);

    printf("\n");
}

/**
 * print_python_list - Print information about a Python list
 * @p: Python list object
 */
void print_python_list(PyObject *p)
{
    int size, i;
    PyObject *item;

    printf("[*] Python list info\n");

    size = (int)PyList_Size(p);
    printf("[*] Size of the Python List = %d\n", size);
    printf("[*] Allocated = %d\n", (int)(((PyListObject *)p)->allocated));

    for (i = 0; i < size; i++)
    {
        item = PyList_GetItem(p, i);
        printf("Element %d: %s\n", i, item->ob_type->tp_name);
        
        if (PyBytes_Check(item))
            print_python_bytes(item);
    }
}
