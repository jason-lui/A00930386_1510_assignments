def selection_sort(arr: list) -> list:
    """

    :param arr:
    :return:
    """
    if not arr:
        print("List is empty")
        return

    sort_index = 0

    while sort_index < len(arr):
        min_index = sort_index
        for i in range(sort_index, len(arr)):
            if arr[i] < arr[min_index]:
                min_index = i
        arr[min_index], arr[sort_index] = arr[sort_index], arr[min_index]
        sort_index += 1

    return arr


# unsorted = [3, 5, 1, 9, -4]
# sorted_copy = selection_sort(unsorted)
# print(sorted_copy)
# [-4, 1, 3, 5, 9]
