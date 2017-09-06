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
    # check if the leftmost position x1 of co1 is between leftmost and rithtmost of co2.
    # check if rithtmost of co1 is between leftmost and rightmost of co2.
    # check if leftmost of co2 is between leftmost and rightmost of co1.
    # check if rightmost of co2 is between leftmost and rithtmost of co1.
    if (co1.x1 > co2.x1 and co1.x1 < co2.x2) \
            or (co1.x2 > co2.x1 and co1.x2 < co2.x2) \
            or (co2.x1 > co1.x1 and co2.x1 < co1.x2) \
            or (co2.x2 > co1.x1 and co2.x2 < co1.x1):
        # return True if any of the above four cases happen
        return True
    else:
        # if none of the if statements match, go to else and return False
        return False

# to check sprites colliding vertically
def within_y(co1, co2):
    # check if topmost position y1 of co1 is between topmost and bottommost of co2
    # check if bottommost of co1 is between topmost and bottommost of co2
    # check if topmost of co2 is between topmost and bottommost of co1
    # check if bottommost of co2 is between topmost and bottommost of co1
    if (co1.y1 > co2.y1 and co1.y1 < co2.y2) \
            or (co1.y2 > co2.y1 and co1.y2 < co2.y2) \
            or (co2.y1 > co1.y1 and co2.y1 < co1.y2) \
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

# the main character of the game, Mr. Stick Man
class StickFigureSprite(Sprite):
    # initialize the stick figure
    def __init__(self, game):
        # call the __init__ of the parent class Sprite
        Sprite.__init__(self, game)
        # create object variables images_left containing a image list
        self.images_left = [
            PhotoImage(file="stick-L1.gif"),
            PhotoImage(file="stick-L2.gif"),
            PhotoImage(file="stick-L3.gif")
        ]
        # create object variables images_right containing a image list
        self.images_right = [
            PhotoImage(file="stick-R1.gif"),
            PhotoImage(file="stick-R2.gif"),
            PhotoImage(file="stick-R3.gif")
        ]
        # draw the first image with function create_image
        self.image = game.canvas.create_image(200, 470, image=self.images_left[0], anchor='nw')
        # store the amount adding to horizontal coordinates when the stick figure moving around the screen
        self.x = -2
        # store the amount adding to vertical coordinates when the stick figure moving around the screen
        self.y = 0
        # store the image's index position as currently displayed on the screen
        self.current_image = 0
        # the number to added to the index position of current_image to get the next position
        self.current_image_add = 1
        # a counter to use for the stick figure jumping
        self.jump_count = 0
        # store the current time using the fuction time of module time
        self.last_time = time.time()
        # set the coordinates object variable to an object of the class Coords
        self.coordinates = Coords()
        # bundle <KeyPress-Left> to the function turn_left to make the stick figure move
        game.canvas.bind_all('<KeyPress-Left>', self.turn_left)
        # bundle <KeyPress-Right> to the function turn_right to make the stick figure move
        game.canvas.bind_all('<KeyPress-Right>', self.turn_right)
        # bundle <space> to the function jump to make the stick figure move
        game.canvas.bind_all('<space>', self.jump)

    # when press the left arrow key, passes an object evt with info what the player dis as a parameter
    def turn_left(self, evt):
        # if the value of y is 0, set x to -2 to run left
        if self.y == 0:
            self.x = -2

    # when press the right arrow key, passes an object evt with info what the player dis as a parameter
    def turn_right(self, evt):
        # if the value y is 0, set x to 2 to run right
        if self.y == 0:
            self.x = 2

    # when press the space key, passes an object evt with info what the player dis as a parameter
    def jump(self, evt):
        # if the value y is 0, the figure is not jumping, set y to -4 to move him up the screen
        if self.y == 0:
            self.y = -4
            # use jump_count to make sure the sick figure doesn't keep jumping forever
            self.jump_count = 0

    # check for movement and change the image accordingly
    def animate(self):
        # check if the stick figure is moving and not jumping
        if self.x != 0 and self.y == 0:
            # calculate the amount of time since the animate function was last called
            if time.time() - self.last_time > 0.1:
                # if the amount greater than o.1s, set the variable last_time to the current time
                self.last_time = time.time()
                # add value of current_image_add to the current_image which store the index position of the currently displayed image
                self.current_image += self.current_image_add
                # check if the value of index position in current_image is greater than or equal to 2
                if self.current_image >= 2:
                    # if so, change the value of current_image_add to -1
                    self.current_image_add = -1
                # check if the value of index position in current_image is less than or equal to 0
                if self.current_image <= 0:
                    # if so, change the value of current_image_add to 1, start counting up again
                    self.current_image_add = 1
        # if x is less than 0, the sitck figure is moving left
        if self.x < 0:
            # check if y is not equal to 0, meaning jumping
            if self.y != 0:
                # use function itemconfig to change the displayed image to the last image in list of left-facing iamges at images_left[2]
                self.game.canvas.itemconfig(self.image, image=self.images_left[2])
            # if not jumping
            else:
                # change the displayed image to whatever index position is in the variable current_image
                self.game.canvas.itemconfig(self.image, image=self.images_left[self.current_image])
        # x is greater than 0, the stick figure is moving right
        elif self.x > 0:
            # check if y is not equal to 0, meaning jumping
            if self.y != 0:
                # use function itemconfig to change the displayed image to the last image in list of right-facing iamges at images_right[2]
                self.game.canvas.itemconfig(self.image, image=self.images_right[2])
            # if not jumping
            else:
                # change the displayed image to whatever index position is in the variable current_image
                self.game.canvas.itemconfig(self.image, image=self.images_right[self.current_image])

    # determine where the stick figure is
    def coords(self):
        # use function coords of variable canvase to return the postions of the current image
        xy = list(self.game.canvas.coords(self.image))
        # top-left x position stored as the x1 variable of coordinates
        self.coordinates.x1 = xy[0]
        # top-left y position stored as the y1 variable of coordinates
        self.coordinates.y1 = xy[1]
        # stick figure image size w27 by h30, bottom-right x position plus 27 stored as the x2 variable of coordinates
        self.coordinates.x2 = xy[0] + 27
        # bottom-right y position plus 30 stored as the y2 variable of coordinates
        self.coordinates.y2 = xy[1] + 30
        # return the object variable coordinates
        return self.coordinates

    # move the game character around the screen
    def move(self):
        # call function animate which changes the currently displayed image if necessary
        self.animate()
        # check if y is less than 0, meaning jumping
        if self.y < 0:
            # add 1 to jump_count
            self.jump_count += 1
            # check if jump_count is bigger than 20
            if self.jump_count > 20:
                # change y to 4 to start the stick figure falling again
                self.y = 4
       # check if y is greater than 0, meaning falling
        if self.y > 0:
            # subtract 1 from jump_count because once counting up to 20, need to count back down again
            self.jump_count -= 1
        # call function coords, determine where the character is on the screen and store its result in variable co
        co = self.coords()
        # create left to check if the character hits left
        left = True
        # create right to check if the character hits right
        right = True
        # create top to check if the character hits top
        top = True
        # create bottom to check if the character hits bottom
        bottom = True
        # create falling to check if the character is falling
        falling = True

        # if falling, and y2 position is greater than or equal to the canvas_height of the object game
        if self.y > 0 and co.y2 >= self.game.canvas_height:
            # stop the stick figure from falling, set value of y to 0
            self.y = 0
            # set the bottom variable to False, meaning no longer to check if the figure has hit the bottom
            bottom = False
        # if jumping, and y1 position is less than or equal to 0, meaning hits the top of the canvas
        elif self.y < 0 and co.y1 <= 0:
            # set value of y to 0 to stop the movement
            self.y = 0
            # set top variable to False, meaning no longer need to check if the figure has hit the top
            top = False

        # if runing to the right, and hitting the right-hand side of the screen
        if self.x > 0 and co.x2 >= self.game.canvas_width:
            # set value of x to 0 to stop the stick figure from running
            self.x = 0
            # set the right variable to False, meaning no longer need to check if the figure has hit the right
            right = False
        # if running to the left, and hitting the left-hand side of the screen
        elif self.x < 0 and co.x1 <= 0:
            # set value of x to 0 to stop the stick figure from running
            self.x = 0
            # set the left variable to False , meaning no longer to check if the figure has hit the left
            left = False

        # loop through the list sprites, assigning each one in turn to the variable sprite
        for sprite in self.game.sprites:
            # if the sprite is the same as self, no need to determine colliding
            if sprite == self:
                # continue to jump to the next sprite in the list
                continue
            # get the coordinates of the new sprite, store the result in the variable sprite_co
            sprite_co = sprite.coords()
            # has not hit the top, and jumping, and the top of stick figure has collided with the sprite from the list
            if top and self.y < 0 and collided_top(co, sprite_co):
                # start falling back down, reverse the value of y
                self.y = -self.y
                # set variable top to False, meaning no need to check for hitting the top
                top = False

            # has not hit the bottom, and falling, and the bottom of stick figure has collided with the sprite from the list
            if bottom and self.y > 0 and collided_bottom(self.y, co, sprite_co):
                # get amount the stick figure should drop in order to land properly on the top of the platform
                self.y = sprite_co.y1 - co.y2
                # in case the stick figure fly back up again, check if value of y is less than 0
                if self.y < 0:
                    # set value of y to 0
                    self.y = 0
                # set variable bottom to False, meaning no need to check for hitting the bottom
                bottom = False
                # set variable top to False, meaning no need to check for hitting the top
                top = False

            # has not hit the bottom, and need to check if should be falling, and not falling, and bottom of sprite hasn't hit the bottom, and hit the top
            if bottom and falling and self.y == 0 and co.y2 < self.game.canvas_height and collided_bottom(1, co, sprite_co):
                # set the falling variable to False, meaning no need to check for falling
                falling = False

            # has not hit the left, and moving to the left, and has collided with a sprite
            if left and self.x < 0 and collided_left(co, sprite_co):
                # make the stick figure stop running
                self.x = 0
                # no need to check for hitting left of the screen
                left = False

            # has not hit the right, and moving to the right, and has collided with a sprite
            if right and self.x > 0 and collided_right(co, sprite_co):
                # make the stick figure stop running
                self.x = 0
                # no need to check for hitting right of the screen
                right = False

        # check if both falling and bottom variable are set to True, and check if should be falling, and bottom of sprite hasn't hit the bottom
        if falling and bottom and self.y == 0 and co.y2 < self.game.canvas_height:
            # set y to 4 to make the stick figure run off the end of any platform
            self.y = 4
        # move the image across the screen, according to the value of x, y
        self.game.canvas.move(self.image, self.x, self.y)

# save object of the Game class as the variable g
g = Game()
# add a bunch of platform objects with different x and y positions
platform1 = PlatformSprite(g, PhotoImage(file="platform1.gif"), 0, 480, 100, 10)
platform2 = PlatformSprite(g, PhotoImage(file="platform1.gif"), 150, 440, 100, 10)
platform3 = PlatformSprite(g, PhotoImage(file="platform1.gif"), 300, 400, 100, 10)
platform4 = PlatformSprite(g, PhotoImage(file="platform1.gif"), 300, 160, 100, 10)
platform5 = PlatformSprite(g, PhotoImage(file="platform2.gif"), 175, 350, 66, 10)
platform6 = PlatformSprite(g, PhotoImage(file="platform2.gif"), 50, 300, 66, 10)
platform7 = PlatformSprite(g, PhotoImage(file="platform2.gif"), 170, 120, 66, 10)
platform8 = PlatformSprite(g, PhotoImage(file="platform2.gif"), 45, 60, 66, 10)
platform9 = PlatformSprite(g, PhotoImage(file="platform3.gif"), 170, 250, 32, 10)
platform10 = PlatformSprite(g, PhotoImage(file="platform3.gif"), 230, 200, 32, 10)
# add object platform1~10 to the list of sprites in the game object
g.sprites.append(platform1)
g.sprites.append(platform2)
g.sprites.append(platform3)
g.sprites.append(platform4)
g.sprites.append(platform5)
g.sprites.append(platform6)
g.sprites.append(platform7)
g.sprites.append(platform8)
g.sprites.append(platform9)
g.sprites.append(platform10)
# create a StickFigureSprite object and set it equal to the variable sf
sf = StickFigureSprite(g)
# add variable sf to the list of sprites stored in the game object
g.sprites.append(sf)
# call mainloop to draw the screen
g.mainloop()
