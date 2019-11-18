def dijkstra(arr: list):
    """

    :param arr:
    :return:
    """
    red = 0
    blue = len(arr) - 1

    for i, color in enumerate(arr):
        if color == 'red':
            arr[i], arr[red] = arr[red], arr[i]
            red += 1
    for i in reversed(range(len(arr))):
        if arr[i] == 'blue':
            arr[i], arr[blue] = arr[blue], arr[i]
            blue -= 1


# dutch = ['white', 'blue', 'blue', 'red', 'white', 'red', 'white']
# dijkstra(dutch)
# print(dutch)
