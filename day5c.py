nums = [10, 20, 30, 40, 50]
nums.sort()
print(nums[-2])


text = "python"
freq = {}
for ch in text:
    if ch in freq:
        freq[ch] += 1
    else:
        freq[ch] = 1
print(freq)


nums = [1, 2, 2, 3, 4, 4, 5]
unique = list(set(nums))
print(unique)