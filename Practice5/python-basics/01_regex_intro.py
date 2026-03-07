# RegEx is Regular Expressions, sequence of characters that forms search patterns
# They can be used to check if string contains specific pattern

import re # RegEx library/module

text = "Hello, Alisher"
name = re.findall("^Hello\, .+", text)
print(name)