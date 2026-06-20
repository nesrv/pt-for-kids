# Шаг 4: Класс Apple — появление яблок
import pygame
import random


class Snake:
    CELL = 20
    COLOR = (0, 255, 0)

    def __init__(self, x, y):
        self.segments = [(x, y)]
        self.direction = (self.CELL, 0)

    def handle_key(self, key):
        if key == pygame.K_UP and self.direction != (0, self.CELL):
            self.direction = (0, -self.CELL)
        elif key == pygame.K_DOWN and self.direction != (0, -self.CELL):
            self.direction = (0, self.CELL)
        elif key == pygame.K_LEFT and self.direction != (self.CELL, 0):
            self.direction = (-self.CELL, 0)
        elif key == pygame.K_RIGHT and self.direction != (-self.CELL, 0):
            self.direction = (self.CELL, 0)

    def move(self):
        head_x, head_y = self.segments[0]
        new_head = (head_x + self.direction[0], head_y + self.direction[1])
        self.segments = [new_head]

    def draw(self, screen):
        for x, y in self.segments:
            pygame.draw.rect(screen, self.COLOR, (x, y, self.CELL, self.CELL))


# Класс Apple — красное яблоко на поле
class Apple:
    CELL = 20
    COLOR = (255, 0, 0)  # красный

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.pos = (0, 0)  # координаты яблока (x, y)

    # Ставим яблоко в случайное место, но не на змейку
    def spawn(self, snake):
        while True:
            # random.randint даёт случайное число клеток, * CELL — в пиксели
            x = random.randint(0, (self.width - self.CELL) // self.CELL) * self.CELL
            y = random.randint(0, (self.height - self.CELL) // self.CELL) * self.CELL
            if (x, y) not in snake.segments:
                self.pos = (x, y)
                return

    def draw(self, screen):
        pygame.draw.rect(screen, self.COLOR, (*self.pos, self.CELL, self.CELL))


class Game:
    WIDTH = 600
    HEIGHT = 400
    STEP = pygame.USEREVENT

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("Змейка ООП — шаг 4")
        self.clock = pygame.time.Clock()
        self.running = True
        self.snake = Snake(self.WIDTH // 2, self.HEIGHT // 2)
        self.apple = Apple(self.WIDTH, self.HEIGHT)
        self.apple.spawn(self.snake)  # первое яблоко
        pygame.time.set_timer(self.STEP, 350)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                self.snake.handle_key(event.key)
            elif event.type == self.STEP:
                self.snake.move()

    def draw(self):
        self.screen.fill((0, 0, 0))
        self.snake.draw(self.screen)
        self.apple.draw(self.screen)

    def run(self):
        while self.running:
            self.handle_events()
            self.draw()
            pygame.display.flip()
            self.clock.tick(60)
        pygame.quit()


if __name__ == "__main__":
    Game().run()
