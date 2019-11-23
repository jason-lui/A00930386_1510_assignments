def dijkstra(dutch: list):
    """
    Sort a list of 'red', 'white' and 'blue' strings based on the Dutch flag partition.

    :param dutch: a list
    :precondition: dutch_colors must be a list of strings containing only 'red', 'white' and 'blue' strings
    :postcondition: the list will be sorted by 'red', 'white', 'blue' in place
    """
    red, mid, blue = 0, 0, len(dutch) - 1
    while mid <= blue:
        # Element is red, sort it to the beginning of the list
        if dutch[mid] == "red":
            dutch[mid], dutch[red] = dutch[red], dutch[mid]
            red, mid = red + 1, mid + 1

        # Element is white, leave it
        elif dutch[mid] == "white":
            mid += 1

        # Element is blue, sort it to the end of the list
        elif dutch[mid] == "blue":
            dutch[mid], dutch[blue] = dutch[blue], dutch[mid]
            blue -= 1