file = open("text.txt", "r")
print(file.read())      # reads content of the file
print(file.readline())  # reads one line of the file
print(file.readlines())  # reads all lines of the file and returns them as a list of strings
