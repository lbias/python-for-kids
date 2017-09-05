def hello():
    print('hello there')

from tkinter import *
tk = Tk()
btn = Button(tk, text="click me", command=hello)
btn.pack()

# wait for the user to close the window
tk.mainloop()
