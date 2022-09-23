def factorial_recursive(n: int) -> int:
    """
    Calculate factorial of number n (> 0) in recursive way
    :param n: int > 0
    :return: factorial of n
    """
    if n < 0:
        raise ValueError
    if n in (0,1):
        return 1
    else:
        return n * factorial_recursive(n-1)

def factorial_iterative(n: int) -> int:
    """
    Calculate factorial of number n (> 0) in iterative way

    :param n: int > 0
    :return: factorial of n
    """
    if n < 0:
        raise ValueError
    factorial = 1
    if n in (0,1):
        return factorial
    for i in range(1, n + 1):
        factorial *= i
    print(n)
    return factorial

def factorial_generator(n):
    if n < 0:
        raise ValueError
    value = 1
    for i in range(1, n+1):
        yield value
        value *= i

