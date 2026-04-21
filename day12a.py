nums = [1, 2, 3]
square_dict = {x: x*x for x in nums}
print(square_dict)

nums = [1, 2, 3, 4]
even_dict = {x: x*x for x in nums if x % 2 == 0}
print(even_dict)

names = ["AI", "ML", "Python"]
length_dict = {name: len(name) for name in names}
print(length_dict)