# we can use with statement to open a file
# we do not have to worry about closing files, the statement takes care of that
with open("demofile.txt") as f:
    print(f.read())
