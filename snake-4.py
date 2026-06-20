# Шаг 4: Появление яблок
import pygame
import random

pygame.init()

WIDTH, HEIGHT = 600, 400
CELL = 20

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Змейка — шаг 4")

clock = pygame.time.Clock()

snake = [(WIDTH // 2, HEIGHT // 2)]
direction = (CELL, 0)

STEP = pygame.USEREVENT
pygame.time.set_timer(STEP, 150)


def spawn_apple():
    """Ставит яблоко в случайную клетку, где нет змейки."""
    while True:
        x = random.randint(0, (WIDTH - CELL) // CELL) * CELL
        y = random.randint(0, (HEIGHT - CELL) // CELL) * CELL
        if (x, y) not in snake:
            return (x, y)


apple = spawn_apple()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != (0, CELL):
                direction = (0, -CELL)
            elif event.key == pygame.K_DOWN and direction != (0, -CELL):
                direction = (0, CELL)
            elif event.key == pygame.K_LEFT and direction != (CELL, 0):
                direction = (-CELL, 0)
            elif event.key == pygame.K_RIGHT and direction != (-CELL, 0):
                direction = (CELL, 0)

        if event.type == STEP:
            head_x, head_y = snake[0]
            new_head = (head_x + direction[0], head_y + direction[1])
            snake = [new_head]

    screen.fill((0, 0, 0))

    for x, y in snake:
        pygame.draw.rect(screen, (0, 255, 0), (x, y, CELL, CELL))

    pygame.draw.rect(screen, (255, 0, 0), (*apple, CELL, CELL))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
