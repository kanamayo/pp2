n = int(input())
keys = input().split()
values = input().split()
query = input()
d = dict(zip(keys, values))
# ans = 0
# for i in r:
#     ans += int(i[0]) * int(i[1])
# print(ans)
if query not in d:
    print("Not found")
else:
    print(d[query])