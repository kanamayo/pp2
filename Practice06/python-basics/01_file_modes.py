# we open files with open() function
# files can be opened in multiple modes
# we always need to close files: due to buffering, changes may not apply until tthe file is closed
file1 = open("text.txt", "r") # r - read, by default
file2 = open("text.txt", "a") # a - append
file3 = open("text.txt", "w") # w - write
file4 = open("text.txt", "x ") # x - creates file

# additionally, filetype can be specified
file5 = open("text.txt", "rt") # t - text, by default
file6 = open("text.txt", "rb") # b - binary