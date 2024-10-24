# Import pygame library
#Docs are at https://pygame.org/docs/
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
        # Create a while loop so that the game is still running & updating until the game is over
        while not isGameOver:
            for event in pygame.event.get():  # for each event happening on screen
                # did user press quit
                if event.type == pygame.QUIT:
                    isGameOver = True #if so, closes game screen
                print(event)

            #Update display
            pygame.display.update()
            # Update the display 60 frames/second
            clock.tick(TICK_RATE)

        #Close program if the game is over - set it outside the isGameOver loop
        pygame.quit()
        quit() # stops script execution


# Create game object to invoke it - outside the Game class
new_game = Game('frogger_bkg.png', SCREEN_TITLE, SCREEN_WIDTH, SCREEN_HEIGHT) # pass those values into the class

# Run function
# will show exact position (coords) of your mouse
new_game.runGame() #will run the runGame method, which is part of the Game class

#When placing things, target desired coordinates 