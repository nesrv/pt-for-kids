# Урок 10: @staticmethod — метод без self
#
# Обычный метод: нужен объект → lamp.turn_on()
# Статический: вызываем от класса → Point.origin()
# Удобен для «помощников», которым не нужен конкретный объект.


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

    @staticmethod
    def origin():
        """Фабрика: точка в начале координат."""
        return Point(0, 0)

    @staticmethod
    def from_tuple(pair):
        """Создать точку из кортежа (x, y)."""
        x, y = pair
        return Point(x, y)

    @staticmethod
    def distance(a, b):
        """Расстояние между двумя точками (упрощённо, без sqrt)."""
        dx = a.x - b.x
        dy = a.y - b.y
        return dx * dx + dy * dy


class Lamp:
    MAX_BRIGHTNESS = 100  # константа класса — общая для всех ламп

    def __init__(self, name, x, y):
        self.name = name
        self.position = Point(x, y)

    @staticmethod
    def is_valid_name(name):
        """Проверка имени — не нужен конкретный объект lamp."""
        return len(name) > 0 and not name.isspace()


# --- вызываем без создания объекта ---

zero = Point.origin()
print("Начало координат:", zero)

p = Point.from_tuple((4, 7))
print("Из кортежа:", p)

a = Point(0, 0)
b = Point(3, 4)
print("distance(a, b):", Point.distance(a, b))

print("Имя «Окно» подходит?", Lamp.is_valid_name("Окно"))
print("Пустое имя подходит?", Lamp.is_valid_name("   "))
print("Макс. яркость:", Lamp.MAX_BRIGHTNESS)

# попробуйте: @staticmethod mid(a, b) — точка посередине между a и b
