# Theres plenty of special Metacharacters that help us to find specific things 
import re

text = "11234 1asdf asdfd hello heioo world helo heo hellllllloooo hellllo white red"
re.findall("[a-z]", text) # [] is Set of Characters
re.findall("\d", text)           # \ indicates special sequence Set of Characters
re.findall("he..o", text)        # . is any character
re.findall("^hello", text)       # ^ is starts with
re.findall("world$", text)       # $ is ends with
re.findall("he.*o", text)        # * is Zero or More occurrences
re.findall("he.+o", text)        # * is One or More occurrences
re.findall("he.?o", text)        # ? is Zero or One occurrences
re.findall("he.{4}o", text)      # {N} is exactly N number of occurrences
re.findall("white|black", text)  # | is either/or
re.findall("(\d+) (.{4})", text) # () is for capturing and grouping
