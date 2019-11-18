def im_not_sleepy():
    """

    :return:
    """

    max_times = []
    hours = max_bars(1, 12)
    tens = max_bars(0, 5)
    minutes = max_bars(0, 9)

    for h in hours:
        for t in tens:
            for m in minutes:
                max_times.append(str(h) + ":" + str(t) + str(m))

    bar_sum = time_to_bars(max_times[0])

    return max_times, bar_sum


def max_bars(lower_bound, upper_bound):
    """

    :param lower_bound:
    :param upper_bound:
    :return:
    """
    bar_dict = {0: 6, 1: 2, 2: 5, 3: 5, 4: 4, 5: 5, 6: 6, 7: 3, 8: 7, 9: 6, 10: 8, 11: 4, 12: 7}
    res = []
    max_value = 0

    for i in range(lower_bound, upper_bound):
        if bar_dict[i] > max_value:
            max_value = bar_dict[i]

    for i in range(lower_bound, upper_bound):
        if bar_dict[i] == max_value:
            res.append(i)

    return res


def time_to_bars(time_str: str) -> int:
    """

    :param time_str:
    :return:
    """
    bar_dict = {0: 6, 1: 2, 2: 5, 3: 5, 4: 4, 5: 5, 6: 6, 7: 3, 8: 7, 9: 6, 10: 8, 11: 4, 12: 7}
    total_bars = 0

    for char in time_str:
        if char.isnumeric():
            total_bars += bar_dict[int(char)]

    return total_bars


print(im_not_sleepy())
