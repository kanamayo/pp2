def f(n):
    for i in range(0, n + 1, 2):
        yield(i)
a = int(input())
b = f(a)
for i in b:
    print(i, end="")
    if i == (a - (a % 2)):
        break
    print(', ', end='')