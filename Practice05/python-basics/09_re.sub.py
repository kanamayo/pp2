# sub() function replaces matches with text of choice
import re

txt = "The rain in Spain"
x = re.sub("\s", "9", txt)
print(x)