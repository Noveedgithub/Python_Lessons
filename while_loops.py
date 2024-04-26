# While loops can execute a set of statements as long as the condition is true

i = 1               # setting the starting value of i before the while loop is executed
while i < 6:        # This checks that the value of i is still below 6
  print(i)          # If i is below 6, then i will be printed in the console
  i += 1            # i will have 1 added to it which is increase the value of i
                    # This will now loop until i is still lower than 6. This will print to 5 and stop
                    

# BREAK STATEMENT
# The break statement can stop the while loop, even if the condition is still true.

i = 1
while i < 6:
  print(i)
  if i == 3:        # Setting the condition of the break, even though the while loop is set to keep looping until it reaches 6,
    break           # We break that loop once the break condition has been met
  i += 1            # This will now keep looping until i has changed to 3 and will then stop. 
                    

#CONTINUE STATEMENT
# The continue statement stops the loop (iteration) at the set condition and then continues after

i = 0
while i < 6:
  i += 1
  if i == 3:        # Setting the continue statement to stop and then continue after
    continue        # This will now skip the loop once it reaches 3 and then continue from 4, until the while loops condition has been met.
  print(i)
  

# ELSE STATEMENT
# The else statement can run a block of code when the while condition is no longer true.
  
i = 1
while i < 6:
  print(i)
  i += 1
else:                                       # This loop will now run until the value of i reaches 5. After 5, the while condition is no longer true
  print("i is no longer less than 6")       # When the while condition is not true, the else statement is added to instruct the while loop 
                                            # that the while loop is no longer true and to run the block of code, set under else.


