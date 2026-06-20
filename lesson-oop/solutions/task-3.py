# Решение задачи 3: слово × число
#
# __mul__  — word * 3
# __rmul__ — 3 * word (число слева)


class Word:
    def __init__(self, text):
        self.text = str(text)

    def __str__(self):
        return self.text

    def __mul__(self, n):
        return Word(self.text * int(n))

    def __rmul__(self, n):
        return self * n


# --- тесты ---

assert str(Word("ля") * 3) == "ляляля"
assert str(Word("Ha") * 2) == "HaHa"
assert str(3 * Word("!")) == "!!!"
assert str(Word("x") * 1) == "x"
assert str(Word("x") * 0) == ""

print("Задача 3 — решение OK")
