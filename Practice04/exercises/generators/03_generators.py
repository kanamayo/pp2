def f(n):
    for i in range(0, n + 1):
        if i % 12 == 0: yield(i)
a = int(input())
b = f(a)
for i in b:
    print(i, end=" ")