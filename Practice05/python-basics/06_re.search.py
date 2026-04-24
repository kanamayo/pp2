# function re.search() finds first match and return match() object if theres a match
import re
text = "hello helllo"
print(re.search("he.+o", text))