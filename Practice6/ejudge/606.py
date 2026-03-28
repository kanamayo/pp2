n = int(input())
a = list(map(int, input().split()))
# func = lambda x: x >= 0;
ans = all(i >= 0 for i in a)
if ans:
    print("Yes")
else:
    print("No")
# print(ans)