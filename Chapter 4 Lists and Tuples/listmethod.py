friend = ["Apple", "Orange",5,356.45,False,"Bimal","Satvik"]
print(friend)
friend.append("Virat")
print(friend)

# sorting the integer value in ascending order
list1 = [1,45,5,67,6,7,90,1]
list1.sort() # it sorts the number in ascending order
list1.reverse() #it reverse the number 
list1.insert(3,32) #it inserts the list in the index wherer 3 is the index where to sort the object and 32 is the object
list1.pop(2) # it delete the value of 2 index
list1.remove(1)
# it prints the value of list  except index 2 
print(list1.pop(3)) # its print the value of 3 index it doesn't print any list
print(list1)