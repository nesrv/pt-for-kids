# Урок 2: Методы — что умеет делать точка
#
# Метод — функция внутри класса. Вызываем так: point.move(1, 2)


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, dx, dy):
        """Сдвигаем точку на dx по X и на dy по Y."""
        self.x += dx
        self.y += dy

    def info(self):
        """Возвращаем строку с координатами."""
        return f"Точка ({self.x}, {self.y})"


a = Point(3, 5)
print(a.info())

a.move(2, -1)  # сдвиг вправо на 2, вниз на 1
print("После move(2, -1):", a.info())

a.move(1, 1)
print("Ещё один шаг:", a.info())

# попробуйте сами — метод reset(), который ставит точку в (0, 0):
# def reset(self):
#     self.x = 0
#     self.y = 0
