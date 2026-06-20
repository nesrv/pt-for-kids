# Задача 1: как сложить строку с числом?
#
# Цель: Text("Мне ") + 13  →  Text("Мне 13")
#
# Подсказка: реализуйте __add__(self, other)


class Text:
    def __init__(self, value):
        self.value = str(value)

    def __str__(self):
        return self.value

    def __add__(self, other):
        # TODO: верните новый Text, склеив self.value и other (other → str)
        raise NotImplementedError("допишите __add__")


# --- тесты (не меняйте) ---

assert str(Text("Мне ") + 13) == "Мне 13"
assert str(Text("Год: ") + 2025) == "Год: 2025"
assert str(Text("x") + 0) == "x0"

print("Задача 1 решена!")
