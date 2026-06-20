# Шаг 5: Хвост и рост при съедании яблока
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

    # Двигаем голову и проверяем, не проиграли ли мы
    # Возвращает: "ok", "wall" (стена) или "self" (удар в себя)
    def move(self, width, height):
        head_x, head_y = self.segments[0]
        new_head = (head_x + self.direction[0], head_y + self.direction[1])

        # голова вышла за край окна?
        if (
            new_head[0] < 0
            or new_head[0] >= width
            or new_head[1] < 0
            or new_head[1] >= height
        ):
            return "wall"

        # голова попала на своё тело?
        if new_head in self.segments:
            return "self"

        # добавляем новую голову в начало списка
        self.segments.insert(0, new_head)
        return "ok"

    # Убираем последний сегмент — хвост «следует» за головой
    def trim_tail(self):
        self.segments.pop()

    # Проверяем: голова на том же месте, что и яблоко?
    def ate(self, apple_pos):
        return self.segments[0] == apple_pos

    def draw(self, screen):
        for x, y in self.segments:
            pygame.draw.rect(screen, self.COLOR, (x, y, self.CELL, self.CELL))


class Apple:
    CELL = 20
    COLOR = (255, 0, 0)

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.pos = (0, 0)

    def spawn(self, snake):
        while True:
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
        pygame.display.set_caption("Змейка ООП — шаг 5")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont("arial", 28)  # шрифт для текста
        self.running = True
        self.game_over = False  # True — игра закончилась
        self.snake = Snake(self.WIDTH // 2, self.HEIGHT // 2)
        self.apple = Apple(self.WIDTH, self.HEIGHT)
        self.apple.spawn(self.snake)
        pygame.time.set_timer(self.STEP, 350)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif not self.game_over and event.type == pygame.KEYDOWN:
                self.snake.handle_key(event.key)
            elif not self.game_over and event.type == self.STEP:
                self.step_snake()

    # Один игровой шаг: движение, рост или проигрыш
    def step_snake(self):
        result = self.snake.move(self.WIDTH, self.HEIGHT)
        if result != "ok":
            self.game_over = True
            return

        if self.snake.ate(self.apple.pos):
            # съели яблоко — хвост не убираем, змейка длиннее
            self.apple.spawn(self.snake)
        else:
            self.snake.trim_tail()

    def draw(self):
        self.screen.fill((0, 0, 0))
        self.snake.draw(self.screen)

        if not self.game_over:
            self.apple.draw(self.screen)
        else:
            # белый текст по центру экрана
            text = self.font.render("Игра окончена! Закрой окно.", True, (255, 255, 255))
            self.screen.blit(text, (self.WIDTH // 2 - text.get_width() // 2, self.HEIGHT // 2))

    def run(self):
        while self.running:
            self.handle_events()
            self.draw()
            pygame.display.flip()
            self.clock.tick(60)
        pygame.quit()


if __name__ == "__main__":
    Game().run()
