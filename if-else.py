#flow control/conditionals can be confusing but practice helps think of it as instructions
#starting with if - else 

# we start with our variable x 
x = 3
if x == 3: #if x is equal to 3 then
  print("x is equal to 3") #print x is equal to 3
else:  #the else is a catch all statement that doesnt take an argument so if no other condition is met do this
  print("x is not equal to 3") 

#another example of this would be 
students = ["tom", "fred", "jack", "brandon"] #we start with a list of students
if "tom" in students: #the inital if statement same as earlier
  print("{} is one of the students".format(students[0])) 
elif "fred" in students: #but here we add an elif(else if) you can add as many as you need to 
  print("{} is one of the students".format(students[1]))
elif "jack" in students:
  print("{} is one of the students".format(students[2]))
elif "brandon" in students:
  print("{} is one of the students".format(students[3]))
else: #then our catch all statement if none of the conditions are met
  print("that is not one of the students".format(students))

#okay this is a bit useless without accepting any user input so lets change that
students = ["tom", "fred", "jack", "brandon"]
#we can also use the if any( ** in ** for ** in **):
question = input("please enter a name to check if they are a student: \n")
if question.lower() == "tom": # using .lower() to make the input case-insensitive
    print("{} is one of the students".format(students[0]))
elif question.lower() == "fred":
    print("{} is one of the students".format(students[1]))
elif question.lower() == "jack":
    print("{} is one of the students".format(students[2]))
elif question.lower() == "brandon":
    print("{} is one of the students".format(students[3]))
else:
    print("That is not one of the students") 
    
#we can also use nested if - else conditions for example 
x = 3
y = 3
#it looks a bit confusing at first but the indentation helps to clarify things
if x == 3: #the outer condition 
  if y == 2: #the inner condition only happens if the outer condition is met
    print(x + 2)
else: 
  print(x - 2)

#now we can get a bit more in depth with how we establish flow control
students = ["tom", "fred", "jack", "brandon"]
if len(students) == 4 and "tom" in students: #the len counts the number of items in our list(not the sum) and the and condition means both conditions must be met
  print("we have four students in our class")
  for i in students:
    print(i)
else:
  print("no students")
#the code above uses the and condition means both conditions must be met this uses or meaning only one must be met
if len(students) ==3 or "fred" in students: 
  print("we have four students in our class")
  for i in students:
    print(i)
else:
  print("no students")

# lets explore the break command, it stops our script 
for i in range(11):
    if i == 3:
        print("Found 3!") 
        break #the list iterates over the list counting all numbers but when it gets to 3 it stops
else:
    print("3 not found.")
#this is the inverse of the same command
for i in range(6):
  if i == 7:
      print("7 found.")
      break
else:
    print("7 is not in this list")
    
#----------------------------------------------------------------------------------------------------------
seats_available = list(range(1,31))
print(seats_available)
SeatQuery = input("Please enter a number between 0 and {} to secure your seat \n".format(len(seats_available)))
SeatQuery = int(SeatQuery)

if SeatQuery in seats_available:
    seats_available.remove(SeatQuery)
    print("Your seat has been successfully reserved thank you")
else:
    print("Invalid seat number or seat is already occupied.")
#------------------------------------------------------------------------------------------------------------
    
#one more example that details the importance of type conversion before moving on(trust me its important)
what_is_your_age = input("What is your age\n") #the users response to this will be a string even tho its a number
#if we were to try to immediately add the user input it would return a value error to avoid that we
#we convert the users response from a string to a int
what_is_your_age = int(what_is_your_age) #we do that through type casting 
your_age_in_5 = what_is_your_age + 5
print(your_age_in_5) 

"""
example:
numbers = [5, 8, 12, 6, 3]

# Using 'if any' to check if any element is greater than 10
if any(num > 10 for num in numbers):
    print("At least one number is greater than 10.")
else:
    print("No number is greater than 10.")

example:
locations = ["florida", "Georgia", "Carolina", "Tennessee"]

if any(loc == "Georgia" for loc in locations):
    print("Georgia is a valid location")
else:
    print("Georgia is not a valid location")
    
"""

