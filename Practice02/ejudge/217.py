n = int(input())
s = [input() for i in range(0, n)]
ans = 0
d = {}
for i in s:
    d[i] = s.count(i)
for i in d:
    if d[i] == 3:
        ans += 1
print(ans)