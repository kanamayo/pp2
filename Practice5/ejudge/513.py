import re
s = input()
ans = re.findall("\w+", s)
print(len(ans))