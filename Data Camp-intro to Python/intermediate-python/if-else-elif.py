# Conditional statements
# 	• If
# 	• Else
# 	• Elif


# 	• If condition :
# 		Expression
			
# 	• Can use multiple expressions, but as soon as Python reaches  the first one that is true, it will run that and cease running the rest 


## EXERCISE 1 
area = 10.0
if(area < 9) :
    print("small")
elif(area < 12) :
    print("medium")
else :
    print("large")

#prints medium




## EXERCISE 2 - IF
# Define variables
room = "kit"
area = 14.0

# if statement for room
if room == "kit" :
    print("looking around in the kitchen.")

# if statement for area
if area > 15.0 :
    print("big place!")



##EXERCISE 3 - ELSE
# Define variables
# Define variables
room = "kit"
area = 14.0

# if-else construct for room
if room == "kit" :
    print("looking around in the kitchen.")
else :
    print("looking around elsewhere.")

# if-else construct for area
if area > 15 :
    print("big place!")
else :
    print("pretty small.")



##EXERCISE 4 - ELIF
# Define variables
room = "bed"
area = 14.0

# if-elif-else construct for room
if room == "kit" :
    print("looking around in the kitchen.")
elif room == "bed":
    print("looking around in the bedroom.")
else :
    print("looking around elsewhere.")

# if-elif-else construct for area
if area > 15 :
    print("big place!")
elif area > 10 :
    print("medium size, nice!")
else :
    print("pretty small.")