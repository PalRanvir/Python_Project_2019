# list_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# userInput = int(input("Enter a number: "))
#
# for i in list_numbers:
#     if i == userInput:
#         print("Matching number found", i)
#         break
# else:
#     print("No match found...")



# for i in "HelloWorld":
#     if i == "W":
#         break
#     print(i)
# print("you are out of the loop as iteration encountered W")


# for i in "HelloWorld":
#     if i == "o":
#         continue
#     print(i)
#
# print("you can't see O in output as there is continue keyword")

# for i in "HelloWorld":
#     if i == "o":
#         pass
#     print(i)
#
# print("what happens when pass keyword is the only statement in the block ")


for i in "HelloWorld":
    if i == "o":
        pass
        print("I will do this later")
    print(i)

print("what happens when pass keyword & other statements are in the block ")