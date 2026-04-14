def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)
print(factorial(5))


def sum_numbers(n):
    if n == 1:
        return 1
    return n + sum_numbers(n-1)
print(sum_numbers(5))


def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)
for i in range(6):
    print(fibonacci(i), end=" ")