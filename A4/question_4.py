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
    ValueError: item_list must be a non-empty
    >>> selection_sort([3, 2, 1])
    [1, 2, 3]
    >>> selection_sort(['bae', 'Bae'])
    ['Bae', 'bae']
    >>> selection_sort([3.3, 1.1, 2.2])
    [1.1, 2.2, 3.3]
    >>> selection_sort([False, True, False])
    [False, False, True]
    """
    if not item_list:
        raise ValueError("item_list must be a non-empty")

    list_copy = item_list[:]
    write_index = 0

    while write_index < len(list_copy):
        min_index = write_index
        for i in range(write_index, len(list_copy)):
            if list_copy[i] < list_copy[min_index]:
                min_index = i
        list_copy[min_index], list_copy[write_index] = list_copy[write_index], list_copy[min_index]
        write_index += 1

    return list_copy


if __name__ == '__main__':
    doctest.testmod()
