# age = int(input("How old are you? "))

# Can use parenthesis too, operator precedence may cause unwanted results
# if age >=16 and age <= 65:
# if 16 <= age <= 65:
#     print("Have a good day at work.")

# if age < 16 or age > 65:
#     print("Enjoy your free time")
# else:
#     print("Have a good day at work")

# True = 1, false = 0 in Python
# Any nonzero values in a condition evaluate as true
# x = "false"
# if x:
#     print("x is true")

# x = input("Please enter some text: ")
# if x:
#     print("You entered '{}'".format(x))
# else:
#     print("You did not enter anything")
#
# print(not False)
# print(not True)

parrot = "Norwegian Blue"
letter = input("Enter a character: ")

# If char is in string, then do something
# in keyword here is case sensitive, 'b' != 'B'
if letter in parrot:
    print("Give me an {}, Bob".format(letter))
else:
    print("I don't need that letter")