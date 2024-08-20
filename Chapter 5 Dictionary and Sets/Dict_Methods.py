d = {}# empty dictionary
marks ={
    "Bimal" : 86,
    "Rohan" : 97,
    "Bishal" : 27,
    0 : "Aayush"

}
print(marks.items()) # it prints the value of items in the marks it gives all the value
print(marks.keys()) # it give the marks of the keys
#it print the value of the left hand side i.e. Bimal Rohan Bishal , 0
print(marks.values()) # it print the right hand side of the given keys i.e it print the marks 86,34
marks.update({"Bimal":94,"Binod":22}) 
# it change the value of the 86 of Bimal to the 94 of the bimal it means it update the value of the person
#if it doesnt contains Binod in the dict then it add binod instead of showing error
print(marks)
print(marks.get("Bimal"))
# it give the marks of the bimal i.e 86 if we given the unknown name which is not given in the given list  then it gives  the output :: none
print(marks.get("Bimal2"))# Returns NONE
# if we write 
# print(marks["Bimal2"]) Returns Error 
