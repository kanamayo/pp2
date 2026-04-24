n = int(input())
a = list(map(int, input().split()))
ans = sorted(set(a))
for i in ans: print(i, end=" ")