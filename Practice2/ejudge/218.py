n = int(input())
s = [input() for i in range(0, n)]
d = {}
for i in s:
    d[i] = s.find(i)
for i in sorted(d):
    print(f"{i} {d[i]}")