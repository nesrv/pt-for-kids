# Задача 2: как сложить строку со списком?
#
# Цель: Text("abc") + ["d", "e"]  →  Text("abcde")
#
# Подсказка: if isinstance(other, list): ...


class Text:
    def __init__(self, value):
        self.value = str(value)

    def __str__(self):
        return self.value

    def __add__(self, other):
        # TODO: если other — список, склейте элементы как строки
        raise NotImplementedError("допишите __add__")


# --- тесты ---

assert str(Text("abc") + ["d", "e", "f"]) == "abcdef"
assert str(Text("") + [1, 2, 3]) == "123"
assert str(Text("hi") + []) == "hi"

print("Задача 2 решена!")
