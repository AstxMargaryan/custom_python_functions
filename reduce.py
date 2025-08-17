# Implementing reduce


import typing


def custom_reduce(func, iterable, initializer=None):
    """
    Replicates the behavior of Python's built-in reduce function.

    Parameters:
        func (callable): Function of two arguments to apply cumulatively.
        iterable (iterable): Iterable of elements to reduce.
        initializer (optional): Initial value to start the reduction.

    Returns:
        The final reduced value.

    Raises:
        TypeError: If iterable is not iterable or func is not callable.
        TypeError: If iterable is empty and initializer is not provided.
    """
    if not isinstance(iterable, typing.Iterable):
        raise TypeError("Tur indz iteracvox tip")

    if not callable(func):
        raise TypeError("Tur indz kanchvox tip")

    if not iterable:
        if initializer == None:
            raise TypeError("Tur indz gone initializer")
        else:
            return initializer

    if initializer != None:
        res1 = initializer
        start = 0
    else:
        res1 = iterable[0]
        start = 1

    for i in range(start, len(iterable)):
        res1 = func(res1, iterable[i])
    return res1


ls = [1, 2, 3, 4, 5]
print(custom_reduce(lambda x, y: x + y, ls, initializer=None))