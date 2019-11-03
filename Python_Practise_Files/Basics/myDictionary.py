# # Dictionary- formed with keys and values, {}, comma-separated, we can define whatever keys(indices) we want to
#
# myDictOne ={
#     "playerOne": "Virat",
#     "playerTwo": "Rohit",
#     "playerThree": "MS"
# }
#
# print(myDictOne)
# print(myDictOne["playerTwo"])
#
#
# print(myDictOne.keys())       # Prints all the keys of Tuple as a List ,
#                               # dict_keys(['playerOne', 'playerTwo', 'playerThree'])
#
#
# print(myDictOne.values())     # Prints all the values of Tuple as a List ,
#                             # dict_values(['Virat', 'Rohit', 'MS'])


scores = {
    "Rohit": 109,
    "Shikhar":  88,
    "Virat": 110,
    "Shreyash": 81
}

print(scores)

# for score in scores:
#     print(score)                 # this will print only the keys not the values ,
#                                  # that is for loop will iterate through the keys
# for score in scores:
#     print(score, "score in the match is", scores[score])

####Replacing a value in  key-value pair
replaceKey = input("Enter the key to be replaced: ")
replaceValue = input("Enter the value to be replaced: ")

scores[replaceKey] = replaceValue
print(scores)


##### Adding a new key-value pair
newKey = input("Enter the key to be added: ")
newValue = input("Enter the value to be added: ")

scores[newKey] = newValue
print(scores)

##### Removing a key-value pair
remKey = input("Enter the key to be removed: ")

del scores[remKey]
print(scores)
