from tkinter import *
from random import randint
import math

class Ball:
    def __init__(self, canvas, x1, y1, x2, y2, speed, color):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.speed = speed
        self.dv = True
        self.canvas = canvas
        self.ball = canvas.create_oval(self.x1, self.y1, self.x2, self.y2, fill=color)

    def move_ball(self):
        deltax = randint(-self.speed,self.speed)
        deltay = randint(-self.speed,self.speed)
        self.canvas.move(self.ball, deltax, deltay)
        self.canvas.after(50, self.move_ball)

root = Tk()
root.title("Moleculs")
root.resizable(False,False)
canvas = Canvas(root, width = 500, height = 500)
canvas.pack()

a = []
b = []
for i in range(250):
    size1 = randint(5,20)
    size2 = randint(5,20)
    u = randint(200,400)
    f = randint(200,400)
    a.append(Ball(canvas, u, u, u+size1, u+size1, 25-size1, "blue"))
    b.append(Ball(canvas, f, f, f+size2, f+size2, 25-size2, "red"))
for i in a:
    i.move_ball()
for i in b:
    i.move_ball()

root.mainloop()
