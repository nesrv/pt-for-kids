# Шаг 2: Класс Snake — голова змейки
import pygame


# Класс Snake — всё про змейку: где она и как её нарисовать
class Snake:
    CELL = 20              # размер одного квадратика (клетки)
    COLOR = (0, 255, 0)    # зелёный цвет (R, G, B)

    def __init__(self, x, y):
        # segments — список частей тела; пока только голова
        self.segments = [(x, y)]

    # Рисуем каждый сегмент змейки зелёным квадратом
    def draw(self, screen):
        for x, y in self.segments:
            pygame.draw.rect(screen, self.COLOR, (x, y, self.CELL, self.CELL))


class Game:
    WIDTH = 600
    HEIGHT = 400

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("Змейка ООП — шаг 2")
        self.clock = pygame.time.Clock()
        self.running = True
        # создаём змейку в центре экрана
        self.snake = Snake(self.WIDTH // 2, self.HEIGHT // 2)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def draw(self):
        self.screen.fill((0, 0, 0))
        # змейка сама знает, как себя рисовать
        self.snake.draw(self.screen)

    def run(self):
        while self.running:
            self.handle_events()
            self.draw()
            pygame.display.flip()
            self.clock.tick(60)
        pygame.quit()


if __name__ == "__main__":
    Game().run()
