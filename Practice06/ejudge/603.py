n = int(input())
s = input().split()
ans = enumerate(s)
for i, value in ans:
    print(f"{i}:{value}", end=" ")
# print(ans)