# Задача 1 — решение через наследование от str
#
# Text — это «особая строка». Наследуемся от str и переопределяем __add__.
# У обычной str: "abc" + 5 → ошибка.
# У нашей Text: Text("abc") + 5 → Text("abc5")


class Text(str):
    """Строка, которую можно складывать с числом."""

    def __add__(self, other):
        # super().__add__(...) — вызов __add__ у базового класса str
        # str(other) — число превращаем в строку, как "13"
        return Text(super().__add__(str(other)))


# --- тесты ---

assert str(Text("Мне ") + 13) == "Мне 13"
assert str(Text("Год: ") + 2025) == "Год: 2025"
assert str(Text("x") + 0) == "x0"

# бонус: Text — это и str, и Text одновременно
t = Text("привет")
assert isinstance(t, str)
assert t + "!" == Text("привет!")

print("Задача 1 (наследование от str) — OK")
