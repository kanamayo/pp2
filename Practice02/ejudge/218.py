n = int(input())
s = [input() for i in range(0, n)]
d = {}
for i in s:
    d[i] = s.index(i) + 1
for i in sorted(d):
    print(f"{i} {d[i]}")