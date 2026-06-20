# Задача 4: как сравнить две точки?
#
# Цель: Point(1, 2) == Point(1, 2)  →  True
#
# Подсказка: реализуйте __eq__(self, other)


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        # TODO: True если other — Point с теми же x и y
        raise NotImplementedError("допишите __eq__")


# --- тесты ---

assert Point(1, 2) == Point(1, 2)
assert not (Point(0, 0) == Point(1, 0))
assert not (Point(3, 4) == Point(3, 5))
assert Point(3, 4) != "точка"  # не ошибка, просто False

print("Задача 4 решена!")
