# Шаг 1: Класс Game — полотно (окно игры)
import pygame


# Класс Game — это «чертёж» всей игры.
# Из него мы потом создаём объект и запускаем игру.
class Game:
    WIDTH = 600   # ширина окна в пикселях
    HEIGHT = 400  # высота окна в пикселях

    # __init__ вызывается автоматически, когда пишем Game()
    def __init__(self):
        pygame.init()  # включаем библиотеку pygame
        # создаём окно — это наш «холст» для рисования
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("Змейка ООП — шаг 1")
        self.clock = pygame.time.Clock()  # помогает не торопить игру
        self.running = True  # пока True — игра работает

    # Слушаем, что нажал игрок (пока только закрытие окна)
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # нажали крестик
                self.running = False

    # Рисуем один кадр на экране
    def draw(self):
        self.screen.fill((0, 0, 0))  # заливаем фон чёрным

    # Главный цикл — повторяется, пока окно открыто
    def run(self):
        while self.running:
            self.handle_events()       # проверяем нажатия
            self.draw()                # рисуем кадр
            pygame.display.flip()      # показываем кадр на экране
            self.clock.tick(60)        # ждём до 60 кадров в секунду
        pygame.quit()


# Запускаем игру только если файл открыли напрямую (не импортировали)
if __name__ == "__main__":
    Game().run()
