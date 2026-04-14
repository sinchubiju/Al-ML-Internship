nums = [1, 2, 3, 4]
result = list(filter(lambda x: x % 2 == 0, nums))
print(result)


marks = [40, 60, 70, 30]
result = list(filter(lambda x: x > 50, marks))
print(result)


words = ["apple", "banana", "kiwi", "grapes"]
result = list(filter(lambda x: len(x) > 5, words))
print(result)