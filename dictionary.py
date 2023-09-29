""" 
dictionaries are one of pythons versions of a table. they take all data types 
each dictionary has a key/value(rows/columns in sql), they are built from lists [] 
we establish a list in a similar way we'd do a variable sort of because thats what it is a 
variable that holds a dictionary. we start with the variable name followed by {} 
there are two ways of writing them one line 
example: 
nba = {"team": ["celtics", "nets"], "all-star":["Jayson Tatum, Jaylen Brown", "Ben simmons, Mikal Bridges"]
this can be a bit confusing so the preferred approach is to leave it stacked

example: 
dictionary = {
  
} 

inside of our curly braces are our keys and values, mentioned earlier but they can take all data types

example: 
dictionary = {
  "name": ["john"]
}

if were going to be working with different keys we need to add commas in between 
dictionary = {
  1 : [1, 2, 3, 4, 5],
  2 : [6, 7, 8, 9, 10]
}


"""
NFL = {  #our dictionary/variable name is NFL I can use this to call it again later 
  "team" : ["bengals", "browns", "ravens", "steelers"], #key here is a string called "team"
   "qb" : ["Joe Burrow", "Deshuan Watson", "Lamar Jackson", "Kenny Pickett"], #key here is a string called "qb"
   "wr" : ["Jamar Chase", "Amari Cooper", "Odell Beckham Jr", "George Pickens"] #key here called "wr"
}

print(NFL.keys()) #this will only print the keys inside of our dictionary
print(NFL.values()) #this will only print the values inside of our dictionary
print(NFL["team"]) #this will print all the values associated with the key team

""" 
we can get specific values from a list as shown below

example 
dictionary = {
  "examples": ["example1","example2"],
  examplespart2": ["example3","example4"],  
}
print(dictionary[examples][0]) 

we identify the dictionary name first, then in brackets single out the key and the index number
of the value we'd like to retrieve.

we can also use the get function 
dictionary = {
  "examples": ["example1","example2"],
  "examples2": ["example3","example4"],  
}

print(dictionary.get("examples"))
this will print the same thing as before but with the added benefit of returning none if the key is empty

Example:
dictionary = {
  "examples": ["example1","example2"],
  "examples2": ["example3","example4"],  
  "examples3": [],
}
print(dictionary.get("examples3"))
should return

"""
print(NFL["team"][0])  

 # we convert the value that we just retrieved into its own variable 
bengals = NFL["team"][0]
bengals_wr = NFL["wr"][0] 
bengals_qb = NFL["qb"][0]
NFL_QBs = NFL.get("qb")
print("the {}, are one of my favorite teams. {} and {} make a great combo".format(bengals, bengals_wr, bengals_qb))

""""
im going to show how to update our dictionary

example:
nba["key name"] = ["value", "value2", "value3"]

if we print the dictionary it will then print the previous dictionary 
with the addition of the new value pair

lets say we want to add a new key value pair to the dictionary we follow the following steps:
-we start with the dictionary name 
-followed by the new key and values we want to input creating a new key value pair 

example:
nba["key name"] = ["value", "value2", "value5"]


we made a mistake and need to update a value inside the dictionary, its the same concept as before
- variable name followed by the value index we want to update we made a mistake and need to update
value5 to vaLue3 
- in our case value5 is in index 2 so we print nba["key name"][2] 
- followed by adding the value we want to change it too
- nba["key name"][2] = ["value3"]

example:
nba["key name"][2] = ["value3"]

input: print(nba) 
output: nba["key name"] = ["value", "value2", "value3"]

we can delete items from our dictionary using a similar approach to the way we do in list
- for our example we'll delete value number 9 
- we start with using the del followed by the key and the specific index value we want to delete

examples:             0         1         2        3     
nba["key name"] = ["value", "value2", "value3", value9]
input: del nba["key name"][3]
output: nba["key name"] = ["value", "value2", "value3"] 
"""
NFL["coaches"] = ["Zac Taylor", "Kevin Stefanski", "John", "Mike Tomlin"]
# I made a mistake and forgot to add the last name for john lets update it before printing it
NFL["coaches"][2] = ["John Harbaugh"]
print(NFL)



"""
We can perform arithmetic operations within our function I'm creating a function 
to make the process a bit more efficient i added plus one to each because when using 
the range function it doesn't include the last number in the range function
""" 
class1 = list(range(88, 100 + 1)) 
class2 = list(range(76, 87 + 1))
class3 = list(range(65, 86 + 1))
class4 = list(range(50, 64 + 1))
class5 = list(range(49, 0 + 1))

exam_grades = {
    "class1": class1,
    "class2": class2,
    "class3": class3,
    "class4": class4,
    "class5": class5
}

def class_average(list):
    list = sum(list) / len(list)
    return(list)
  
class3_average = class_average(class3)
class4_average = class_average(class4)
print(class3_average)


import pandas as pd
