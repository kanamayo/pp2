def f(n):
    for i in range(1, n + 1):
        yield(i)
a = int(input())
b = f(a)
for i in b:
    print(i, end=" ")