n = int(input())
a = input().split()
b = input().split()
r = zip(a, b)
ans = 0
for i in r:
    ans += int(i[0]) * int(i[1])
print(ans)
