nums = [10, 20, 5, 40]
nums.sort()
print("Second Smallest:", nums[1])


a = [1, 2, 3]
b = [3, 4, 5]
merged = list(set(a + b))
print("Merged:", merged)


nums = [1, 2, 2, 3, 3, 3]
freq = {}
for n in nums:
    freq[n] = freq.get(n, 0) + 1
print(freq)