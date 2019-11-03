# userName = input("Enter the name: ")
# age = int(input("Enter your age: "))
#
# if age >= 21:
#     print(userName, "you are older than 21 years!")
#     print(userName, "You have to pay for your drinks")
# elif age >= 18:
#     print(userName, "you are older than 18 years!")
#     print(userName, "You are allowed in but NO drinks allowed")
# else:
#     print(userName, "you are younger than 18 years!")

customerName = input("Enter your name: ")
print("Give your feedback in range of 1 to 5")
rating = int(input("Please give your rating: "))

if rating == 1:
    print(customerName, "Sorry to hear about your experience.")
elif rating == 2:
    print(customerName, "We are trying to get better.")
elif rating == 3:
    print(customerName, "Thanks!")
elif rating == 4:
    print(customerName, "We almost missed the perfect rating from you.")
elif rating == 5:
    print(customerName, "Happy to know you loved our service !!")
else:
    print(customerName, "NOT valid feedback")