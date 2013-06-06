# symmetric matrix
import numpy


class SymNDArray(numpy.ndarray):
    def setitem(self, i, j, value):
        super(SymNDArray, self).setitem(i, j, value)
        super(SymNDArray, self).setitem(j, i, value)


def symarray(input_array):
    """
    Returns a symmetrized version of the array-like input_array.
    Further assignments to the array are automatically symmetrized.
    """
    return numpy.asarray(input_array).view(SymNDArray)

if __name__ == "__main__":
    import numpy
    a = symarray(numpy.zeros((3, 3)))
    a[0, 1] = 42
    print(a)
    print(a[0, 1])
    print(a[1, 0])
