# ZeroDivisionError: Raised when you try to divide a number by zero.
# ValueError: Raised when a function's argument is of an inappropriate type.
# IndexError: Raised when a sequence subscript is out of range.
# KeyError: Raised when a dictionary key is not found.
# FileNotFoundError: Raised when a file or directory is requested but doesn't exist.
# Except: used to catch all other exceptions like the else statement

items = ['apple', 'banana', 'cherry']

while True:
    try:
        i = int(input("Enter the numbered position of the fruit you want: "))
        print("You selected the fruit: {}" .format(items[i]))
        break  # If we reach this line, no exception was raised and we can exit the loop.
    except IndexError:
        print("Sorry, that index is out of range. Please try again.")
    except ValueError:
        print("Sorry, that's not a valid number. Please try again.")



while True: #we set up a outter loop that will run until ended(break)
    try: #try is exactly as it sounds
         #line 1, line 2 while true try this script
        age = int(input("Enter your age: ")) #we change the input from a string to a integer
        print(age + 5) #add the age variable to 5 and print the result
        break #end of the loop
    except ValueError: #if the input isn't a integer return the following and continue the loop
        print("Please enter a valid number:")
        


x = 3

while True:
    try:
        query = input("x is a number between 0 and 5. Can you guess what number it is?\n")
        query = int(query)  # Convert input to an integer

        # Check if the user guessed correctly
        if query == x:
            print("Congratulations! You guessed the correct number.")
            break  # Exit the loop once the correct number is guessed
        else:
            print("No, try again!")
    
    except ValueError:  # Catching non-numeric inputs
        print("Umm, no. That isn't a number. Try again.")
