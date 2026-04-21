def count(n):
    for i in range(n):
        yield i

for num in count(5):
    print(num)


def even_gen(n):
    for i in range(n):
        if i % 2 == 0:
            yield i

for num in even_gen(6):
    print(num)


def fib(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

for num in fib(6):
    print(num)

names = ["A", "B"]
marks = [80, 90]
combined = list(zip(names, marks))
print(combined)


names = ["AI", "ML"]
for i, name in enumerate(names):
    print(i, name)

names = ["A", "B"]
marks = [80, 90]
result = dict(zip(names, marks))
print(result)