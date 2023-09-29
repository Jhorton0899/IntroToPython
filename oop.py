"""
this is the introduction to OOP if you get confused visit this link 
https://youtu.be/q2SGW2VgwAM genuinely one of the best teachers

the process is fairly straightforward think of an object for my case ill use a table we declare our 
class through a form of type casting

class Table:

then follow that by initializing the class during this process we'll be adding the characteristics 
we've come to expect from our object in our case maybe its the material the table is made of, the 
location of the table, and the amount of legs it has.

class Table:
  def __init__(self, material, location, legs):
  
we reiterate these characteristics again at the bottom 
class Table: 
` def __init__(self, material, location, legs):
  self.material = material
  self.location = location
  self.legs = legs
  
the thing that stands out the most is probably the self, its a weird concept that i dont fully 
understand myself yet but i think of it as this the table is the object we are trying to build 
the characteristics(parameters) are the blueprint for the table. so when we say self.location were 
speaking as if were in the table either way it always comes first in the parameters and you'll get 
used to it with more practice.

class Table:
  def __init__(self, location, material, legs):
    self.location = location
    self.material = material
    self.legs = legs
    
this alone is good and we can use our object as show below, sort of like using our created functions
it takes three parameters so we fill in those parameters with the appropriate values 

x = Table("kitchen", "wood", 4)
print(x.location)

we can call on those parameters later on or built into it like so

class Table:
  def __init__(self, location, material, legs):
    self.location = location
    self.material = material
    self.legs = legs
    
def full(self):
  return("the table in the {} is full".format(self.location))


x = Table("kitchen", "wood", 4)
print(full(x))

practice makes perfect but this is the general gist of OOP 
        
"""
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def drive(self):
        return "The {} is driving".format(self.make)

# Create an instance of Car
my_car = Car("Honda", "Civic", 2019)

# Access and print the 'year' attribute
print(my_car.year)

# Call the 'drive' method and print the result
print(my_car.drive())



class Laptop:
    def __init__(self, brand, memory, year):
        self.brand = brand
        self.memory = memory
        self.year = year

    def InUse(self):
        try: 
          brands = ["Windows", "Apple", "Dell", "HP", "Lenovo"]
          if self.brand in brands: 
            return "{} is a great company".format(self.brand)
          else: 
            return "invalid brand"
        except Exception as e:
          return "Error {}".format(e)
        
x = Laptop("Apple", 100, 2020)
print(x.InUse())
print(Car)
print(type(Car))

print(x.year)
         

"""
next up are subclasses we create them through the process of inheritance starting with the parent class
Home, i showed the process earlier but quick refresher 

class Home: #we create the class(object) 
  def __init__ (self, rooms, bathrooms, level): #assign the parameters associated with the object
    self.rooms = rooms
    self.bathrooms = bathrooms
    self.level = level


next up is creating a subclass of the class Home we need to nest the main class inside the subclass 
class Bedrooms(Home): 

#the first set of parameters inside the new subclass match the ones from the main class this is 
#the process of inheritance but inheritance only works one way, meaning that the main class can pass
#down its parameters but the subclass cant pass up its parameters

  def __init__ (self, rooms, bathrooms, level, beds, closet, patio): 
  
next line we reiterate the original classes using the super method 
    super().__init__(rooms, bathrooms, level)
then the process of creating an object continues as normal    
    self.beds = beds
    self.closet = closet
    self.patio = patio
    
this is the another subclass of Home but notice when defining the parameters 
Kitchen even tho it was made after Bedroom we dont have to add any of Bedrooms parameters
thats because inheritance is only one way

class Kitchen(Home):
  def __init__(self, rooms, bathrooms, level, pantry, material):
    super().__init__(rooms, bathrooms, level)
    self.pantry = pantry
    self.material = material



x = Home(4, 2, 2 )
print(x.bathrooms)

y = Bedrooms(4, 3, 2, 1, True, False)
print("the house has {} bedrooms but only {} bathrooms".format(y.rooms, y.bathrooms))

z = Kitchen(4, 3, 2, True, "tile")
print(z.material)
"""

class Car:
    def __init__(self, brand, style, model):
        # Initializing car attributes
        self.brand = brand
        self.style = style
        self.model = model
    
    def brand_style(self):
        # Formating a string to display car details
        return "The {} is a {} style car made by {}".format(self.model, self.style, self.brand)

class Brand(Car):
    def __init__(self, brand, style, model, engine, doors):
        # Using the superclass (Car's) initializer
        super().__init__(brand, style, model)
        
        # Initializing additional attributes specific to Brand class
        self.engine = engine
        self.doors = doors

# Creating an instance of Brand
honda = Brand("Honda", "Eco", "Civic", 2.0, 4)

# Calling the method on the honda object
print(honda.brand_style())  


"""
class Neighborhood: 
    def __init__(self, number_of_houses, pool, *name_of_streets):
        self.number_of_houses = number_of_houses
        self.name_of_streets = name_of_streets
        self.pool = pool
        
class House1(Neighborhood):
    def __init__(self, number_of_houses, pool, rooms, modernized, stories, *name_of_streets):
        super().__init__(number_of_houses, pool, *name_of_streets)
        self.rooms = rooms
        self.modernized = modernized
        self.stories = stories

GoldenGates = Neighborhood(20, True, "1st street", "2nd street", "3rd street")
print(GoldenGates.name_of_streets)

print("its a big neighborhood it has {} houses and they are all on {}".format(GoldenGates.number_of_houses,GoldenGates.name_of_streets))
print(GoldenGates.name_of_streets[2])

FirstHouse = House1(20, True, 5, True, 2, "1st street", "2nd street", "3rd street")
print("I live in the first house, it has {} rooms and we live on {}".format(FirstHouse.rooms, FirstHouse.name_of_streets[2]))
 


"""
class Human:
  def __init__(self, race, gender):
    self.race = race
    self.gender = gender


class Person1(Human):
  def __init__(self, race, gender, name, age, height, weight):
    super().__init__(race, gender)
    self.name = name
    self.age = age
    self.height = height
    self.weight = weight
    

Joshua = Person1("African American", "Male", "Joshua", 23, "6'0", 235)
legal_voting_age = list(range(23, 55))

if Joshua.age in legal_voting_age:
  print("{} you are allowed to vote".format(Joshua.name))
else:
  print("{} you are not allowed to vote".format(Joshua.name))
  
#youll figure it out the more you practice but heres two quick things 
#the think of the class as a libary that we can export to other files sort of how we would do the 
# import etc as etc right so when we see the word __main__ used its refering to where the class was 
#created, if its the main file were working currently in or imported from a different source

#also the = none when creating the class is equivalent to np.nan its so it doesnt throw a error
#if the persoschool class Student: 
"""  
def __init__ (self, name, age):
        self.name = name
        self.age = age

class College(Student):
    def __init__ (self, name, age, grade, Credit_Hours, location, school = None, Occupation = None):
        super().__init__(name, age)
        self.grade = grade
        self.Credit_Hours = Credit_Hours
        self.location = location
        self.school = school
        self.occupation = Occupation
       
thomas = College("Thomas", 23, "Junior", 53.7, "Florida")
Joshua = College(name="Joshua", age=22, grade="freshman", Credit_Hours=13.5, location="Alabama", school= None, Occupation= "Teacher")
print(Joshua.school)
"""