def f(k):
    for i in range(k, -1, -1):
        yield i
t = int(input())
o = f(t)
for i in o:
    print(i)