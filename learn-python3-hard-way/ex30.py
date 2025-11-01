# EX 30 - ELSE AND IF

people = 30
cars = 40
trucks = 15

if cars > people:
  print("We should take the cars")
elif cars < people:
    print("We should abandon the cars")
else:
    print("We can't decided.")

# trucks +=50

if trucks > cars:
  print("That's way too many trucks - pollution, people!")
elif trucks < cars:
  print("Perhaps we could attempt the trucks - hopefully folks have their license.")
else:
  print("We are still unable to decide.")

if people > trucks:
  print("Alright, let's just take the trucks. Screw the cars.")
else:
  print("Fine, let's stay home, guys.")

