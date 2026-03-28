import os

os.mkdir("folder")                              # create single directory
os.makedirs("level1/level2", exist_ok=True)     # create directories
print(f"Content: {os.listdir('.')}")    # list all files/folders in current path
os.chdir("folder")                      # change current directory
print(f"Current: {os.getcwd()}")        # display current workingh directory
os.rmdir("empty_folder")                # remove an EMPTY directory