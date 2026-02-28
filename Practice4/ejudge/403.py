j = int(input())

def f(n):
    for i in range(0, n + 1, 12):
        yield i
k = f(j)
for i in k:
    print(i, end=" ")