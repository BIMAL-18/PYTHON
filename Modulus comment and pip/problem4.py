import os
# specify the director that you want to list
directory_path ='/'
# list all the files and directories in the specified path
contents =os.listdir(directory_path)
#print each file and directory name
# print(contents)
for item in contents:
    print(item)
    #we can replace the directory path by = any name and items by = any name it is declared datatype;
    # '''again we can replace the 
    # for item in contents:
    # print(item) by = print(contents)
    # '''