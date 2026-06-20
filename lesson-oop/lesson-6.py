# Урок 6: __str__ — красивый вывод через print()
#
# __str__ вызывается, когда пишем print(объект).
# Объект сам решает, как выглядеть «для человека».


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        # print(point) покажет эту строку
        return f"Точка ({self.x}, {self.y})"


class Lamp:
    def __init__(self, name, x, y):
        self.name = name
        self.is_on = False
        self.position = Point(x, y)

    def __str__(self):
        state = "включена" if self.is_on else "выключена"
        return f"Лампа «{self.name}» на {self.position}, {state}"


a = Point(3, 5)
lamp = Lamp("Настольная", 2, 4)
lamp.is_on = True

# раньше print(a) показывал бы что-то вроде <Point object at 0x...>
print(a)
print(lamp)

# str() делает то же самое, что и print внутри
text = str(a)
print("Строка:", text)

# попробуйте: добавьте __str__ в класс Room из урока 5
