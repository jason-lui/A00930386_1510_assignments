"""
#1) Test 2 parallel lines that do not intersect.
    Example: [[0.0, 0.0], [1.0, 1.0]] and [[1.0, 1.0], [2.0, 2.0]]

#2) Test 2 identical lines that are coincident.
    Example: [[0.0, 0.0], [1.0, 1.0]] and [[1.0, 1.0], [2.0, 2.0]]

#3) Test 2 lines that intersect and both have negative slopes.
    Example: [[1.0, 1.0], [0.0, 0.0]] and [[1.0, 1.0], [0.5, 0.5]]

#4) Test 2 lines that intersect and both have positive slopes
    Example: [[1.0, 1.0], [0.0, 0.0]] and [[1.0, 1.0], [0.5, 0.5]]

#5) Test 2 lines that intersect and one has a negative slope while the other has a positive slope
    Example: [[0.0, 0.0], [1.0, 1.0]] and [[1.0, 1.0], [0.0, 0.0]]

#6) Test 2 lines that intersect and one line is horizontal and the other is vertical
    Example: [[0.0, 0.0], [1.0, 0.0]] and [[0.0, 0.0], [0.0, 1.0]]
"""
