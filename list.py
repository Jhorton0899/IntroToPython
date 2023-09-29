#lets start working with lists, list are mutable and allow us to modify them with a few different functions

x = list() #this is an empty list
x.append(1) #using the append function we add 1 automatically to the end of our list
print(x)
x = x.insert(0, 2) #the first number represents index position and the second is what were adding

number = list(range((21))) #range is used to list the numbers between 0 and 21
print(number)
#this is slicing a list
#the first index is where we'll start within our list
#the second is where we'll end within our list
#the last number repersents the pattern
print(number[0:22:2]) 
print(number[6:12])

#this example is going to feed off our earlier one.
number2 = number.copy() #using the copy function we copy an exact match of our earlier list
print(number2)
number.append(21)
print(number)#it will print up to 20 
print(number2)#it will print and include the number 21

names = [["john", "josh", "jacob"], ["Tom", "Tony", "Thomas"]] #this list contains two lists(nested)
print(names[0][1])#the first element[0] is the list we want to access, the second element is what we want from said list

print(names[1][0:2])#first element is which list, second like earlier is to say print from index 0 to index 2
print(names[1][1:]) #this says print from index 1 until completion 

colors = ["red", "green"]
colors.extend(["blue", "yellow"]) #the extend function is used to add multiple elements to the end of the list
print(colors)  # Output: ["red", "green", "blue", "yellow"]


#i discussed adding to our list but this is how we'd remove elements from the list
cars = ["bmw", "audi", "toyota", "honda"]
cars.remove("bmw") #the remove function is pretty simple 
print(cars)

#or we could use the pop function that
fruits = ["apple", "banana", "orange"]
fruits = fruits.pop(1) 
print(fruits)  


#the sort is similar to the ORDER BY ASC by default it returns the elements in ascending order
numbers = [3, 1, 4, 1, 5, 9, 2]
numbers.sort()
print(numbers)  
numbers.sort(reverse=True)#this orders it by descending order

#--------------------------------------------------------------------------------------------------------------
    
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [num for row in matrix for num in row]
print(flattened)  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]

squares = [x**2 for x in range(1, 6)]
print(squares)  # Output: [1, 4, 9, 16, 25]


inventory = list(range(1,11, 2))
#same as 
inventory = list(range(1,11)[::2]) 

                 
                