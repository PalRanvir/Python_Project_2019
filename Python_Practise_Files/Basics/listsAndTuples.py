# # Lists - Mutable, comma-separated , [], numeric, strings
#
# myListOne = [5.8, "Ranvir", 4, 5, "Ram"]
# myListTwo = [55, 66, "Pal"]
#
# print(myListOne)
# print(myListOne[4])
# print(myListOne[-1])
# print(myListOne[-5])
# print(myListOne[-4])
# print(myListTwo[0:2])   #Note the last range isNOT included
# print(myListTwo * 2)    # Just like it will concatenate
#
# x = "Ranvir"
# print(x * 2)
#
# print(myListOne + myListTwo)    # Just like it will concatenate
#
# myListOne[1] = "Sona"      # Value at the 1st position of myListOne i.e "Ranvir"
#                            # will be replaced by "Sona". Lists are mutable
#
# print(myListOne)

# names = ["Rohit", "Shikhar", "Virat", "Shreyash", "MS", "Hardik"]
# length = len(names)
# print(length)

# for index in range(0, length):
#     print(names[index], "is found at index", index)
#


# names = ["Rohit", "Shikhar", "Virat", "Shreyash", "MS", "Hardik"]
# x = names.index("MS")                          # imdex funtion gives the index of a value in the list.
#
# for name in names:
#     print(name, "is found at index", names.index(name))



# Lists can be extended, changed & manipulated.
# Add a value to the list using append function & remove a value from list using remove function

names = ["Rohit", "Shikhar", "Virat", "Shreyash", "MS", "Hardik"]
print(names)

newIndex = int(input("Please enter the index to be replaced: "))
newName = input("Please enter the new name to put into the index: ")

names[newIndex] = newName
print(names)

newName = input("Please enter the name to be added/appended to the list: ")
names.append(newName)
print(names)

remName = input("Please enter the name to be removed from the list: ")
names.remove(remName)
print(names)

# Tuples - Also known as Read only Lists, IMMUTABLE, comma-separated , (), numeric, strings

# myTupleOne = (4, "Ranvir", 5.6, "Pal")
# myTupleTwo = (5, 2, "Ram")
#
# print(myTupleOne[1])                     # Any value at any position can be accessed
# print(myTupleOne[1:3])                   #Concept of Range is similar to that of Strings & Lists
#
# print(myTupleOne * 2)                    # Concatenates similar to that of Strings & Lists
# print(myTupleOne + myTupleTwo)
#
# myTupleOne[1] = "Sona"                   # Will throw error, TypeError: 'tuple' object does not support item assignment