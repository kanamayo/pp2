# Special sequence is a \ with one of the next characters
# we put 'r' in the beginning to make sure that string is being treated as a "Raw String"
import re
text = "The weather is rainy rain"
re.search("\AThe")  # \A characters are at the beginning
re.search("\bThe")  # \b characters are at the beginning or the end of the word
re.search("\Bain")  # \B characters are present but NOT at the beginning or end
re.search("\d")     # \d is contains digits
re.search("\D")     # \D is DOES NOT contains digits
re.search("\s")     # \s is contains white space character
re.search("\S")     # \S is DOES NOT contains white space character
re.search("\w")     # \w is contains any word characters (from a to Z, 0-9 and '_')
re.search("\w")     # \w is DOES NOT contains any word characters
re.search("rain\Z") # \Z characters are at the end