import re
s = input()
if re.search("cat|dog", s):
    print("Yes")
else:
    print("No")