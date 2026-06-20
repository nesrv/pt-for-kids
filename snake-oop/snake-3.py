# Шаг 3: Управление с клавиатуры
import pygame


class Snake:
    CELL = 20
    COLOR = (0, 255, 0)

    def __init__(self, x, y):
        self.segments = [(x, y)]
        # direction — куда ползём: (20, 0) значит «вправо на 20 пикселей»
        self.direction = (self.CELL, 0)

    # Меняем направление по нажатой стрелке
    def handle_key(self, key):
        # нельзя развернуться на 180° — иначе змейка сразу врежется в себя
        if key == pygame.K_UP and self.direction != (0, self.CELL):
            self.direction = (0, -self.CELL)      # вверх
        elif key == pygame.K_DOWN and self.direction != (0, -self.CELL):
            self.direction = (0, self.CELL)       # вниз
        elif key == pygame.K_LEFT and self.direction != (self.CELL, 0):
            self.direction = (-self.CELL, 0)      # влево
        elif key == pygame.K_RIGHT and self.direction != (-self.CELL, 0):
            self.direction = (self.CELL, 0)       # вправо

    # Один шаг: ставим голову чуть дальше по направлению
    def move(self):
        head_x, head_y = self.segments[0]
        new_head = (head_x + self.direction[0], head_y + self.direction[1])
        self.segments = [new_head]

    def draw(self, screen):
        for x, y in self.segments:
            pygame.draw.rect(screen, self.COLOR, (x, y, self.CELL, self.CELL))


class Game:
    WIDTH = 600
    HEIGHT = 400
    STEP = pygame.USEREVENT  # своё событие «пора сделать шаг»

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("Змейка ООП — шаг 3")
        self.clock = pygame.time.Clock()
        self.running = True
        self.snake = Snake(self.WIDTH // 2, self.HEIGHT // 2)
        # каждые 350 мс pygame пришлёт событие STEP
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

    def run(self):
        while self.running:
            self.handle_events()
            self.draw()
            pygame.display.flip()
            self.clock.tick(60)
        pygame.quit()


if __name__ == "__main__":
    Game().run()
