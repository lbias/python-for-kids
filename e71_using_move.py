from tkinter import *

tk = Tk()
canvas = Canvas(tk, width=400, height=400)
canvas.pack()
my_triangle = canvas.create_polygon(10, 10, 10, 60, 50, 35)
canvas.move(my_triangle, 5, 0)

# wait for the user to close the window
tk.mainloop()
