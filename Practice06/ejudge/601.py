n = int(input())
nums = input().split()
squares = map(lambda x: int(x)**2, nums)
ans = 0
for i in squares:
    ans += i
print(ans)
