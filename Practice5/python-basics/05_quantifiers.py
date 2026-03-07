# quantifiers
import re
text = "helo hello helllo hellllo helllllo hegjfhgkhljo"
print(re.findall(r"he.{1}o", text)) # {n} is exactly n times occurrences
print(re.findall(r"he.{3,}o", text)) # {n, } is at least n times occurrences
print(re.findall(r"he.{3,4}o", text)) # {n, m} is from n to m times occurrences
