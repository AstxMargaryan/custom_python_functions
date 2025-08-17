# Implementing zip

def custom_zip(*iterables):
    """
    Replicates the behavior of the built-in zip function.

    Parameters:
        *iterables: One or more iterable objects (lists, tuples, etc.).

    Returns:
        list of tuples: Each tuple contains elements from all iterables at the same index.

    Notes:
        - Iteration stops at the length of the shortest iterable.
    """
    min_elem = len(iterables[0])
    res = []
    for i in iterables:
        if len(i) < min_elem:
            min_elem = len(i)
    for i in range(min_elem):
        tmp = []
        for j in iterables:
            tmp.append(j[i])
        res.append(tuple(tmp))
    return res


list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
result = custom_zip(list1, list2)
print(result)  # Output: [(1, 'a'), (2, 'b'), (3, 'c')]


# Generator version of custom_zip


def zip_generator(*iterables):
    """
    Generator version of the built-in zip function.

    Parameters:
        *iterables: One or more iterable objects (lists, tuples, etc.).

    Yields:
        tuple: Elements from all iterables at the same index.

    Notes:
        - Iteration stops at the length of the shortest iterable.
        - Memory-efficient for large iterables.
    """
    min_val = min([len(i) for i in iterables])
    for i in range(min_val):
        tmp = []
        for j in iterables:
            tmp.append(j[i])
        yield tuple(tmp)


res = zip_generator([1, 2, 3], (4, 5, 6, 7))
print(list(res))