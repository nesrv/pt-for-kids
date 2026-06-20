# Урок 5: Room — комната с несколькими лампами
#
# Класс Room управляет списком объектов Lamp.


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Lamp:
    def __init__(self, name, x, y):
        self.name = name
        self.is_on = False
        self.position = Point(x, y)

    def turn_on(self):
        self.is_on = True

    def turn_off(self):
        self.is_on = False

    def distance_to(self, x, y):
        """Расстояние от лампы до точки (x, y) — упрощённо, без корня."""
        dx = self.position.x - x
        dy = self.position.y - y
        return dx * dx + dy * dy  # чем меньше число, тем ближе


class Room:
    def __init__(self, name):
        self.name = name
        self.lamps = []  # список ламп в комнате

    def add_lamp(self, lamp):
        self.lamps.append(lamp)

    def turn_all_on(self):
        for lamp in self.lamps:
            lamp.turn_on()

    def turn_all_off(self):
        for lamp in self.lamps:
            lamp.turn_off()

    def count_on(self):
        count = 0
        for lamp in self.lamps:
            if lamp.is_on:
                count += 1
        return count

    def nearest_lamp(self, x, y):
        """Лампа, ближайшая к точке (x, y)."""
        best = self.lamps[0]
        best_dist = best.distance_to(x, y)
        for lamp in self.lamps[1:]:
            dist = lamp.distance_to(x, y)
            if dist < best_dist:
                best = lamp
                best_dist = dist
        return best

    def report(self):
        print(f"Комната «{self.name}» — ламп: {len(self.lamps)}, горит: {self.count_on()}")
        for lamp in self.lamps:
            state = "ON" if lamp.is_on else "OFF"
            print(f"  {lamp.name} ({lamp.position.x}, {lamp.position.y}) — {state}")


# --- программа ---

room = Room("Класс")

room.add_lamp(Lamp("Потолок", 5, 5))
room.add_lamp(Lamp("Доска", 0, 3))
room.add_lamp(Lamp("Окно", 9, 1))

room.report()

print()
room.turn_all_on()
print("После turn_all_on:")
room.report()

near = room.nearest_lamp(0, 0)
print(f"\nБлиже всего к (0, 0): «{near.name}»")

# попробуйте: добавьте свою лампу, turn_all_off(), снова report()
