import pandas as pd 
import numpy as np
"""
pandas is arguably one of the most common modules you'll use. its used mostly to store large amounts
of data similar to the way we use dictionaries and technically thats what they really are until 
converted so many of the same principles and functions apply

example:
contacts = {
  "Name": ["Joshua", "Thomas", "Brandon"],
  "Email": ["Joshua@example.com", "Thomas@example.com", "Brandon@example.com"],
  "Number": ["(900) 865-1234", "(432) 473- 1234", "(883) 2943-4652"]
}
pd.DataFrame() is the line of code that we use to ,ake the conversion
df = pd.DataFrame(contacts)
when we need to get information from the dataframe again we just call it using df
"""

contacts = {
  "Name": ["Joshua", "Thomas", "Brandon", "Sarah", "Ashley", np.nan],
  "Email": ["Joshua@example.com", "Thomas@example.com", "Brandon@example.com", "Sarah@example.com", np.nan, np.nan],
  "Number": ["(900) 865-1234", "(432) 473- 1234", "(883) 2943-4652", np.nan, "(324) 754-1892", "(967) 656-9000"]
}

df = pd.DataFrame(contacts)
print(df)

"""
you'll notice it prints a bit more organized showing the keys at the top, the columns listed below
and on the left hand side is the indexed number for reference 

  
        Name                Email           Number
0   Joshua   Joshua@example.com   (900) 865-1234
1   Thomas   Thomas@example.com  (432) 473- 1234
2  Brandon  Brandon@example.com  (883) 2943-4652
3    Sarah    Sarah@example.com              NaN
4   Ashley                  NaN   (324) 754-1892
5      NaN                  NaN   (967) 656-9000

I mentioned that the basis of the pandas library is built off of dictionaries so many of the functions 
we use will look familiar nut here are a few of the new ones 

Examples:
by default it prints the top 5 elements of our dataframe unless otherwise specified

In: print(df.head)
Out:     Name                Email           Number
0   Joshua   Joshua@example.com   (900) 865-1234
1   Thomas   Thomas@example.com  (432) 473- 1234
2  Brandon  Brandon@example.com  (883) 2943-4652
3    Sarah    Sarah@example.com              NaN
4   Ashley                  NaN   (324) 754-1892

In: print(df.head(2))
Out:     Name                Email           Number
0   Joshua   Joshua@example.com   (900) 865-1234
1   Thomas   Thomas@example.com  (432) 473- 1234

tail does the reverse in printing the specified end of the list 

In: print(df.tail(2))
Out: 3    Sarah    Sarah@example.com              NaN
     4   Ashley                  NaN   (324) 754-1892

we spoke about dimension's in numpy but it applies to dictionaries as well using the .shape function
it takes into account the keys and the values first number represents the values and the second number represents
represents the number of keys

In: print(df.shape)
Out: (6, 3) 6 

"""
print(df.head)



print(df.shape)

df.info("Name")


print(df.tail) #prints the last 5 elements of the datframe
print(df.tail(2)) #prints the last two elements of the dataframe


df["State"] = ["Florida", "Florida", "Georgia", "Texas", "South Carolina", np.nan]
print(df)


"""
import pandas as pd 

School = {
    "Subject": ["Math", "Science", "English"],
    "Teachers": ["Ms. Smith", "Mr. Thomas", "Mrs. John"],
    "Room Number": [201, 111, 306],
    "Class Capacity": [20, 10, 25]
}

df = pd.DataFrame(School)
subjects = (df["Subject"].to_list())
subjects = ','.join(map(str,subjects))
print(subjects)

print("our school focuses on a variety of subjects but the main {} are {}".format(len(subjects), subjects))

"""
contacts = {
  "Name": ["Joshua", "Thomas", "Brandon", "Sarah", "Ashley", np.nan],
  "Email": ["Joshua@example.com", "Thomas@example.com", "Brandon@example.com", "Sarah@example.com", np.nan, np.nan],
  "Number": ["(900) 865-1234", "(432) 473- 1234", "(883) 2943-4652", np.nan, "(324) 754-1892", "(967) 656-9000"],
  "Grade" : [87.3, 82.5, 94.8, 83.7, 96.9, 99.0]
}

df = pd.DataFrame(contacts)
print(df["Grade"])

def ApplyCurve(x):
  return x + 2.0

#the .apply function affects the whole row without using the map or a for loop
df["Grade"] = df["Grade"].apply(ApplyCurve)
print(df["Grade"])


contacts = {
  "Name": ["Joshua", "Thomas", "Brandon", "Sarah", "Ashley", np.nan],
  "Email": ["Joshua@example.com", "Thomas@example.com", "Brandon@example.com", "Sarah@example.com", np.nan, np.nan],
  "Number": ["(900) 865-1234", "(432) 473- 1234", "(883) 2943-4652", np.nan, "(324) 754-1892", "(967) 656-9000"],
  "Grade" : [87.3, 82.5, 94.8, 83.7, 96.9, 99.0]
}

df = pd.DataFrame(contacts)


"""

Im going to go over pulling and using information from datframes fairly straightforward but lets start 
with creating a simple dataframe 

Students = {
  "Name" : ["Joshua", "Karri", "Thomas"],
  "Grade" : [99.0, 84.0, 77.0]
}
df = pd.DataFrame(Students)

we have a dataframe called Students typically to get information we'd do 
print(df["Name"])

this would return the following
0    Joshua
1     Karri
2    Thomas

or we could also use the following
print(df["Name"][0])
which would return 
Joshua

(
Subset but while were disccusing it lets go over loc and iloc

iloc looks through our dataframe using the indexed position it typically takes two arguments 
one for the index number and one for the column name example: 

print(df.iloc[0]["Name"]) 

this will print Joshua but the following prints the same thing 
print(bool(df.iloc[0]["Name"] == df["Name"][0]))


loc is slightly different it doesnt use index posistion to pull a single value it pulls all values 
associated with the index so it takes one argument which is the index number

this
print(df.loc[0])

will print this
Name     Joshua
Grade      99.0
)

back to the original topic now this is our dataframe lets get the information for the 

Students = {
  "Name" : ["Joshua", "Karri", "Thomas"],
  "Grade" : [99.0, 84.0, 77.0],
  "Email" : ["Jemail@Example.com", "Kemail@example.com", "Temail@example.com"]
}
df = pd.DataFrame(Students)

lets say we only want to get the information for students that scored higher than a 90 on the test
we'd write the following script 

print(df[df["Grade"] >= 99.0])

and since Joshua is the only student on the test who scored higher than a 90 it will return
0  Joshua   99.0  Jemail@Example.com

but this prints all the information including the email we dont need that right now so lets cut it down
we put our columns names into a list for later use
Columns = ["Name", "Grade", "Email"]

save our condition as a variable  
passing = (df[df["Grade"] >= 99.0])

now to get the only the information we want we need to use multiple lists in one another
print(passing[ [Columns[0], Columns[1]] ])

lets see it in action below 

"""

Students = {
  "Name" : ["Joshua", "Karri", "Thomas"],
  "Grade" : [99.0, 84.0, 77.0],
  "Email" : ["Jemail@Example.com", "Kemail@example.com", "Temail@example.com"]
}
df = pd.DataFrame(Students)
print(df[df["Grade"] <= 90])

""" 
you can think of it as a SQL query
print(df[df["Grade"] <= 90])

SELECT * FROM Students 
WHERE Grade <= 90  

and 
passing = (df[df["Grade"] <= 90])
print(passing[["Name", "Grade"]])

SELECT Name, Grade FROM Students 
WHERE Grade <= 90
"""

"""
Heres how we handle multiple conditions for a more in depth analysis using the same dataframe with more depth 
Students = {
  "Name" : ["Joshua", "Karri", "Thomas", "Jake"],
  "Grade" : [99.0, 84.0, 77.0. 88.9, ],
  "Level" : ["Level 1", "Level 4", "Level 5", "Level 4"]
}
df = pd.DataFrame(Students)

for the more in depth analysis we have to use the loc(briefly touched on it earlier) its going to look funny to start
but like in html we always have an opening and closing tag so where you see one you'll see another I indicated the 
opening and closing tags using numbers 1 goes with 1 2 with 2 and so on its confusing at first but practice helps 


      1 2 3         3            2   4  5         5           4 1   
df.loc[(df["Example"]== "Example") & (df["Example"]== "Example")]

df.loc[(df["Level"] == "Level 4") & (df["Grade"] >= 85.0)]


lets start off simple lets check out level 4 two questions we want to answer with this analysis 

1. who is and how many students are apart of level 4 
2. Who has passed in Level 4 (passing grade < 85.0)


two answer number 1 we can 
LengthOf4 = df[df["Level"] == "Level 4"]
print(len(LengthOf4)) this returns 2 so we have the answer to question 1

1. who is and how many students are apart of level 4 (2)

next we can answer 2 using the more in depth analysis 

Level4Passing = df.loc[(df["Level"] == "Level 4") & (df["Grade"] >= 85.0)]
print(Level4Passing[["Name", "Grade"]])

and we've answered question 2 the only person in level 4 that passed was Jake with a grade of 88.9
Name  Grade    
3  Jake   88.9  
"""
Students = {
  "Name" : ["Joshua", "Karri", "Thomas", "Jake"],
  "Grade" : [99.0, 84.0, 77.0, 88.9],
  "Level" : ["Level 1", "Level 4", "Level 5", "Level 4"]
}
df = pd.DataFrame(Students)

Level4Passing = df.loc[(df["Level"] == "Level 4") & (df["Grade"] >= 85.0)]
print(Level4Passing)

"""
this portion will be short but important its about

Map
Describe()

both simple but effective, lets get started with map its an inline for loop 
map takes two arguments the function and what you want to apply it to 

map(function, argument)
Students = {
  "Name" : ["Joshua", "Karri", "Thomas", "Jake"],
  "Grade" : [99.0, 84.0, 77.0, 88.9],
  "Level" : ["Level 1", "Level 4", "Level 5", "Level 4"]
}
df = pd.DataFrame(Students)

we create a function that adds additional points
def Curve(Grade):
    return Grade + 5.0

save our grades from the dataframe into the variable grades
Grades = df["Grade"] 

Use the map function to run it through 
UpdatedGrade = map(Curve,Grades)

**important** 
after using the map function we must convert it to a list if not when we print the variable UpdatedGrade it will print
this <map object at 0x00000183ECF88C10>


UpdatedGrade = list(UpdatedGrade)

once converted to a list it will print
print(UpdatedGrade)
[104.0, 89.0, 82.0, 93.9]

if we were to do this without using map it would be 
def Curve(Grade):
    return Grade + 5.0
    
Grades = df["Grade"] 

for grade in Grades:
    print(Curve(Grades))
Name: Grade, dtype: float64
0    104.0
1     89.0
2     82.0
3     93.9

one last way to do this would be through the apply() method which also takes one argument we update the values like normal
df["Grade"] = 

establish what were updating it to be
df["Grade"] = df["Grade"] 

then add the apply method 
df["Grade"] = df["Grade"].apply(Curve)
print(df)
     Name  Grade    Level
0  Joshua  104.0  Level 1
1   Karri   89.0  Level 4
2  Thomas   82.0  Level 5
3    Jake   93.9  Level 4

using the df from earlier the df gives a brief overview of the numerical inputs in the dataframe
print(df.describe()) it gives a overview of the number of entries(count), average(mean), minimum(min), and maximum(max)

            Grade
count    4.000000
mean    92.225000
std      9.244954
min     82.000000
25%     87.250000
50%     91.450000
75%     96.425000
max    104.000000

"""

def Curve(Grade):
  return Grade + 5.0

Students = {
  "Name" : ["Joshua", "Karri", "Thomas", "Jake"],
  "Grade" : [99.0, 84.0, 77.0, 88.9],
  "Level" : ["Level 1", "Level 4", "Level 5", "Level 4"]
}
df = pd.DataFrame(Students)

df["Grade"] = df["Grade"].apply(Curve)
#print(df["Grade"])

#or 

UpdatedGrade = map(Curve, df["Grade"])
UpdatedGrade = list(UpdatedGrade)
df["Grade"] = UpdatedGrade
# print(df)


#and lastly 

NewGrade = []
for grade in df["Grade"]:
  grade += 5
  NewGrade.append(grade) 
df["Grade"] = NewGrade
print(df)

#all three do the same thing thats the beauty of python
