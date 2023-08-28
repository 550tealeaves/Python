1+1
2**4
True
type(False)
2**5
type("hello world")
type('hola mundo')
type(1.5)
type(65)
type("arrow")
type(["coffe", "yogurt", "oatmeal"])
type([1,5,7,8])
type([1, "bananas", 7, "eight"])
my_variable = "hello"
my_variable.upper() 
'any string'.upper()
'RANDOM STRING'.lower()
'nastasia'.upper()
classes = ['intro to python', 'edu tech', 'data viz', 'digital story']
classes.append('env tech')
classes
classes.remove('data viz')
classes
for drama in "entourage":
    print(drama)



#BOOLEANS
#can generate True/False by setting variables = to a negated variable
open_slot = True
is_available = not open_slot
print(is_available) #False

is_even = not False
print(is_even) #True


flight_mode = True
update = not flight_mode
print(update) #False 


flight_mode = True
updating = not flight_mode #False
use_apps = not updating #True
print(use_apps) #True


#Using != to check if variables are different
num_1 = 17
num_2 = 23
print(num_1 != num_2) #True


tries_left = 1
game_over = tries_left == 0
print("Game over:") #Game over:
print(game_over) #False


player_1 = 0
player_2 = 10
player_1 = 10 #reassigns new value to existing variable

same_score = player_1 == player_2 #see if variables are equal to each other

print("It's a tie:") #It's a tie
print(same_score) #True


#Can reassign a value to itself
downloaded = 9
downloaded = downloaded + 1
print(downloaded) #10

in_progress = downloaded != 10  #downloaded doesn't equal 10

print("Download finished:")
print(in_progress) #False b/c 10 is equal to 10