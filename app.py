"""
#first print
print('I am Akela')

#how python code is interperated
print('o----')
print(' ||||')

#intro to strings
print('*' * 10)

#updating variable
price = 10
price = 20

#Types of variables
price = 10
rating = 4.9
name = 'Akela'
is_published = True
#PP:We check in a patient named John Smith --> 20 years old and new patient
#create 3 different variables to store name, age, and whether or not he's a new patient
patientName = 'John Smith'
patientAge = 20
currentPatient = False
#Solution 3/3 correctweq



#Receiving Input
name = input('What is your name? ')
print('Hi ' + name)
#PP: ask for person's name and favorite color then print message like "Mosh likes blue"
name = input('What is your name? ')
color = input('What is your favorite color? ')
print(name + ' likes ' + color)
#Solution 2/2 correct



#Type Conversion
birth_year = input("Birth year: ")
age = 2019 - birth_year
print(age)

#this resulted in error which states: TypeError: unsupported operand type(s) for -: 'int' and 'str'
#this error is caused bc the year is taken as a literal string '2000'
#you can't substract a string from an int therefore... need to do this
birth_year = input("Birth year: ")
age = 2023 - int(birth_year)
print(age)
print(type(birth_year))
print(type(age))

#PP: Ask user their weight (in pounds), convert it to kilograms and print
pound_weight = input("What is your weight in pounds? ")
kilo_weight = int(pound_weight) * 0.45
print("Your weight in kilograms is: " + str(kilo_weight))


#Strings
#if want to use ' in the middle of the string, wrap everything in "
course = "Python's Course for Beginners"
print(course)
#if want to use " in the middle of the string, wrap everything in '
course = 'Python Course for "Beginners"'
print(course)
#if want to def multiple lines of string '''   '''
course = '''
Hi John, 
Here is my first email to you

Thank you,
Support Team
'''
print(course)
#want to get specific character in string --> use []
course = 'Python for Beginners'
print(course[0]) #P
#you can use negative indexes, which will get from the back
print(course[-1]) #s
print(course[-2]) #r
#you can get a range of characters too like this --> will get character at index 0 all the way to 3 but will exclude 3
print(course[0:3]) #Pyt
print(course[1: ]) #ython for Beginners --> print everything starting from index 1
print(course[:5]) #Pytho --> interp will assume starting is at 0
print(course[:]) #Python for Beginners --> copying string because assuming 0 for begin. and last index for ending
#PP if we have:
name = 'Jennifer'
print(name[1:-1])
#What will it print --> don't use terminal but use your knowledge first
#my guess: enniferr?
#Solution: ennife
#why was I wrong? bc after the : that number is excluded therefore since r = -1 index that will be excluded


#Formatted Strings
#useful to dynamically generate some text w/ variables
first = 'John'
last = 'Smith' # now we want to get John [Smith] is a coder --> how do we do that?
message = first + ' [' + last + '] is a coder' #John [Smith] is a coder
print(message)
# we can do this but it's not ideal when the text is longer
msg = f'{first} [{last}] is a coder'
print("Better one: " + msg) #Better one: John [Smith] is a coder


#String Methods
course = 'Python for Beginners'
print(len(course)) #20
print(course.upper()) #PYTHON FOR BEGINNERS
print(course.lower()) #python for beginners
print(course) #Python for Beginners

print(course.find('P')) #will return the index of the first P -->  0
print(course.find('o')) #4
#find is case sensitive
print(course.find('O')) #-1
print(course.find('Beginners')) #11 --> bc Beginners starts at index 11

print(course.replace('Beginners', 'Absolute Beginners')) #Python for Absolute Beginners
print(course.replace('n','J')) #PythoJ for BegiJJers --> replaces all instances of n with J's

print('Python' in course) #True bool statement
print('python' in course) #False bool statement
#in vs find
#in returns boolean
#find returns index of char/bit of string


#Arithmetic Operations
#same as math + - * and / but another division operator for intergers //
#% returns remainder
#** exponent
print(10+3) #13
print(10-3) #7
print(10*3) #30
print(10/3) #3.333333333333335
print(10//3) #3
print(10%3) #1
print(10**3) #1000

x = 10
x = x+3 #13
print(x) #13
#but we can write this shorter w/ augmented assignment
x+=3
print(x) #16


#Operator Precendence
x = 10+3*2
print(x) #16
#order (L to R) : exponent - multi/division - add/sub
x = 10 + 3 * 2 **2
#guess before running: 22
print(x) #22
#parenthesis changes priority (just like in math)
#PP:
x = (2+3)*10-3
#guess before running: 47
print(x) #47
"""


#Math Functions
#round
x = 2.9
print(round(x)) #3
#absolute -- always shows the positive value even if value is negative
print(abs(-2.9)) #2.9
#python has a handful of built in math functions but for more complex ones we need to import the math module
#module -- separate file w/ some reusebal code to organize our code into different files
import math #we would usually write this on top of the document
print(math.ceil(2.9)) #3 -- ceil takes the ceiling number
print(math.floor(2.9)) #2


#if statements
is_hot = True
if is_hot:
    print("it's a hot day")
print("Enjoy your day") #it's a hot day & Enjoy your day

is_hot = False
if is_hot:
    print("it's a hot day")
print("Enjoy your day") #Enjoy your day

is_hot = False
if is_hot:
    print("it's a hot day")
else:
    print("it's a cold day")
print("Enjoy your day") #it's a cold day & Enjoy your day

is_hot = False
is_cold = False
if is_hot:
    print("it's a hot day")
elif is_cold:
    print("it's a cold day")
else:
    print("it's a lovely day")
print("Enjoy your day") #it's a lovely day & Enjoy your day
#PP: price of a house is 1m - if buyer has good credit downpayment 10% - otherwise put down 20% _ print down statement
price = 1000000
good_credit = True
if good_credit:
    payment = price * 0.1
else:
    payment = price * 0.2
print(f'Down payment: ${payment}') #Down payment: $100000.0


#Logical Operators
#and: just use word and
#or: just use word or
#not: just use word not (java is the !equivalent)
