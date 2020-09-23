from math import ceil, sqrt, floor

class Shape:
    def __init__(self):
        raise NotImplementedError

    def area(self):
        raise NotImplementedError

    def env(self):
        raise NotImplementedError

    def draw(self):
        raise NotImplementedError

class Rectangle(Shape):
    def __init__(self, w: int, h: int):
        self.w = w
        self.h = h

    def area(self):
        return self.w * self.h

    def env(self):
        return 2 * (self.w + self.h)

    def draw(self):
        for _ in range(self.h):
            print('*' * self.w)

class Square(Rectangle):
    def __init__(self, a: int):
        super().__init__(a, a)

class Parallelogram(Shape):
    def __init__(self, a: int, b: int, h: int):
        self.h = h
        self.a = a
        self.b = b

    def area(self):
        return self.h * self.a

    def env(self):
        return 2 * (self.h + self.a)

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

rec = Rectangle(2, 4)

squ = Square(2)

par = Parallelogram(3, 4, 2).area()

rho = Rhombus(4, 2)

dia = Diamond(4)