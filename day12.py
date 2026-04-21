nums = [1, 2, 3, 4]
squares = [x*x for x in nums]
print(squares)


nums = [1, 2, 3, 4, 5, 6]
even = [x for x in nums if x % 2 == 0]
print(even)


names = ["ai", "ml", "python"]
upper = [n.upper() for n in names]
print(upper)

nums = [10, 60, 30, 80, 45]
result = [x for x in nums if x > 50]
print(result)