age = 24
# Following does not work:
# print("My age is " + age + " years")

# Fix #1: through str() method -> converts something to a string
print("My age is " + str(age) + " years")

# Fix #2: replacement fields
print("My age is {0} years and I have {1} years to go to 100!".format(age, 100 - age))

print("""January: {2}
February: {0}
March: {2}
April: {1}
May: {2}
June: {1}
July: {2}
August: {2}
September {1}
October: {2}
November: {1}
December: {2}""".format(28, 30, 31))

# Fix #3: DEPRECATED FROM PYTHON3
print("My age is %d years " % age)
print("My age is %d %s, %d %s" % (age, "years", 6, "months"))

for i in range(1, 12):
    print("No. %2d squared is %4d and cubed is %4d" %(i, i ** 2, i ** 3))

print("PI is approximately %12.50f" % (22 / 7))

#Back to replacement fields {data:min_width} < -> left formatted (left justified)
for i in range(1, 12):
    print("No. {0:2} squared is {1:<4} and cubed is {2:<4}".format(i, i ** 2, i ** 3))

#Add precision to replacement fields
print("PI is approximately {0:12.50}".format(22 / 7))

#Use of numbers in replacement fields is optional
for i in range(1, 12):
    print("No. {:2} squared is {:4} and cubed is {:4}".format(i, i ** 2, i ** 3))