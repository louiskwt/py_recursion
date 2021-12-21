def fib(x):
    """Find the finbonacci sequence using rabbit example"""
    if x == 0 or x == 1:
        return x

    return fib(x - 1) + fib(x - 2)


print(fib(6))
