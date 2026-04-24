import re
s = input()
t = re.compile("\w+")
ans = re.findall(t, s)
# print(s)
# print(t)
print(len(ans))