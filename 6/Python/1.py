from math import ceil, sqrt, floor
from abc import ABC, abstractmethod


class Shape(ABC):
    def __init__(self):
        raise NotImplementedError
    
    @abstractmethod
    def area(self):
        """Returns the area"""

    @abstractmethod
    def env(self):
        """Returns the Enviroment of the shape"""

    @abstractmethod
    def draw(self):
        """Draw the shape"""
    
    @staticmethod
    def concat_area(li: list):
        area = 0
        for rec in li:
            if type(rec) == Rectangle:
                area += rec.area
            else:
                raise TypeError
        return area


class Rectangle(Shape):
    def __init__(self, w: int, h: int):
        self.w = w
        self.h = h

    @property
    def area(self):
        return self.w * self.h

    @property
    def env(self):
        return 2 * (self.w + self.h)

    def draw(self):
        for _ in range(self.h):
            print('*' * self.w)


class Square(Rectangle):
    def __init__(self, a: int):
        super().__init__(a, a)

    @staticmethod
    def draw_concat(l):
        for i in range(max(l)):
            for j in l:
                if type(j) == int:
                    if j - i > 0:
                        print('*' * j, end = '')
                    else:
                        print(' ' * j, end = '')
                else:
                    raise TypeError
            print()


class Parallelogram(Shape):
    def __init__(self, a: int, b: int, h: int):
        self.h = h
        self.a = a
        self.b = b

    @property
    def area(self):
        return self.h * self.a

    @property
    def env(self):
        return 2 * (self.b + self.a)

    def draw(self):
        for i in range(self.h - 1, -1, -1):
            print(i * (int(sqrt(self.b ** 2 - self.h ** 2)) // self.h) * ' ' + self.a * '*')

# dar lozi farz shode ke hame azlaa ba ham barabar hastand taa beshavad shekle on raa keshid
class Rhombus(Parallelogram):
    def __init__(self, a: int, h: int):
        super().__init__(a, a, h)


class Diamond(Square, Rhombus):
    def __init__(self, a):
        Square.__init__(self, a)

    def draw(self):
        n = self.w * 1.7
        n = ceil(n) if ceil(n) % 2 == 1 else floor(n)

        for i in range(1, n + 1):
            i = i - (n // 2 + 1)
            if i < 0:
                i = -i
            print(' ' * i + '*' * (n - i * 2))

Square.concat_area([3,5,10,9,10])