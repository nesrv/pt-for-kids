# Задача 3: как умножить «слово» на число?
#
# Цель: Word("ля") * 3  →  Word("ляляля")
#       3 * Word("!")   →  Word("!!!")
#
# Подсказка: __mul__ и __rmul__


class Word:
    def __init__(self, text):
        self.text = str(text)

    def __str__(self):
        return self.text

    def __mul__(self, n):
        # TODO: Word("а") * 3 → "aaa"
        raise NotImplementedError("допишите __mul__")

    def __rmul__(self, n):
        # TODO: 3 * Word("а") — число слева от *
        raise NotImplementedError("допишите __rmul__")


# --- тесты ---

assert str(Word("ля") * 3) == "ляляля"
assert str(Word("Ha") * 2) == "HaHa"
assert str(3 * Word("!")) == "!!!"
assert str(Word("x") * 1) == "x"
assert str(Word("x") * 0) == ""

print("Задача 3 решена!")
