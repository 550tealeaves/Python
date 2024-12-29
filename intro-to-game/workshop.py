# install pygame in the terminal 
# python3 -m pip install -U pygame --user (not working b/c I don't have python installed but run it through Anaconda)

# Import pygame library
#Docs are at https://pygame.org/docs/
# Type this in the console first - pip3 install pygame
import pygame


# Inititalize pygame
pygame.init() # initialize pygame

# Add dimensions & title - variable is capitalized to indicate that it will not change, will always be 800
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
SCREEN_TITLE = "Froggish"


#Add colors on screen (black/white)
WHITE_COLOR = (255, 255, 255) 
BLACK_COLOR = (0, 0, 0)

# Frame rate - controls how fast the game moves and how often screen refreshes  
clock = pygame.time.Clock()
TICK_RATE = 60 # industry standard is 60 frames per second

# Specify the font 
pygame.font.init() # initialize font library - look at library for options
font = pygame.font.SysFont('comicsans', 75) #choose font in string & font size

### CREATE GAME SCREEN ###
# All python classes start with a capital (every word in class does)

# def __init__ is the initializer area - define all parameters/values you want class to have
# always pass self as the first parameter into python class 
# title, width, height are just placeholders for the actual variables screen_width...
class Game:
    def __init__(self, image_path, title, width, height):
        self.title = title # can access & work w/ values after passing self
        self.width = width
        self.height = height

        # Create game screen object 
        # .display - show display module of library
        # set_mode sets display size - takes a tuple value = (())
        self.game_screen = pygame.display.set_mode((width, height)) 
        # Fill screen with color - white
        self.game_screen.fill(WHITE_COLOR)
        # Set title w/ caption # pass in title
        pygame.display.set_caption(title)

        # Create background image
        background_image = pygame.image.load(image_path)
        # Scale background image
        self.scaled_bkg = pygame.transform.scale(background_image, (width, height))
    # create function that runs the game - put it outside the initializer function but still w/in the Game class
    def runGame(self):
        # Set game over to false as initial
        isGameOver = False 
        #Defines direction 
        direction = 0 

        # Create the playing character - object is lower case but class is capitalized - give it image, x, y, width, height
        player_character = PlayerCharacter('frog.png', 380, 700, 50, 50) # frog size is 50x50

        # add enemy character class
        enemy_0 = EnemyCharacter('enemy.png', 20, 600, 50, 50) 

        # Create a while loop so that the game is still running & updating until the game is over
        while not isGameOver:
            for event in pygame.event.get():  # for each event happening on screen
                # did user press quit
                if event.type == pygame.QUIT:
                    isGameOver = True #if so, closes game screen
                print(event)
                #Listen for key presses (arrow keys)
                direction = pygame.key.get_pressed()

            #Update display
            pygame.display.update()
            # Update the display 60 frames/second
            clock.tick(TICK_RATE)
            # add background
            self.game_screen.blit(self.scaled_bkg, (0, 0))

            # Place the character and update its position 
            player_character.draw(self.game_screen) # draws frog on top of background
            player_character.move(direction) # moves character

            #Draw the enemy on the screen
            enemy_0.draw(self.game_screen)
            enemy_0.move(self.width)


        #Close program if the game is over - set it outside the isGameOver loop
        pygame.quit()
        quit() # stops script execution


# Create GameObjects class
# All objects have image, x, y, width, height
class GameObjects:
    def __init__(self, image_path, x, y, width, height):
        # Allow the objects to use the attributes - assign them to self
        self.x_pos = x # x position
        self.y_pos = y # y position
        self.width = width
        self.height = height

        # Load the image from image path - will transform all images to that size 
        object_image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(object_image, (width, height))

    # Define draw method outside of the initializer
    # Use blit to draw objects on top of background
    def draw(self, background):
        # Draw the image on a specific x/y coordinate
        background.blit(self.image, (self.x_pos, self.y_pos))


# Create a SUB-CLASS called player character - inherits all traits of parent object (GameObjects)
class PlayerCharacter(GameObjects):
    # set speed
    SPEED = 10
    #define initializer
    def __init__(self, image_path, x, y, width, height):
        # Use super() method to inherit from one class to another
        super().__init__(image_path, x, y, width, height) 

    def move(self, direction):
        #If keyboard is pressed up, move 10 pixels
        if direction[pygame.K_UP]:
            self.y_pos -= self.SPEED
            #If keyboard is pressed down, move down 10 pixels
        elif direction[pygame.K_DOWN]:
            self.y_pos += self.SPEED
            # If keyboard is pressed left, move left 10 pixels
        elif direction[pygame.K_LEFT]:
            self.x_pos -= self.SPEED
            # If keyboard is pressed right, move right 10 pixels
        elif direction[pygame.K_RIGHT]:
            self.x_pos += self.SPEED

# Create enemy character
class EnemyCharacter(GameObjects):
    # Give it a slower speed
    SPEED = 5

    #define initializer
    def __init__(self, image_path, x, y, width, height):
        # Use super() method to inherit from one class to another
        super().__init__(image_path, x, y, width, height) 

    # Enemy's only role is to move horizontally
    # Create move method - must know screen boundaries (width) - pass max_width as parameter
    def move (self, max_width):
        if self.x_pos <= 20: # stops 20 pixels before left-hand side of screen
            self.SPEED = abs(self.SPEED) # takes absolute value of SPEED - makes it positive - moves to right
        elif self.x_pos > max_width - (20 + self.width): # stop 20 pixels less than 800 also accounting for the enemy character's width
            self.SPEED = -abs(self.SPEED) #negates absolute value - moves it left
        # This moves the enemy character
        self.x_pos += self.SPEED 


             




# Create game object to invoke it - outside the Game class
new_game = Game('frogger_bkg.png', SCREEN_TITLE, SCREEN_WIDTH, SCREEN_HEIGHT) # pass those values into the class

# Run function
# will show exact position (coords) of your mouse
new_game.runGame() #will run the runGame method, which is part of the Game class


# NEXT STEPS AND CHALLENGES TO ADD
# Nxt have to add collision detection
# Create power up objects
# Move the treasure chest
# Make enemies move up/down
# Make the enemy follow the player
