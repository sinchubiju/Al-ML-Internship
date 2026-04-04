# def add(a, b):
#     return a + b

# x = 6
# y = 4

# print("Result:", add(x, y))

# def is_prime(n):
#     if n <= 1:
#         return False
#     for i in range(2, n):
#         if n % i == 0:
#             return False
#     return True

# num = 7

# if is_prime(num):
#     print("Prime")
# else:
#     print("Not Prime")

def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

num =5
print("Factorial:", factorial(num))