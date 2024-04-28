# A for loop is used for iterating (looping) over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).
# With the for loop we can execute a set of statements, once for each item in a list, tuple, set etc.

fruits = ["apple", "banana", "cherry"]      # FOR LOOPING THROUGH A LIST, SET, TUPLE AND DICTIONARY
for x in fruits:                            # a for loop has been set to loop continuously in the fruit list and has assigned a variable x
  print(x)                                  # this will now start by printing "apple", then it will loops back and print banana etc until it reaches the end of the list
  
  
# Looping through a string.

for x in "banana":                          # This loops will print each letter of the word banana, on a seperate line.
  print(x) 


# THE BREAK STATEMENT
# The break statement stops the loop (iteration) before it can loop through all the items

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":                         # A break condition has been set to stop the loop once it has reached banana
    break                                   # the break statement needs to be written under the condition to execute, once the condition has been met.
                                            # This will now print all the words in the list but will stop when the loop has printed banana (cherry will not be printed)
                                            
                                            
# THE CONTINUE STATEMENT
# The continue statement stops the loop (iteration) at the set condition and then continues after

fruits = ["apple", "banana", "cherry", "tomato"]
for x in fruits:
  if x == "banana":                         # A continue condition has been set to skip once the loop has reached banana
    continue                                # This will now loop until it reaches banana. Once banana has been reached, it will skip banana and move onto cherry 
  print(x)                    
  
  
# THE RANGE FUNCTION - range()
# To loop through a set of code a specified number of times, we can use the range() function,
# The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and ends at a specified number.

for x in range(6):                          # The range has been set to 6. This will now print number upto 5 on a seperate line. 
  print(x)                                  # This is because the (6) refers to index positions and index positions start at 0. (0=1, 1=2, 2=3 etc)

for x in range(2, 6):                       # You can also set your own range by adding the parameter in the brackets.
  print(x)                                  # eg for x in range(2, 6) will means values from 2 to 6 (not including 6, so will stop at 5)
  
for x in range(2, 30, 3):                   # it is possible to specify the increment value by adding a third parameter: range(2, 30, 3)
  print(x)                                  # This will now start the range from 2 until 30 and will go up in incriments of 3.
  

# Else in For Loop
# The else keyword in a for loop specifies a block of code to be executed when the loop is finished

for x in range(6):                          
  print(x)
else:                                       # Once the for loops has finished, the else statement is executed and will print "Finally Finished".
  print("Finally finished!")                # The else statement will not work if the loop is stopped by a break statement 
  

# NESTED LOOPS - A nested loop is a loop inside a loop
# The "inner loop" will be executed one time for each iteration of the "outer loop"

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y) 
    
    
# THE PASS STATEMENT
# for loops cannot be empty, but if you for some reason have a for loop with no content, put in the pass statement to avoid getting an error

for x in [0, 1, 2]:
  pass