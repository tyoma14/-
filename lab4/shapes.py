import math
from abc import ABC
from abc import abstractmethod
from tkinter import Canvas


class Shape(ABC):   # абстрактный класс
     
    # Объявляем абстрактные методы, которые нужно реализовать
    @abstractmethod
    def perimeter(self):
        pass

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def draw(self, canvas: Canvas):
        pass


class Rectangle(Shape):     # наследуемся от Shape
    
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
    # переопределяем методы
    def perimeter(self):
        return 2 * (self.width + self.height)

    def area(self):
        return self.width * self.height

    def draw(self, canvas: Canvas):
        x0 = 15
        y0 = 15
        canvas.create_rectangle(x0, y0, x0 + self.width, y0 + self.height)


class Triangle(Shape):
    
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    
    def perimeter(self):
        return self.a + self.b + self.c

    def area(self):
        p = self.perimeter() / 2
        return math.sqrt(p*(p-self.a)*(p-self.b)*(p-self.c))

    def draw(self, canvas: Canvas):
        h = 2 * self.area() / self.a
        x0 = 15
        y0 = 15 + h
        x1 = x0 + self.a
        y1 = y0
        x2 = x1 - self.b * math.sqrt(1 - (h/self.b)**2)
        y2 = y0 - h
        canvas.create_polygon(x0, y0, x1, y1, x2, y2, fill='white', outline='black')
