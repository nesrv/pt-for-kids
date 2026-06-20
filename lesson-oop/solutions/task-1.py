# Решение задачи 1: строка + число
#
# __add__ вызывается при знаке +.
# Превращаем other в строку и возвращаем новый Text.


class Text:
    def __init__(self, value):
        self.value = str(value)

    def __str__(self):
        return self.value

    def __add__(self, other):
        return Text(self.value + str(other))


# --- тесты ---

assert str(Text("Мне ") + 13) == "Мне 13"
assert str(Text("Год: ") + 2025) == "Год: 2025"
assert str(Text("x") + 0) == "x0"

print("Задача 1 — решение OK")
