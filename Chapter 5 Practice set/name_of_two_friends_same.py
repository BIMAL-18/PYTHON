# # if the name of two friends are same : what will happen to the program in problem value and keys.py


d = {}
name = input("Enter the name of the friends")
lang = input("Enter the language of the friends you know.")
d.update({name : lang})
# if we give the name of the two friends same then
# suppose i give 
# name = "Bimal"
# lang = "python"
name = input("Enter the name of the friends")
lang = input("Enter the language of the friends you know.")
d.update({name : lang})

# name = "Rohan"
# lang = "c++"
name = input("Enter the name of the friends")
lang = input("Enter the language of the friends you know.")
d.update({name : lang})

# name = "Bimal"
# lang = "js"
# Here , the value is same as in 1st and 4 so the after we give the same name then the first "python" will be updated to "js"

name = input("Enter the name of the friends")
lang = input("Enter the language of the friends you know.")
d.update({name : lang})

# name = "Bishal"
# lang = "HTML"

print(d)