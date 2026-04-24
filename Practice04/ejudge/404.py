def squares(a, b):
    for i in range(a, b + 1):
        yield i**2
t = input().split()
i, j = int(t[0]), int(t[1])
o = squares(i, j)
for i in o:
    print(i)