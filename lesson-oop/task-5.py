# Задача 5: как проверить «есть ли в коробке?»
#
# Цель: "груша" in Box(["яблоко", "груша"])  →  True
#
# Подсказка: реализуйте __contains__(self, item)


class Box:
    def __init__(self, items):
        self.items = list(items)

    def __contains__(self, item):
        # TODO: True если item есть в self.items
        raise NotImplementedError("допишите __contains__")


# --- тесты ---

box = Box(["яблоко", "груша", "банан"])

assert "груша" in box
assert "яблоко" in box
assert "апельсин" not in box
assert 123 not in Box([1, 2, 3]) or 123 in Box([123])

empty = Box([])
assert "что угодно" not in empty

print("Задача 5 решена!")
