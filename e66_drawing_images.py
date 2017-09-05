from tkinter import *

tk = Tk()
canvas = Canvas(tk, width=800, height=400)
canvas.pack()
myimage = PhotoImage(file='/Users/sam/ws/python-for-kids/test.gif')
canvas.create_image(0, 0, anchor=NW, image=myimage)

# wait for the user to close the window
tk.mainloop()
