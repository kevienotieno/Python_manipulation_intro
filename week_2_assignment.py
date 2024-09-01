# Create an empty list
mylist = []

# add values to the list through the append method
mylist.append(10)
mylist.append(20)
mylist.append(30)
mylist.append(40)

# add 15 to the second position in the list
mylist.insert(1, 15)

# create another list
otherlist = [50, 60, 70]

# use the list to extend the mylist
mylist.extend(otherlist)

# remove the last element of my list
mylist.remove(mylist[-1])

# sorting mylist
sorted(mylist)

print(mylist.index(30))
