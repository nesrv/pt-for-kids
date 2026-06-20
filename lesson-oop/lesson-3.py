# Урок 3: Класс Lamp — состояние и поведение
#
# Лампа «помнит», включена она или нет, и умеет переключаться.


class Lamp:
    def __init__(self, name):
        self.name = name
        self.is_on = False  # по умолчанию выключена

    def turn_on(self):
        self.is_on = True

    def turn_off(self):
        self.is_on = False

    def toggle(self):
        """Переключить: было вкл → стало выкл, и наоборот."""
        self.is_on = not self.is_on

    def status(self):
        state = "включена" if self.is_on else "выключена"
        return f"Лампа «{self.name}»: {state}"


lamp1 = Lamp("Потолочная")
lamp2 = Lamp("Настольная")

lamp1.turn_on()
print(lamp1.status())
print(lamp2.status())

lamp2.toggle()
print("После toggle:", lamp2.status())

# попробуйте: создайте lamp3, включите первую, выключите вторую
