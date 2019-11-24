import doctest


def selection_sort(item_list: list) -> list:
    """
    Sorts a list of items using selection sort.

    :param item_list: a list
    :precondition: item_list must be a non-empty list of sortable items
    :postcondition: the item_list will be sorted
    :return: a sorted copy of item_list

    >>> selection_sort([])
    Traceback (most recent call last):
    ...
    ValueError: item_list must have elements
    >>> selection_sort([3, 2, 1])
    [1, 2, 3]
    >>> selection_sort(['bae', 'Bae', 'bAe'])
    ['Bae', 'bAe', 'bae']
    >>> selection_sort([3.3, 1.1, 2.2])
    [1.1, 2.2, 3.3]
    >>> selection_sort([False, True, False])
    [False, False, True]
    """
    if not item_list:  # Empty list
        raise ValueError("item_list must have elements")

    copy = item_list[:]  # Copy the list to preserve original list

    for write_in, value in enumerate(copy):
        min_in = write_in  # Set min_in to remember which index the function will write to
        for i in range(write_in, len(copy)):
            if copy[i] < copy[min_in]:  # There is a lower number
                min_in = i
        copy[min_in], copy[write_in] = copy[write_in], copy[min_in]  # Swap the values

    return copy


if __name__ == '__main__':
    doctest.testmod()
