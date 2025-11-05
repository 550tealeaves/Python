# EX 35 - Branches and Functions

def gold_room():
  print("This rom is full of gold. How much do you take?")

  choice = input("> ")
  if "0" in choice or "1" in choice:
    how_much = int(choice)
  else:
      dead("Man, learn to type a number.")

  if how_much < 50:
    print("Nice, you're not too avaricious, you win!")
    exit(0)
  else:
    dead("You greedy scoundrel")

def bear_room():
  print("There is a bear here.")
  print("The bear has a bunch of honey.")
  print("The fat bear is in front of another door.")
  print("How would you move that gargantuan bear?")
  bear_moved = False

  while True:
    choice = input("> ")

    if choice == "take honey":
      dead("The bear looks at you then slashes your face off.")
    elif choice == "taunt bear" and not bear_moved:
      print("The bear has moved from the door.")
      print("You can go through it now.")
      bear_moved = True
    elif choice == "taunt bear" and bear_moved:
      dead("The bear becomes irate and chews your leg off.")
    elif choice == "open door" and bear_moved:
      gold_room()
    else:
      print("I don't understand what that means.")

def cthulhu_room():
  print("Here before you is the great evil Cthulhu!")
  print("He, it, whatever stares at you and you go insane.")
  print("Do you flee for your life or devour your own head?")

  choice = input("> ")

  if "flee" in choice:
      start()
  elif "head" in choice:
    dead("Well that was quite tasty, a bit tangy!")
  else:
    cthulhu_room()


def dead(why):
  print(why, "Good job!")
  exit(0)

def start():
  print("You are in a dark room.")
  print("There is a door to your right and left.")
  print("Which one should you open?")

  choice = input("> ")

  if choice == "left":
    bear_room()
  elif choice == "right":
    cthulhu_room()
  else:
    dead("You stumble around the room until you starve.")

start()

def dead(why):
  print(why, "Good job!")