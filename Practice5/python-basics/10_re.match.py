# re.match() checks for match only at the start of string
# If the match, it returns a match object; otherwise it returns None
import re

result = re.match(r"\d+", "123abc")
print(result.group())  # Output: 123