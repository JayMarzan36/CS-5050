def Fib(x):
    if x < 2:
        return x

    return Fib(x - 1) + Fib(x - 2)


def Fib2(x):
    # Dynamic programming version
    fib = [0 for _ in range(x + 1)]

    fib[0] = 0

    fib[1] = 1

    for i in range(2, x + 1, 1):
        fib[i] = fib[i - 1] + fib[i - 2]

    return fib[x]


def T(x):
    """
    T(x) that gives a number of 'basic computer steps' for each x. For Fib,
    1 comparison, 2 subtraction, 1 addition, 2 recursive calls. This is where the 6 comes from.

    Args:
        x (int): x

    Returns:
        int: amount of basic computer steps
    """
    return 6 + T(x - 1) + T(x - 2)


def T2(x):
    """
    T(x) that gives a number of 'basic computer steps' for each x. For Fib2,

    2 assignments, 1 initialization. Each loop has 2 reads and 1 assignment.

    Args:
        x (_type_): _description_

    Returns:
        _type_: _description_
    """
    return 7 * x - 4
