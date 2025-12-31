# variable/assignment statement
number = 5
x = 0

# data types
integer = 1
decimal = 4.3
string = "Hello"
boolean = True

list_1 = [integer, decimal, string, boolean]
tuple_1 = (integer, decimal, string, boolean)
dict_1 = {
    "fruit": "apple",
    "vegetable": "celery",
    "time": 5
}
set1 = {integer, decimal, string, boolean}

# expressions
5 + 3
x * 2
"Expression" + " " + " Example"
True and False

# function (no arguments)
def function1():
    print("My First Function.")

function1()

# function (w/ arguments)
def function2(age):
    print(f"I am {age} years old!")

function2(4)

# module
import moduleForMastersheet

moduleForMastersheet.favoriteFruit("pineapple")

# class and object
class class1:
    name = "Starlie"
    age = 15
    hobbies = ["art", "violin", "gaming"]

printer = class1()

print(printer.name)
print(printer.age)
print(printer.hobbies)

# Conditional Statements
rainyDay = True
cloudyDay = True
goOutside = True

if rainyDay == True:
    goOutside = False
    print("Weather too bad to go out and play.")
elif rainyDay == False and cloudyDay == True:
    goOutside = False
    print("Weather too unpredictable to go out and play.")
else:
    goOutside = True
    print("Weather is great! Go out and play!")
    
# for loop
for i in range(5):
    print(i)
    
# while loop
y = False

while y == False:
    print("Making y True.")
    y = True
    
# exception handling
try:
    print(10 / 0)
    
except ZeroDivisionError:
    print("You can't divide a number by 0!")
    
finally:
    print("cookiess mmmmm")