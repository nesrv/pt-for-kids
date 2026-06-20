# Урок 8: __add__ — сложение объектов через +
#
# point_a + point_b создаёт новую точку.
# Старые точки не меняются — получаем новый объект.


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __add__(self, other):
        # other — вторая точка справа от +
        if not isinstance(other, Point):
            return NotImplemented
        return Point(self.x + other.x, self.y + other.y)


# «шаг» — смещение, тоже точка
step = Point(2, -1)
start = Point(3, 5)

# складываем координаты: (3+2, 5+(-1)) = (5, 4)
finish = start + step

print("Старт:", start)
print("Шаг:", step)
print("Финиш:", finish)

# можно складывать цепочкой
a = Point(1, 1)
b = Point(2, 3)
c = Point(-1, 2)
result = a + b + c
print("a + b + c =", result)

# попробуйте: Point(0, 0) + Point(10, 0) — куда попадём?
