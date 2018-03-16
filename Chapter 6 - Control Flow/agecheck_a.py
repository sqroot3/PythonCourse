# Write a small program to ask for a name and an age
# When both values have been entered, check if the person is the right age for a 18-30 holiday
# If they are, welcome to holiday
# If not, print polite message refusing entry

name = input("Please enter your name: ")
age = int(input("Please enter your age: "))

if 18 < age < 31:
    print("Welcome to the holiday, {}!".format(name))
else:
    print("Sorry, you can't get in. Goodbye!")