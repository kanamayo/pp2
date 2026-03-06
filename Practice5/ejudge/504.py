import re
s = input()
# k = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# i = 0
# a = []
ans = re.findall("\d", s)
# for x in k:
    # print(re.split(x, s))
    # if len(re.split(x, s)) > 1:
        # ans += ' '
        # ans += x
    # i += 1
# print(a)
for i in ans:
    print(i, end=" ")