import re
s = input()
p = input()
t = re.escape(p)
ans = re.findall(t, s)
print(len(ans))