# Решение задачи 2: строка + список
#
# Сначала проверяем тип: list → склеиваем элементы как строки.
# Иначе ведём себя как в задаче 1.


class Text:
    def __init__(self, value):
        self.value = str(value)

    def __str__(self):
        return self.value

    def __add__(self, other):
        if isinstance(other, list):
            extra = "".join(str(x) for x in other)
            return Text(self.value + extra)
        return Text(self.value + str(other))


# --- тесты ---

assert str(Text("abc") + ["d", "e", "f"]) == "abcdef"
assert str(Text("") + [1, 2, 3]) == "123"
assert str(Text("hi") + []) == "hi"

print("Задача 2 — решение OK")
