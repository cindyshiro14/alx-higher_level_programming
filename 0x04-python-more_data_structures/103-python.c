#include <Python.h>

void print_python_bytes(PyObject *p)
{
    int size, i;
    char *str;
    char *raw_data;

    printf("[.] bytes object info\n");

    if (!p || !PyBytes_Check(p))
    {
        printf("  [ERROR] Invalid Bytes Object\n");
        return;
    }

    size = (int)((PyVarObject *)p)->ob_size;
    raw_data = ((PyBytesObject *)p)->ob_sval;
    str = size > 10 ? raw_data : ((PyBytesObject *)p)->ob_sval;

    printf("  size: %d\n", size);
    printf("  trying string: %s\n", str);

    printf("  first %d bytes:", size + 1);
    for (i = 0; i <= size && i < 10; i++)
        printf(" %02x", (unsigned char)raw_data[i]);

    printf("\n");
}

void print_python_list(PyObject *p)
{
    int size, i;
    PyObject *item;

    printf("[*] Python list info\n");

    if (!p || !PyList_Check(p))
    {
        printf("  [ERROR] Invalid List Object\n");
        return;
    }

    size = (int)((PyVarObject *)p)->ob_size;
    printf("[*] Size of the Python List = %d\n", size);
    printf("[*] Allocated = %d\n", (int)((PyListObject *)p)->allocated);

    for (i = 0; i < size; i++)
    {
        item = ((PyListObject *)p)->ob_item[i];
        printf("Element %d: %s\n", i, item->ob_type->tp_name);

        if (PyBytes_Check(item))
            print_python_bytes(item);
    }
}
