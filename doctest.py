def average(value):
    """Computes the arithmetic mean of given numbers.
    >>>print(average([10,20,30,40]))
    """
    return sum(value)/len(value)

import doctest
doctest.testmod()