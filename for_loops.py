# A for loop is used for iterating (looping) over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).
# With the for loop we can execute a set of statements, once for each item in a list, tuple, set etc.

fruits = ["apple", "banana", "cherry"]      # FOR LOOPING THROUGH A LIST, SET, TUPLE AND DICTIONARY
for x in fruits:                            # a for loop has been set to loop continuously in the fruit list and has assigned a variable x
  print(x)                                  # this will now start by printing "apple", then it will loops back and print banana etc until it reaches the end of the list


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

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":                         # A continue condition has been set to skip once the loop has reached banana
    continue                                # This will now loop until it reaches banana. Once banana has been reached, it will skip banana and move onto cherry 
  print(x)                    

