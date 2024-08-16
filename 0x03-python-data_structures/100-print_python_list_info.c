#include <Python.h>
#include <stdio.h>

/**
 * print_python_list_info - Prints basic information about a Python list.
 * @p: PyObject pointer to the Python list
 */
void print_python_list_info(PyObject *p)
{
    Py_ssize_t size, alloc, i;
    PyObject *item;

    if (!PyList_Check(p))
    {
        fprintf(stderr, "Error: The provided PyObject is not a list\n");
        return;
    }

    size = PyList_Size(p);
    alloc = ((PyListObject *)p)->allocated;

    printf("[*] Size of the Python List = %zd\n", size);
    printf("[*] Allocated = %zd\n", alloc);

    for (i = 0; i < size; i++)
    {
        item = PyList_GetItem(p, i); // Get the i-th item
        if (item == NULL)
        {
            fprintf(stderr, "Error: Could not retrieve list item\n");
            continue;
        }

        // Print the type of each element
        if (PyUnicode_Check(item))
            printf("Element %zd: str\n", i);
        else if (PyLong_Check(item))
            printf("Element %zd: int\n", i);
        else if (PyFloat_Check(item))
            printf("Element %zd: float\n", i);
        else if (PyTuple_Check(item))
            printf("Element %zd: tuple\n", i);
        else if (PyList_Check(item))
            printf("Element %zd: list\n", i);
        else
            printf("Element %zd: unknown\n", i);
    }
}
