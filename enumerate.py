#  Implementing enumerate


def custom_enumerate(iterable, start=0):
    """
    Replicates the behavior of Python's built-in enumerate function.

    Parameters:
        iterable (iterable): The iterable to enumerate.
        start (int, optional): The starting index. Default is 0.

    Returns:
        list of tuples: Each tuple contains (index, element) from the iterable.
    """
    res = []
    for i in iterable:
        res.append((start, i))
        start += 1
    return res


fruits = ['apple', 'banana', 'cherry']
result = custom_enumerate(fruits, start=1)
print(result)  # Output: [(1, 'apple'), (2, 'banana'), (3, 'cherry')]
# res2 = custom_enumerate(fruits)
# print(res2)
res = enumerate(['apple', 'banana', 'cherry'], 2)
print(list(res))

# Generator version of custom_enumerate


def custom_enumerate_with_yield(iterable, start=0):
    """
    Generator version of Python's built-in enumerate function.

    Parameters:
        iterable (iterable): The iterable to enumerate.
        start (int, optional): The starting index. Default is 0.

    Yields:
        tuple: (index, element) for each element in the iterable.
    """
    for i in iterable:
        yield start, i
        start += 1


res = custom_enumerate_with_yield([1, 2, 3, 4, 5])
print(list(res))