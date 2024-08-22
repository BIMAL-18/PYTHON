# create an empty dictionary .Allow 4 friends  to enter their favourite language as value and use key as their name
# Assume that their name are unique.

d={}
name = input("Enter the name of the friends :  ")
lang = input("Enter the language of the friends you know :  ")
d.update({name : lang})

name = input("Enter the name of the friends :  ")
lang = input("Enter the language of the friends you know :  ")
d.update({name : lang})

name = input("Enter the name of the friends :  ")
lang = input("Enter the language of the friends you know :  ")
d.update({name : lang})

name = input("Enter the name of the friends :  ")
lang = input("Enter the language of the friends you know :  ")
d.update({name : lang})

print(d)
