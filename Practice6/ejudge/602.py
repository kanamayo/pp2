n = int(input())
nums = input().split()

r = list(filter(lambda x: int(x) % 2 == 0, nums))
print(len(r))
