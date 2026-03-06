import re
s = input()
ans = re.findall("[0-9][0-9]/[0-9][0-9]/[0-9][0-9][0-9][0-9]", s)
print(len(ans))