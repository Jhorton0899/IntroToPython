import matplotlib.pyplot as plt
import numpy as np


"""
so this is a bit interesting to me at least we plot using matplotlib.pyplot and numpy at least in this 
example so lets make two arrays

x = np.array([1, 2, 3, 4, 5])
y = np.array([6, 7, 8, 9, 10])

plt.plot(x, y)
plt.show()

this will print a straight line going from the bottom of the graph to the top straightforward. the way its
graphed is it takes the values from both arrays and combines them to create coordinates(plot points)
so for our example it will look like 
(1, 6)
(2, 7)
(3, 8)
(4, 9)
(5, 10)

hopefully the line is starting to look more familiar now but if it isnt we can make the plot points 
more defined by using the marker function it takes a string value but allows us to add a indicator
for each plot point

x = np.array([1, 2, , 3, 4, 5])
y = np.array([6, 7, 8, 9, 10])

plt.plot(x, y, marker = "o")
plt.show() 

now our line has a little o indicator for each plot point note you can also change the marker size 
and color using ms and markerfacecolor 

x = np.array([1, 2, , 3, 4, 5])
y = np.array([6, 7, 8, 9, 10])

plt.plot(x, y, marker = "o", ms = 12, markerfacecolor= "r")
plt.show() 

"""
x = np.array([1,8]) 
y = np.array([3, 10])

plt.plot(x, y, marker = "x", ms = 20, )
plt.show()

""" 
theres a bunch of other little features that we can add to customize our graph but id suggest reading the 
documentation or https://www.w3schools.com/python/matplotlib_labels.asp for a full indepth review for now
ill go over the basics using the label function adding basic labels to the X and Y axis and the title 

x = np.array([1,8]) 
y = np.array([3, 10])

plt.plot(x, y, marker = "x", ms = 20, )
plt.title("Label)
plt.xlabel("X")
plt.ylabel("Y")
plt.show()

we also have grid by it takes a boolean value but by default it is True 

plt.grid() 
"""

"""
this is how we create a bar plot using matplotlib same concept as before but instead of using two
arrays, we use the X array as the markers and the Y as the plot points for example

names = ["Joshua", "Thomas"]
testscores = np.array([96.7, 77.4])
plt.bar(names, testscores)
plt.show()
in this example under each bar will be the X values and the Y values will be the plotted

we can flip our plot on its side by changing the type of the plot
names = ["Brittany", "Brian", "John"]
test_scores = np.array([89.5, 94.3, 78.0])
plt.barh(names, test_scores)
plt.show()
   
"""
import matplotlib.pyplot as plt
import pandas as pd

school = {
  "Teachers": ["Mrs. Barber", "Mr. Hart", "Mr. Green", "Ms. Harold", "Ms. Thomas"],
  "Subject": ["Mathematics", "Science", "Computer Science", "Social Studies", "English"],
  "Class Capacity": [24, 27, 32, 25, 35],
  "AVG test grade": [83.8, 79.2, 74.3, 89.3, 86.5]
}

df = pd.DataFrame(school)

test = df["AVG test grade"]  
subjects = df["Subject"]
colors = ['blue', 'green', 'orange', 'purple', 'red']

bars = plt.barh(subjects, test, color=colors)
plt.xlabel("Average Test Grade")
plt.ylabel("Subject")
plt.title("Average Test Grades by Subject")

plt.legend(bars, subjects)
plt.tight_layout()

plt.show()
3

"""
import numpy as np
import matplotlib.pyplot

x = np.array([ 1, 2, 3, 4])
y = np.array([24, 43, 11, 14])

plt.plot(x, y)
plt.show()
"""

