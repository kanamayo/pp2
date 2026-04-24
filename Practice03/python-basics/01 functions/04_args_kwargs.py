# *args allows function to accept any number of positional arguments
# function will receive tuple of arguments
def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")

# **kwargs allows function to accept any number of keyword arguments
# function will receive dictionary of arguments

# we can combine regular parameters with *args and **kwargs
# Regular parameters must come before