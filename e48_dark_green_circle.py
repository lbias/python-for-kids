import turtle

t = turtle.Pen()

def mycircle(red, green, blue):
    t.color(red, green, blue)
    t.begin_fill()
    t.circle(50)
    t.end_fill()

mycircle(0, 0.5, 0)
# wait for the user to close the window
turtle.mainloop()
