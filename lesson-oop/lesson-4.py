# Урок 4: Lamp + Point — лампа стоит в точке
#
# Один объект может хранить другой объект внутри себя.


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def info(self):
        return f"({self.x}, {self.y})"


class Lamp:
    def __init__(self, name, x, y):
        self.name = name
        self.is_on = False
        # лампа «стоит» в точке — создаём объект Point внутри Lamp
        self.position = Point(x, y)

    def turn_on(self):
        self.is_on = True

    def turn_off(self):
        self.is_on = False

    def move_to(self, x, y):
        """Переставить лампу в новую точку."""
        self.position.x = x
        self.position.y = y

    def where(self):
        return f"Лампа «{self.name}» на месте {self.position.info()}"

    def describe(self):
        state = "горит" if self.is_on else "не горит"
        return f"{self.where()}, {state}"


desk = Lamp("Настольная", 2, 3)
window = Lamp("У окна", 8, 1)

desk.turn_on()
print(desk.describe())
print(window.describe())

desk.move_to(5, 5)
print("После move_to:", desk.where())

# попробуйте: лампа «У окна» в (8, 2), включить и вывести describe()
