# Решение задачи 5: «есть ли в коробке?»
#
# __contains__ вызывается при операторе in.
# "груша" in box  →  box.__contains__("груша")


class Box:
    def __init__(self, items):
        self.items = list(items)

    def __contains__(self, item):
        return item in self.items


# --- тесты ---

box = Box(["яблоко", "груша", "банан"])

assert "груша" in box
assert "яблоко" in box
assert "апельсин" not in box
assert 123 in Box([123])
assert "что угодно" not in Box([])

print("Задача 5 — решение OK")
