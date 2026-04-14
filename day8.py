def factorial(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    return fact
print(factorial(5))


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

print(is_prime(7))


def reverse_string(s):
    return s[::-1]
print(reverse_string("python"))


def average(nums):
    return sum(nums) / len(nums)
print(average([10, 20, 30]))