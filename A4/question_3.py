def dijkstra(dutch_colors: list):
    """
    Sort a list of 'red', 'white' and 'blue' strings based on the Dutch flag partition.

    :param dutch_colors: a list
    :precondition: dutch_colors must be a list of strings containing only 'red', 'white' and 'blue' strings
    :postcondition: the list will be sorted by 'red', 'white', 'blue' in place
    """
    red = 0
    blue = len(dutch_colors) - 1

    # Sort 'red's to the beginning of the list
    for i, color in enumerate(dutch_colors):
        if color == 'red':
            dutch_colors[i], dutch_colors[red] = dutch_colors[red], dutch_colors[i]
            red += 1  # Increment write index

    # Sort 'blue's to the end of the list
    for i, color in enumerate(reversed(dutch_colors)):
        i = len(dutch_colors) - 1 - i  # Generate indices to iterate backwards through the list
        if color == 'blue':
            dutch_colors[i], dutch_colors[blue] = dutch_colors[blue], dutch_colors[i]
            blue -= 1  # Decrement write index
