# python's allocating memory for the variable greeting, and storing string "Bruce" into it
# variables can start with _ or alpha chars, then use any mixture of them and numbers
# variable names are case sensitive
greeting = "Bruce"
_name = "Tim"
age = 24

# error: cannot convert age from int to string explicitly
# print(_name + ' is ' + age + ' years old')

# Integer
a = 12
b = 3

# Float (32 precision digits)
c = 3.5

print(a + b)
print(a - b)
print(a * b)
# / operator returns division as a float number
print(a / b)
# // operator returns division as an integer number
print(a // b)
print(a % b)

# order of operations! (operator precedence)
print(a + b / 3 - 4 * 12)
print(8 / 2 * 3)
print(8 * 3 / 2)

# String data type (sequence type - sequence of chars)
parrot = "Norwegian Blue"
print(parrot)
# Printing 3'rd character of string (Python is 0-based)
print(parrot[3])
# Can access negative indices (start from end)
print(parrot[-1])
# Can print a range of chars
print(parrot[0:6])
print(parrot[:6])
print(parrot[6:])
print(parrot[-4:-2])
# Can print specific chars too - 3rd number specifies the "jump size" between chars
print(parrot[0:6:2])
print(parrot[0:6:3])

# Can extract specific characters too
number = "9,223,372,036,854,775,807"
print(number[1::4])

numbers = "1, 2, 3, 4, 5, 6, 7, 8, 9"
print(numbers[0::3])

str1 = "he's "
str2 = "probably "
print(str1 + str2)
# This is valid, but useless
print("he's " "probably " "pining")

# Can multiply strings
print("Hello " *5)
print("Hello " * (5 + 4))

# Substring operator
today = "Friday"
# Returns true/false whether substring is on string
print("day" in today)