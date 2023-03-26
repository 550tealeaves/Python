# WHILE LOOPS
# programs repeat same lines of code over to build things

# How to repeat code?
# 1. Write the code over - time-consuming
print("and again")
print('and again')
print('and again')

# To build bigger programs/sites, repeat code lines using WHILE LOOP
while True:  #will repeat it ad-infinitum
    print('and again')


# WHILE LOOP repeats code block while condition is TRUE
# If while loop condition stays True = infinite loop 
# will not run if FALSE
while False:
    print('skip me')

# To stop a while loop, create a variable OUTSIDE of the loop
# set the same variable (inside same code block) to False to break the while loop

keep_going = True
while keep_going == True:
    print('once more')
    keep_going = False

keep_going = True
while keep_going == True:
    print('and again')

    keep_going = False
    
    print('one more time')

auto_pilot = False
while auto_pilot == True:
    print('Autopilot on: vroom!')
    auto_pilot = False

print('again')

