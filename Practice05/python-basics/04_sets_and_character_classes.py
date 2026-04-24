# Set is set of characters inside of the []
import re
text = "a b c d asd 214 asdfsda"
print(re.findall("[arn]"))      # [arn] is one of the specified characters 
print(re.findall("[a-n]"))      # [a-n] is match for any character between a and n 
print(re.findall("[^arn]"))     # [^arn] is match for any character EXCEPT a, r and n
print(re.findall("[0123]"))     # [0123] is one of the specified digits 
print(re.findall("[0-6]"))      # [0-9] is match for any digit between 0 and 6
print(re.findall("[0-5][0-9]")) # [0-5][0-9] is match for any two-digit between 00 and 59
print(re.findall("[a-zA-Z]"))   # [a-zA-Z] is match for any character between a and z lowercase OR uppercase
print(re.findall("[+]"))        # In sets +, *, ., |, (), $,{} has no special meaning
# [+] means return match for any character in string	



