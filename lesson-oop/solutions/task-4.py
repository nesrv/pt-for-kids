# Решение задачи 4: сравнение точек
#
# __eq__ вызывается при ==.
# Если other не Point — возвращаем False (не ошибку!).


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        if not isinstance(other, Point):
            return False
        return self.x == other.x and self.y == other.y


# --- тесты ---

assert Point(1, 2) == Point(1, 2)
assert not (Point(0, 0) == Point(1, 0))
assert not (Point(3, 4) == Point(3, 5))
assert Point(3, 4) != "точка"

print("Задача 4 — решение OK")
