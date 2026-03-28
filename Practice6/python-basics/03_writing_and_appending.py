# to write to a file, we use next parameters in open() function
# "a" - append - append to the end of file
with open("demofile.txt", "a") as f: 
    f.write("Hello!")

# "w" - write - will overwirte everything
with open("demofile.txt", "a") as f: 
    f.write("Hello!")
