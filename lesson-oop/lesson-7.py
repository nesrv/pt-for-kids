# Урок 7: __repr__ — «техническое» описание объекта
#
# __repr__ — для программиста и отладки.
# Хороший repr можно скопировать и вставить в код.
# Если __str__ нет, print() использует __repr__.


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        # repr(a) → "Point(3, 5)" — похоже на вызов конструктора
        return f"Point({self.x}, {self.y})"

    def __str__(self):
        # для человека — короче и понятнее
        return f"({self.x}, {self.y})"


class Lamp:
    def __init__(self, name, x, y):
        self.name = name
        self.is_on = False
        self.position = Point(x, y)

    def __repr__(self):
        return f"Lamp({self.name!r}, {self.position.x}, {self.position.y}, is_on={self.is_on})"


a = Point(3, 5)
lamp = Lamp("Окно", 8, 1)

print("print(a):", a)           # вызывает __str__
print("repr(a):", repr(a))      # вызывает __repr__
print("repr(lamp):", repr(lamp))

# repr удобен в списках — там всегда __repr__
points = [Point(0, 0), Point(1, 2), Point(3, 4)]
print("Список точек:", points)

# попробуйте: добавьте __repr__ для Lamp с position через repr(self.position)
