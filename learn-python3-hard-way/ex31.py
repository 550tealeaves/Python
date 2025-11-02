# EX 31 - MAKING DECISIONS
# Can ask user for input and then make decision based on responses

print("""You enter a dark room with 2 doors. Should you enter door #1 or door #2?""")

door = input("> ")

# if door #1
if door == "1":
  print("There's an enormous bear inside eating a raspberry cheesecake.")
  print("What od you do?")
  print("1. Snatch the cake.")
  print("2. Yell at the bear.")

  bear = input("> ")
# Options for the bear
  if bear == "1":
    print("The bear eviscerates you, and your girlfriend mounrs your untimely demise")
  elif bear == "2":
    print("The bear only chomps on your legs, sparing your entrails, and leaves you crippled and broken.")
  else:
    print(f"well, doing {bear} is probably the better option")
    print("Bear runs off")

# if door #2
elif door == "2":
    print("You stare into the endless abuss at Cthulu's retina.")
    print("1. Blueberries.")
    print("2. Yellow jacket clothespins.")
    print("3. Understanding revolvers yelling melodies>")

    insanity = input("> ")

    if insanity == "1" or insanity == "2":
      print("Your body survives powered by a mind of jello.")
      print("Good job")
    else:
      print("The insanity rots your eyes into a pool of muck.")
      print("Good job")

# else statement if neither door 1 or door 2
else:
    print("You stumble around and fall on a knife and die. Whomp whomp whoooooommmmmp")