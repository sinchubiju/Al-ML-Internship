# print("Hello
print("Hello")

#    x = int("abc")
x = int("123")    
print(x)    

# nums = [1, 2, 3]
# print(nums[5])
nums = [1, 2, 3]
print(nums[2])


# nums = [4, 2, 1, 3]
# nums.sort()
# print(nums)
nums = [4, 2, 1, 3]
print(sorted(nums))


# a = 5 + 10
# b = 7 + 10
# c = 3 + 10
# print(a, b, c)
def add_ten(x):
    return x + 10
print(add_ten(5), add_ten(7), add_ten(3))


# nums = [1, 2, 3, 4]
# total = 0
# for i in nums:
#     total += i
# print(total)
def get_sum(nums):
    return sum(nums)
nums = [1, 2, 3, 4]
print(get_sum(nums))