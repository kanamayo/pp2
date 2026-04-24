def squares(l, r):
    for i in range(l, r + 1):
        yield(i**2)
a, b = input().split()
# a, b = int(inn[0]), int(inn[1])
f = squares(int(a), int(b))
for i in f:
    print(i, end=" ")