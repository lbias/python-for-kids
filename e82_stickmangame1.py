from tkinter import *
import random
import time

# create class Game, which will be the main controller of the game
class Game:
    # initialize the game
    def __init__(self):
        # create the tk object
        self.tk = Tk()
        # set the window title
        self.tk.title("Mr. Stick Man Races for the Exit")
        # make the window fixed by calling function resizable
        self.tk.resizable(0, 0)
        # move the window in front of all other windows with function wm_attributes
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

# save object of the Game class as the variable g
g = Game()
# call mainloop to draw the screen
g.mainloop()
