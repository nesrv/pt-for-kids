# Урок 9: __mul__ — умножение объекта на число
#
# point * 3 — растягиваем вектор: координаты умножаются на 3.
# 2 * point тоже работает через __rmul__.


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __mul__(self, n):
        # point * 3
        if not isinstance(n, (int, float)):
            return NotImplemented
        return Point(self.x * n, self.y * n)

    def __rmul__(self, n):
        # 3 * point — число слева от *
        return self * n


step = Point(2, 1)

print("Один шаг:", step)
print("Три шага:", step * 3)
print("И так тоже:", 3 * step)

# полезно для «ускорения» движения
velocity = Point(1, 0)
fast = velocity * 5
print("Быстрое движение вправо:", fast)

# попробуйте: step * 0 — что получится?
