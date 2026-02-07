n = int(input())
nums = input()
nums = list(map(int, nums.split()))
for i in range(0, n):
    t = nums[0:i + 1]
    if t.count(nums[i]) == 1:
        print("YES")
    else:
        print("NO")
        