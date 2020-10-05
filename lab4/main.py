from tkinter import *
from lab4.shapes import *


def test():
    r = Rectangle(100, 70)
    t = Triangle(60, 80, 90)
    shapes_list = [r, t]
    root = Tk()
    canvas = Canvas(root, width=400, height=400, bg='white')
    for shape in shapes_list:
        print(shape.perimeter())
        print(shape.area())
        shape.draw(canvas)
    canvas.pack()
    root.mainloop()


test()
