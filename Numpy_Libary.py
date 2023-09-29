import numpy as np

"""
in full transperancy i have no idea why we use arrays as much as we do but youll see them often
and should get familiar with them. best way id explain they follow the same concept as list and tuples
they only take the same types of values if not they'll try to convert them to be the same or issue an 
error unlike the list and tuples they have a few extra features and we create them through type conversions

example:

In: x = [1, 2, 3]
In print(type(x))
Out: list  
In: x = np.array([1, 2, 3])
In: print(type(x))
Out: <class 'numpy.ndarray'> 

"""
x = np.array([1, 2, 3, 4, 5])
print(type(x))

"""each list inside our array counts towards the dimension total below is a one dimensional array

example: 
X = np.array([1, 2, 3]) 

this is a one dimensional array, its easiest to understand like this 

examples:
x = np.array([])
(0,0) this will return (0, 0) because there are no values inside the array

x = np.array([1])
(1,1) this will return (1, 1) because theres one array and one value

x = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
(2, 4) this will return (2, 4) because theres two arrays and 4 values in each array
 
this is a 2 dimensional array
Y = np.array([1, 2, 3, 4, 5], [6, 7, 8, 9, 10])
"""
x = [1, 2, 3, 4, 5] # one dimensional array
y = [6, 7, 8, 9, 10] #one dimensional array
xy = np.array([[6, 7, 8, 9, 10], [1, 2, 3, 4, 5]])  #two dimensional array remember the extra brackets

z = np.array([[x], [y]]) #this is the same as the line above it
print(z)
"""
we can find the dimensions of an array using the built in function shape 

example: 
Y = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(Y.shape)
(2, 5)

the built in function reshape does exactly what it says and reshapes the array to our classifications
example: 
In: Y = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
if we print Y.shape it would return (2, 5), and if we print Y as an array it would return 
[[ 1  2  3  4  5]
 [ 6  7  8  9 10]]
  
when we use the reshape function we can adjust the way it is formatted

In: X = Y.reshape(2, 3)
Out:
[[1 2 3]
 [4 5 6]]  
 """



""" now that we have an understanding of how to create them we can start exploring their different 
capabilities, starting with slicing them 

Example: 
X = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) 
In: Print(X[2])
Out: 3
In: Print(X[3:7])
Out: 4, 5, 6, 7, 8
"""
x = [1, 2, 3, 4, 5]
print(x[2]) 
"""
now if were working with a nested array and would like to select a specific index we have to specify
which array were selecting from as well as the indexed number the first number selects the array the 
second number selects the indexed position

Example: 
In: nested_array = np.array([[1,2,3,4,5], [6,7,8,9,10]])
In: print(nested_array[1][1])
Out: 7
"""
nested_array = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print(nested_array[1][1])

"""moving on the artithic operations such as addition, subtraction, multiplication, division, etc 
they follow the same concept weve seen before 

In: nested_array = np.array([[1,2,3,4,5], [6,7,8,9,10]])
In: total = nested_array[1] * 2 
In: print(total)
Out: [12 14 16 18 20]

it multiplies each number in our array by 2 thats the equivalent of 
for i in nested_array[1]:
  print i * 2
  
if we want to multiply a specific number in our array we can do that as well shown below 
In: nested_array = np.array([[1,2,3,4,5], [6,7,8,9,10]])
In: total = nested_array[1][3] * 2
In: print(total)
Out: 18
"""

nested_array = np.array([[1,2,3,4,5], [6,7,8,9,10]])
total = nested_array[1] * 2 
print(total)

sorted_array = sorted(nested_array[1])

"""
arr = np.arange(10)

this is type conversion a is currently a array
a = np.array([1, 2, 3, 4])
using the .array2str method we can convert it to a string
a = np.array2string(a)
print(type(b))


this will compare the two arrays and return a boolean value 
In: a = np.array([[1,2,3], [1,2,3]])
In: print(np.array_equal(a[0], a[1]))
Out: true



this is the numpy equivalent of range so the principles remain the same
In: x = np.arange(2, 11, 2)
In: print(x)
Out: [2, 4, 6, 8, 10]


its like range so it prints numbers between 0 and 20 but the num = 5 repersents the amount of
elements in our list but will return them as floats
In: x = np.linspace(0, 20, num = 5)
In: print(x)
Out: [ 0.  5. 10. 15. 20.]

sorts the array in ascending order 
r = np.array([2, 1, 5, 3, 7, 4, 6, 8])
np.sort(r)

sorts the array in descending order
r = r[::-1]

a = np.array([1, 2, 3, 4])
b = np.array([5, 6, 7, 8])
print(np.concatenate((a, b)))
"""
"""

this is interesting we start with a simple two dimensional array 
x = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print(np.mean(x, axis=1))

this will print 
3, 8 because those are the means for those two separate lists but when we change the axis number to 0
it no longer sees them as two separate lists it views them as coordinates one unified list the same way
matplotlib does when we plot using numpy

(1, 6)  3.5
(2, 7)  4.5
(3, 8)  5.5
(4, 9)  6.5
(5, 10) 7.5

and returns the average of these 
"""