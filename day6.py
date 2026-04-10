nums = [10, 20, 5, 40]

print("Max:", max(nums))
print("Min:", min(nums))

nums = [10, 20, 5, 40]

nums.sort()
print("Second Largest:", nums[-2])

nums = [1, 2, 2, 3, 4, 4]

unique = list(set(nums))
print("Unique:", unique)

nums = [1, 2, 3, 4, 5, 6]

even = 0
odd = 0

for n in nums:
    if n % 2 == 0:
        even += 1
    else:
        odd += 1

print("Even:", even)
print("Odd:", odd)