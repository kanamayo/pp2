# split() function returns a list where string was split at each match
import re

txt = "The rain in Spain"
x = re.split("\s", txt)
print(x)