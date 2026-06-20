# Шаг 3: Управление с клавиатуры
import pygame

pygame.init()

WIDTH, HEIGHT = 600, 400
CELL = 20

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Змейка — шаг 3")

clock = pygame.time.Clock()

snake = [(WIDTH // 2, HEIGHT // 2)]
direction = (CELL, 0)  # (20, 0) — движение вправо на 20 пикселей за шаг

# STEP — наше событие «пора сделать шаг змейки»
STEP = pygame.USEREVENT
pygame.time.set_timer(STEP, 550)  # каждые 550 мс

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # KEYDOWN — клавиша нажата (не отпущена)
        if event.type == pygame.KEYDOWN:
            # нельзя развернуться на 180°, иначе змейка врежется в себя
            if event.key == pygame.K_UP and direction != (0, CELL):
                direction = (0, -CELL)      # вверх
            elif event.key == pygame.K_DOWN and direction != (0, -CELL):
                direction = (0, CELL)       # вниз
            elif event.key == pygame.K_LEFT and direction != (CELL, 0):
                direction = (-CELL, 0)      # влево
            elif event.key == pygame.K_RIGHT and direction != (-CELL, 0):
                direction = (CELL, 0)       # вправо

        # пришло время сделать шаг
        if event.type == STEP:
            head_x, head_y = snake[0]
            new_head = (head_x + direction[0], head_y + direction[1])
            snake = [new_head]

    screen.fill((0, 0, 0))

    for x, y in snake:
        pygame.draw.rect(screen, (0, 255, 0), (x, y, CELL, CELL))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
