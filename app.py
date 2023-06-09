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


#Comparison Operators
# > < == !=
temp = 30
if temp > 30:
    print("it's a hot day")
else:
    print("it's not a hot day")
#PP: if name if less than 3 characters long -> must be longer than 3
#if name is more than 50 characters long -> name max is 50
#else: name works
name = input("What is your name?: ")
if len(name) < 3:
    print("name must be at least 3 characters long")
elif len(name) > 50:
    print("name can be a max of 50 characters")
else:
    print("name looks good")


#Weight Converter Project



#While loops
#format:
#while condition:
#while loops can have an else statement like if statements
i=1
while i <= 5:
    print(i)
    print('*' * i)
    i += 1
print("Done ", i)

#While loop guessing game
secret_num = 9
guess_counter = 0
guess_limit = 3
while guess_counter < guess_limit:
    guess = int(input('Guess: '))
    guess_counter += 1
    if guess == secret_num:
        print("you won")
        break
else:
    print("you lost")
"""

"""
# for loops:
# syntax ---
# for item in Collection'
# used to iterate over a collection
for item in 'Python':
    print(item)

# [] -> list of anything really
for item in ['Mosh', 'John', 'Sarah']:
    print(item)

# range function - built in function
for item in range(10):
    print(item)  # prints 0-9 excluding 10
# range creates an object, not a list that can be interated over
for item in range(5, 10):
    print(item)  # prints 5-9
# you can do steps in range
for item in range(5, 10, 2):  # means print every odd #
    print(item)  # print 5,7,9
# pp: using for loop, calculate all the prices in the list
prices = [10, 20, 30]
total = 0
for price in prices:
    total += price
print(f"Total: {total}")
# got this question wrong but that's okie
# where i went wrong: didn't initalize total variable first
# can't convert list into int which is what i initiall did like this:
#prices += prices



# Nest loops
# great for going over coordinates which is the example below
for x in range(4):
    for y in range(3):
        print(f'({x}, {y})')

# PP challenge:
# using nested loops construct this shape:
# XXXXX
# XX
# XXXXX
# XX
# XX
#hint: numbers = [5,2,5,2,2]
numbers = [5, 2, 5, 2, 2, ]
# intial thoughts
# have first loop to go through list
# check to see if it's 5 or 2
# have second loop to go print the x's
# couldn't figure out how to right it so here is the solution
for x_count in numbers:
    output = ''
    for count in range(x_count):
        output += 'x'
    print(output)


# Lists
# you can make list for pretty much every time
names = ['john', 'mosh', 'akela', 'chris', 'sarah']
print(names)  # 'john', 'mosh', 'akela', 'chris', 'sarah'] is printed
print(names[3])  # chris
print(names[-1])  # sarah
# exactly the same as accessing indexes of a string
print(names[2:])  # ['akela', 'chris', 'sarah']
print(names[2:4])  # ['akela', 'chris']
# all the examples with the : don't modify the list, it just prints a new one
names[0] = 'Jon'
print(names)
# pp: write a program to find the largest num in a list
numbers = [1, 9, 8, 10, 4, 5, 7, 3, 11]
max = numbers[0]
for next in numbers:
    if next > max:
        max = next
print(max)
# i over complicated this with a double for loop no need for that just yet


# 2D lists
#how to print this matrix
#    1,2,3
#    4,5,6
#    7,8,9
#
# with a list w/in another list or 2d list:
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
# how to access
print(matrix[0][0])  # 1
print(matrix[0][2])  # 3
matrix[0][1] = 20
print(matrix)  # [[1, 20, 3], [4, 5, 6], [7, 8, 9]]
for row in matrix:
    for item in row:
        print(item)



# List methods
numbers = [5, 2, 1, 7, 4]
numbers.append(20)  # adds 20 to the end of the list
print(numbers)
# insert takes the index of where you want to insert an instance,
# and then you put what it is you want to add to the list
numbers.insert(0, 10)
print(numbers)  # [10, 5, 2, 1, 7, 4, 20]
numbers.remove(5)  # removes item from list not by index
print(numbers)  # [10, 2, 1, 7, 4, 20]
# numbers.clear()  # empties list
# print(numbers) #[]
numbers.pop()  # removes the last item in list
print(numbers)  # [10, 2, 1, 7, 4]
# prints the index of the first occurrance of the item -- 3
print(numbers.index(7))
# print(numbers.index(50)) #error
# False -- another way of checking the existance of an item in a list
print(50 in numbers)
print(numbers.count(2))  # 1 -- counts how many instances of item
# None -- object in object that represent the absence of a value
print(numbers.sort())
# if we want to sort we have to do it in 2 steps:
# numbers.sort()
# print(numbers) #[1, 2, 4, 7, 10] in ascending order
numbers.reverse()  # sorts in descending order
print(numbers)  # [10, 7, 4, 2, 1]
# will copy all the items on the list but if there are adjustments to original list, it won't impact the second list
numbers2 = numbers.copy()
numbers.append(10)
print(numbers2)  # [10, 7, 4, 2, 1]
print(numbers)  # [10, 7, 4, 2, 1, 10]
# PP: write a program to remove the duplicates in a list
numList = [2, 2, 4, 6, 3, 4, 6, 1]
unique = []
for num in numList:
    if num not in unique:
        unique.append(num)
print(unique)


# Tuples
# similar to lists but can't modify them
# immutable so can't add, reduce them
numbers = (1, 2, 3)  # has () instead of []
print(numbers[0])


# Unpacking
coordinates = (1, 2, 3)
# instead of doing this:
#x = coordinates[0]
#y = coordinates[1]
#z = coordinates[2]
# we can do unpacking like this
x, y, z = coordinates
print(x)
print(y)
print(z)
#this isn't limited to tuples but works for lists too



# Dictionaries
# used to store info that comes as key value pairs
# key is on the left, value is on the right
# there should only be 1 key so can't have 2 ages
customer = {
    "name": "John Smith",
    "age": 30,
    "is_verified": True
}
print(customer["name"])
# the "name" portion has to be exact so can't write "Name" --> error
# to get around this --> use get method
print(customer.get("birthdate"))  # None
# you can supply a default value
print(customer.get("birthdate", "Jan 1 1980"))
# updating name
customer["name"] = "Jack Smith"
print(customer["name"])
# add new key
customer["birthdate"] = "Jan 1 1980"
print(customer["birthdate"])
#PP: User inputs phone number need to print out the string of it
phone = input("Phone: ")
numbers = {
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four"
}
output = ""
for ch in phone:
    output += numbers.get(ch, "missing") + " " #gets the ch, goes through the dictionary,
    # #if missing will add "missing" as the default but won't affect the dictionary itself
print(output)
print(numbers)
#Emoji Converter using dictionaries
message = input(">")
words = message.split(" ") #how split method works is that it'll create a boundary for based on whatever we have it split based on
#for this instance it'll split the string based on the spaces
#lets say we have something like: good_morning___ where each _ = space then it'll return: ['good', 'morning', '', '', '']
emojis = { #to get emojis on windows it's windows key + .
    ":)": "😊",
    ":(": "😒"
}
output = ''
for word in words:
    output += emojis.get(word, word) + " " #this means we're only translating the emojis,
    # if it's an actual word then it's just be set as the default and ignored
print(output)




#Functions
#definition: a container for a few lines of code that performs a specific tasks
def greet_user():
    print("Hi there!")
    print("Welcome aboard")


print("Start")
greet_user()
print("Finish")



#Parameters
#used in functions as place holders for receiving information
def greet_user1(first_name, last_name):
    print(f'Hi {first_name} {last_name}')
    print("welcome to python")

print("Start")
greet_user1("Mary", "Smith")
greet_user1("John", "Doe")
print("Finish")
#if there is a parameter you are obligated to pass a value -- if not --> error will pop up
#parameter vs argument
#parameter: holes and placeholders that is defined in function for receiving info
#arugments: actual pieces of info that we supply to these functions (look at Mary at line 511)



#Keyword Arguments
#in the previous example, John and Smith are positional arguments which means that position matters
#keyword arguments is where the position doesn't matter
greet_user1(last_name="Ho", first_name="Susan")
#don't always need to do keyword arugments but they can help improve the readability of our code
#keyword arguements should always go after positional arugments something like this
greet_user1("Chris", last_name="Mirandilla")



#Return statement
def square(number):
    print(number*number)
#returns a value but doesn't print until we call print

print(square(3))
#we get 9 and None
#why none: by default all functions return the value None
#none is an object that represents the absence of a value
#after the square function is executed, the value none is returned and passed as an arugment to the print function
#hence why we see it print function on the second line



#Creating a reuseable function using the emoji converter that we made earlier
def emoji_converter(message):
    words = message.split(" ")
    emojis = { #to get emojis on windows it's windows key + .
        ":)": "😊",
        ":(": "😒"
    }
    output = ''
    for word in words:
        output += emojis.get(word, word) + " "
    return output


message = input(">>>")
print(emoji_converter(message))




#Exceptions
#exit code 0 means that code ran smoothly without errors
#we need to anticipate errors without making the whole program crash
#we use - try except - blocks to handle errors
try:
    age = int(input("Age: "))
    income = 2000
    risk = income/age
    print(age)
except ZeroDivisionError:
    print("age can't be 0")
except ValueError: #if you encounter error type ValueError
    print("invalid value")



#Comments: lol i've been using this so much so i'm good but let's see if there's any more info
#tip for writing: write the why's and how's not the what



#Classes:
#Basic Types: Numbers, Strings, Booleans
#More complex ones: Lists, Dictionaries
class Point:
    def move(self):
        print('move')

    def draw(self):
        print('draw') #

#an object is an instance of a class
#class defines or is blueprint/template for creating objects
#to create an object we do something like this:

point1 = Point()
point1.draw()
#objects can also have attributes -- attributes are like variables that belong to a particular object
point1.x = 10
point1.y = 20
print(point1.x)
point1.draw()

point2 = Point()
point2.x = 1
print(point2.x)
#recap: classes are used to define new types, these types can have methods in the body of the class
#attributes can be set anywhere in the program




#Constructors:
#a function that gets called at the time of creating an object in order to create an object
#self is a reference to the current object
class Point:
    def __init__(self,x,y):  #init is short for initialize
        self.x = x
        self.y = y
    def move(self):
        print('move')

    def draw(self):
        print('draw')

point = Point(10,20) #when this is read the10 will be the x, and the 20 will be the y
point.x = 11
print(point.x)
#PP: Create new type called person which should have name attribute as well as talk method
class Person:
    def __init__(self, name):
        self.name = name #setting the name attribtue of the current object to the fname argument passed to this method
    def talk(self):
        print(f'Hi there my name is, {self.name}')


person1 = Person('Mary')
print(person1.name)
person1.talk()
person2 = Person("Bob")
person2.talk()



#Inheritance:
#mechanism for reusing code with parentClass having most of the main key functions and
#the children classes have unique functions for their needs
class Mammal:
    def walk(self):
        print("walk")


class Dog(Mammal): #now dog will inherit all the functions of the mammal class
    pass #python doesn't like an empty class so we use "pass" to not worry about it
    def bark(self):
        print("bark")
class Cat:
    pass
    def be_annoying(self):
        print("annoying")

dog1 = Dog()
dog1.walk()
dog1.bark()

cat1 = Cat()
cat1.be_annoying()




#Modules:
#file with some python code
#used to roganize ocde into files
#like sections in a supermarket
#not all code is going to be in the app.py folder
#you can import modules into any file that needs functions from another module
#modules should contain all related functions and classes
#2 ways to import modules
#whole file
import converters
print(converters.kg_to_lbs(60))

#import specific functions from that module
from converters import kg_to_lbs
print(kg_to_lbs(45)) #we don't have to prefix the function w/ the name of the object

#PP make a function called find_max should take a list and will return largest number in that list
#put the function into a module calling it utils, importing it and then using it
from utils import find_max
numbers = [1, 9, 8, 10, 4, 5, 7, 3, 11]
max = find_max(numbers)
#max is actually a built in function in python so we can just do this
#print(max(numbers))
print(max)



#Package:another way to organize code, to store multiple modules
#in order to make a folder into a package we need to add a special file to it called __init__.py
#or in pycharm you can just do a python folder instead of a regular folder then adding the spec. file
#now we made a another folder which has a calc shipping module in it and want to import it to here
#import the entire file simply
import ecommerce.shipping
ecommerce.shipping.calc_shipping()
#how to import a specific function in module
from ecommerce.shipping import calc_shipping
calc_shipping()
#how to import entire module
from ecommerce import shipping
shipping.calc_shipping()



#Generating Random Values
#Random values is a built in modules in python
#we can see more nuilt in modules at this link : https://docs.python.org/3/py-modindex.html
#random number module is built in
import random
for i in range(3):
    print(random.random()) #random generates a random number between 0-1
    print(random.randint(10,20)) #generates ints between 10,20
members = ['John', 'Mary', 'Bob', 'Mosh']
print(random.choice(members))
"""
#PP Roll a dice program, every time we run it, it'll be different values
#(3,1), etc
#Class Dice with a roll() to return a tuple which is fixed and can't be adjusted
#method vs function: method belongs to a class/object -- funct are independent
import random


class Dice:
    def roll(self):
        firstNum = random.randint(1,6)
        secNum = random.randint(1,6)
        return firstNum, secNum


dice = Dice()
print(dice.roll())



#Working with Directories
from pathlib import Path #common directory built into py
#absolute path
#c:\Program Files\Microsoft
#relative path
path = Path("ecommerce")
print(path.exists())
path = Path("ecommerce1")
print(path.exists())
#make a new directory
path = Path("emails")
#print(path.mkdir())
#remove a directory
path = Path("emails")
#print(path.rmdir()) #make a new directory
#how to find files
path = Path()
for file in path.glob('*.py'):
    print(file)



#Pypi & Pip
#there are a lot of built-in directories in python but not complete there we use other ones:
#Pypi: we can find thousands of packages that others have built and published for us to use
#lets try using one of these pypi packages called openpyxl
#need to install this via terminal




