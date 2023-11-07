

def fib(n):
    if n < 0:
        return None
    if n == 0:
        return 0
    if n == 1 or n == 2:
        return 1
    return fib(n-1) + fib(n-2)


print(fib(9))


# Dynamic approach

fib_array = [0, 1]


def fibonacci(n):

    if n < 0:
        return None

    if n < len(fib_array):
        return fib_array[n]
    else:
        fib_array.append(fibonacci(n-1) + fibonacci(n-2))
        return fib_array[n]


print(fibonacci(9))
