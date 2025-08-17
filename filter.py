# Implementing filter

import typing


def custom_filter(f, iterable):
    
    """
    Replicates the behavior of the built-in filter function.

    Parameters:
        f (callable): A function that returns True or False.
        iterable (iterable): An iterable of items to filter.

    Returns:
        list: A list of items for which func(item) is True.
    """
    res = []
    if f is None:
        for i in iterable:
            if i:
                res.append(i)
    elif not isinstance(f, typing.Callable):
        raise "must be a function"
    else:
        for i in iterable:
            if f(i):
                res.append(i)
    return res


def is_even(x):
    return x % 2 == 0


numbers = [1, 2, 3, 4, 5, 6]
result = custom_filter(is_even, numbers)
print(result)

arr = [1, "", 0, 23]
res = custom_filter(None, arr)
print(res)


# Generator version of custom_filter

def custom_filter_with_yield(f, iterable):
    """
    Replicates the behavior of the built-in filter function using a generator.

    Parameters:
        f (callable): A function that returns True or False.
        iterable (iterable): An iterable of items to filter.

    Yields:
        item: Items for which func(item) is True.
    """
    if f is None:
        for i in iterable:
            if i:
                yield i
    elif not isinstance(f, typing.Callable):
        raise TypeError('tur funkcia')
    else:
        for i in iterable:
            if f(i):
                yield i


res = custom_filter_with_yield(None, ["", 1])
print(list(res))
res2 = custom_filter_with_yield(lambda x: x > 0, [1, 2, -1, 0])
print(list(res2))