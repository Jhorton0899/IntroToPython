#this is going to be going over creating our own functions, we can think of it as a variable 
#that holds a block of code. ill start off simple and work my way up.

def add(a, b): #we use two variables that serve as placeholders until 
  return a + b #here we add our two variables easy enough\the return here can be thought of as 
               # return the sum of a + b
print(add(4, 4))# we replaced the two placeholders a and b with the numbers we actually want to add
#result should be 8

#we can do this with many arithmetic operations
def multiply(num1, num2): #this is for multiplication
    product = num1 * num2 #note the use of a variable here (product) useful when dealing with many arguments
    return product
result = multiply(4, 7)
print(result)

def subtract(num1, num2):
  total = num1 - num2
  return total
print(subtract(5,1))

def divide(num1, num2):
  total = int(num1 / num2)
  return total
print(divide(10,2)) #remember division always returns a float unless we go through type conversion

#our function currently only accepts two arguments to accept more we can do it in two ways:
def add_numbers(a,b,c): #we add an additional variable so it now accepts three arguments
  return a + b + c
print(add_numbers(2,2,2))

#or a more efficient way would be using the * operator 
def add_numbers1(*args): #the star allows us to accept numerous arguments
    total = 0 #we need to add an initial number for when we run our for loops.
    for num in args:
        total += num #total + every number in our arguments 
    return total 
addition = add_numbers1(4, 4, 4) 
print(addition)

#heres an example using  subtraction 
def subtract_number(*args):
  total = 0 
  for num in args:
    total -= num 
    return total
subtract = subtract_number(5, 5)
print(subtract)
#------------------------------------------------------------------------------------------------------------------
#now it becomes a bit more complicated or in depth previously our functions only accepted integers
#now we'll work with other data types starting with strings 
def greet(): #notice the () is empty because it doesnt accept an argument since its goal is to get info
    name = input("What is your name? ")
    return "Hello, {}".format(name) 
greeting = greet()
print(greeting)

#lets do one for lists
def repeat(list):
  for i in list:
    print("{} is in our list".format(i))
x = list(range(6))#through type conversion we make a list then using the range function list all numbers from 0 to 5
print(x)
repeat(x)

def multiply_by_2(list):
    return [item * 2 for item in list]
y = list(range(8))
print(multiply_by_2(y))


y = [1,2,3,10]
def find_max(a_list):
  maximum = max(a_list)
  return maximum
print(find_max(y))

def find_min(a_list):
  minimum = min(a_list)
  return minimum
print(find_min(y))





occupiedseats = list(range(31))
print(occupiedseats)
SeatQuery = input("Please enter a number to check availability\n")
SeatQuery = int(SeatQuery)#we have to do type conversion here because the original input will be returned as a string
if SeatQuery in occupiedseats:
    print("that seat is already taken")
else:
    print("that seat is available")
    
seats_available = list(range(1,31))
print(seats_available)
SeatQuery = input("Please enter a number between 0 and {} to secure your seat \n".format(len(seats_available)))
SeatQuery = int(SeatQuery)

if SeatQuery in seats_available:
    seats_available.remove(SeatQuery)
    print("Your seat has been successfully reserved thank you")
    
else:
    print("Invalid seat number or seat is already occupied.")
    
#wasnt mentioned earlier but the more you keep going you'll see these 
def divide(a, b):
    if b == 0:
        raise ValueError("Division by zero is not allowed.")
    return a / b
"""
def add(a, b):
    total = a + b
    return total

when we use return it stores the result as a variable ? 
if you want to see the result of this you'll need to use print 
input: print (add(8,7))
output: 15 
the return allows you to use the return output again in your next function

compared to if I were to try 
def add(a, b):
    total = a + b
    print(total)

compared to if I were to try to use the print output it will simply print
the result and not keep a memory of it for later
"""

"""instead of doing the for loop we can use map() instead
x = [1, 2, 3, 4, 5]
def AddBy2(x):
  return x + 2

So the way map works is it takes a function first and the arguments
x = map(AddBy2, x) 

We then have to convert our argument(x) to a list 
x = list(x)

print(x)
[3, 4, 5, 6, 7]

so this x = map(AddBy2, x) is the equivalent to 
for i in x:
  print(i + 2)

with the exception of returning it in a list format
"""

x = [1, 2, 3, 4, 5]
def AddBy2(x):
  return x + 2

x = map(AddBy2, x)
x = list(x)
print(x)