#before starting with that you'll see these often and should understand what they mean first.
#continue: means to skip block if condition is met 
#break means to exit loop if condition is met

#an example of the continue is below
for i in range(21): #for every number in range of 0 to 20 do as follows 
    if i % 2 == 0: #if the number divided by 2 is = to 0 skip
      continue #the continue repersents skipping bypassing it and do the next line of code
    print("{} is an odd number".format(i))

#a more detailed example is as followed 
names = ["tory", "kenny", "mike", "carlos"]
vowels = ("a", "e", "i", "o", "u")
for name in names:
  if vowels in names:
    continue #skip
  else:
    print("{} does not have a vowel".format(name))

#---------------------------------------------------------------------------------------------

a = 2 #x is equal to 2
while a < 4: # while x is less than 4 
    print(a + 1) #print x + 1
    a += 1  # Increment x to break the infinite loop eventually #the += adds 1 to x and updates x to the value
    if a > 4: #if x ever becomes greater than 4 then break the loop
        break
else:
    print("{} is less than 4".format(a)) #if it never happens then print x is less than 4
#--------------------------------------------------------------------------------------------------------------
x = 12
while x > 10: #this is the overhead condition, as long as this is true do whats below
  x -= 1 #were subtracting 1 from x then printing x and this will continue until x is less than 10
  print(x)
#----------------------------------------------------------------------------------------------------

# Let's start with a variable `n`
n = 0
while n < 5:  # while `n` is less than 5 run the following script
    if n == 3: #if `n` becomes 3 
        break  # stop the script
    print(n)  # print the value of `n` #until n is equal to 3 continue with the script
    n += 1  # add 1 to `n`, updating the value of `n`
    
#------------------------------------------------------------------------------------------------------

# Let's start with a variable `n`
n = 0
while n < 5:  # while `n` is less than 5
    n += 1  # add 1 to `n`, updating the value of `n`
    if n == 3:
        continue  # If n is equal to 3, skip the rest of the loop and continue with the next iteration
    print(n + 9)
#---------------------------------------------------------------------------------------------------------
n = 0
while n < 5:  # While `n` is less than 5
    n += 1  # Add 1 to `n`, updating the value of `n`
    
    if n == 3:
        continue  # If n is equal to 3, skip the rest of the loop and continue with the next iteration

    print("Outer loop, n + 9 is: {}".format(n + 9))  # Printing in outer loop
    
    # Now, let's add an inner loop that counts down from `n` until it reaches 0
    m = n  # We'll use another variable `m` for our inner loop
    while m > 0:  # While `m` is greater than 0
        print("Inner loop, m is: {}".format(m))  # Printing in inner loop
        m -= 1  # Subtract 1 from `m`
#---------------------------------------------------------------------------------------------------------

    """

x = list(range(11))
print(x)

while True:
  for i in x :
    print(i)
  break the break has to match for loop to avoid infinite loop

  """