# Implementing map


def custom_map(f, *iterables):

    """
    Replicates the behavior of the built-in map function for one or more iterables.

    Parameters:
         f (callable): A function to apply to the items of the iterables.
        *iterables: One or more iterable objects (lists, tuples, etc.).

    Returns:
        list: A list containing the results of applying func to the items of the iterables.

    Notes:
        - Iteration stops at the length of the shortest iterable.
        - Supports functions with multiple arguments if multiple iterables are provided.
    """
    min_elem = len(iterables[0])
    for i in iterables:
        if len(i) < min_elem:
            min_elem = len(i)

    res = []
    for i in range(min_elem):
        tmp =[]
        for j in iterables:
            tmp.append(j[i])
        res.append(f(*tmp))
    return res


def square(x):
    return x ** 2


def square2(x, y):
    return x ** y


numbers = [1, 2, 3, 4]
arr = [6, 4]
# result = custom_map(square, numbers)
# print(result)
res = custom_map(square2, numbers, arr)
print(res)


# Generator version of custom_map

def custom_map_with_yield(func, *iterables):
    """
    Generator version of map function.

    Parameters:
        func (callable): Function to apply to elements of the iterables.
        *iterables: One or more iterable objects (lists, tuples, etc.).

    Yields:
        Result of applying func to elements at the same index across iterables.

    Notes:
        - Iteration stops at the length of the shortest iterable.
        - Supports multiple iterables for functions with multiple arguments.
    """
    min_val = min([len(i)for i in iterables])
    for i in range(min_val):
        tmp =[]
        for j in iterables:
             tmp.append(j[i])
        yield func(*tmp)


res = custom_map_with_yield(lambda x, y: x*y, [1, 2, 3], (5, 4))
print(list(res))