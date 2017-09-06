from tkinter import *
import random
import time

# create class Game, which will be the main controller of the game
class Game:
    # initialize the game with function __init__
    def __init__(self):
        # create the tk object
        self.tk = Tk()
        # set the window title
        self.tk.title("Mr. Stick Man Races for the Exit")
        # make the window fixed by calling function resizable
        self.tk.resizable(0, 0)
        # move the win in front of all other win with function wm_attributes
        self.tk.wm_attributes("-topmost", 1)
        # create the canvas
        self.canvas = Canvas(self.tk, width=500, height=500, highlightthickness=0)
        # call function pack of the canvas object
        self.canvas.pack()
        # call function update of the tk object
        self.tk.update()
        # create variable canvas_height to store the height of the canvas
        self.canvas_height = 500
        # create variable canvas_width to store the width of the canvas
        self.canvas_width = 500
        # create the variable bg which contains a PhotoImage object
        self.bg = PhotoImage(file="background.gif")
        # store the width of the image in the variables w
        w = self.bg.width()
        # store the height of the image in the variables h
        h = self.bg.height()
        # use for loop to calculate the columns across
        for x in range(0, 5):
            # use for loop to calculate the rows going down
            for y in range(0, 5):
                # x * w for how far across, y * h for how down to draw
                self.canvas.create_image(x * w, y * h, image=self.bg, anchor='nw')
        # create the variable sprites, which holds an empty list
        self.sprites = []
        # create the variable running, which contains the Boolean value True
        self.running = True

    # function mainloop for doing the animation
    def mainloop(self):
        # create a while loop that will run unitil the game win is closed
        while 1:
            # check if the variable running is equal to True
            if self.running == True:
                # if True, loop through any sprites in the list of sprites
                for sprite in self.sprites:
                    # call function move for each sprite
                    sprite.move()
                # force the tk object to redraw the screen and sleep for 0.01s
                self.tk.update_idletasks()
                self.tk.update()
                time.sleep(0.01)

# create class Coords to specify the position of sth on the game screen
# this class will store the position top-left(x1, y1), bottom-right(x2, y2) of any component of the game
class Coords:
    # function __init__ where we pass the four parameters
    def __init__(self, x1=0, y1=0, x2=0, y2=0):
        # each parameter is saved as an object variable of the same name
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

# to check sprites colliding horizontally
# co1, the first coordinate object
# co2, the second coordinate object
def within_x(co1, co2):
    # check if the leftmost position x1 of co1 is between leftmost and rithtmost of co2
    if (co1.x1 > co2.x1 and co1.x1 < co2.x2) \
            # check if rithtmost of co1 is between leftmost and rightmost of co2
            or (co1.x2 > co2.x1 and co1.x2 < co2.x2) \
            # check if leftmost of co2 is between leftmost and rightmost of co1
            or (co2.x1 > co1.x1 and co2.x1 < co1.x2) \
            # check if rightmost of co2 is between leftmost and rithtmost of co1
            or (co2.x2 > co1.x1 and co2.x2 < co1.x1):
        # return True if any of the above four cases happen
        return True
    else:
        # if none of the if statements match, go to else and return False
        return False

# to check sprites colliding vertically
def within_y(co1, co2):
    # check if topmost position y1 of co1 is between topmost and bottommost of co2
    if (co1.y1 > co2.y1 and co1.y1 < co2.y2) \
            # check if bottommost of co1 is between topmost and bottommost of co2
            or (co1.y2 > co2.y1 and co1.y2 < co2.y2) \
            # check if topmost of co2 is between topmost and bottommost of co1
            or (co2.y1 > co1.y1 and co2.y1 < co1.y2) \
            # check if bottommost of co2 is between topmost and bottommost of co1
            or (co2.y2 > co1.y1 and co2.y2 < co1.y1):
        # return True if any of the if statements match
        return True
    else:
        # return False is none of the if statements match
        return False

# check if the left-hand side of co1 has hit co2
def collided_left(co1, co2):
    # check if the two objects has crossed over vertically using function within_y
    if within_y(co1, co2):
        # check if leftmost of co1 has hit the position of co2
        if co1.x1 <= co2.x2 and co1.x1 >= co2.x1:
            return True
    return False

# check if the right-hand side of co1 has hit co2
def collided_right(co1, co2):
    # check if the two objects has crossed over vertically using function within_y
    if within_y(co1, co2):
        # check if rightmost of co1 has hit the position of co2
        if co1.x2 >= co2.x1 and co1.x2 <= co2.x2:
            return True
    return False

# check if the topmost position of co1 has hit co2
def collided_top(co1, co2):
    # check if the two objects has crossed over horizontally using function within_x
    if within_x(co1, co2):
        # check if topmost of co1 has hit the position of co2
        if co1.y1 <= co2.y2 and co1.y1 >= co2.y1:
             return True
    return False

# check if the bottommost position of co1 has hit co2
def collided_bottom(y, co1, co2):
    # check if the two objects has crossed over horizontally using function within_x
    if within_x(co1, co2):
        # add the value of y parameter to y2 position of co1, store the result in y_calc
        y_calc = co1.y2 + y
        # check if bottommost of co1 has hit the top of coordinate co2
        if y_calc >= co2.y1 and y_calc <= co2.y2:
            return True
    return False

# class Sprite for our game items Sprite
class Sprite:
    # any sprite can access the list of other sprites in the game with function __init__
    def __init__(self, game):
        # store parameter game as an object variable
        self.game = game
        # indicate the end of the game
        self.endgame = False
        # set coordinates to nothing
        self.coordinates = None
    # move the sprite
    def move(self):
        # do nothing in the parent class
        pass
    # return the sprite's current position on the screen
    def coords(self):
        # return the object variable coordinates
        return self.coordinates

# class PlatformSprite for platform objects, it is a child class of Sprite
class PlatformSprite(Sprite):
    # has seven parameters
    def __init__(self, game, photo_image, x, y, width, height):
        # call the __init__ of the parent class to have all the object variables from it
        Sprite.__init__(self, game)
        # save parameter photo_image as an object variable
        self.photo_image = photo_image
        # draw the image on screen with create_image
        self.image = game.canvas.create_image(x, y, image=self.photo_image, anchor='nw')
        # create a coordinates object containing the real location of the platform image on the screen
        self.coordinates = Coords(x, y, x + width, y + height)

# save object of the Game class as the variable g
g = Game()
# add a platform object
platform1 = PlatformSprite(g, PhotoImage(file="platform1.gif"), 0, 480, 100, 10)
# add object platform1 to the list of sprites in the game object
g.sprites.append(platform1)
# call mainloop to draw the screen
g.mainloop()
