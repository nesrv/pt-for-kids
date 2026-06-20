# Шаг 5: Хвост и рост при съедании яблока
import pygame
import random

pygame.init()

WIDTH, HEIGHT = 600, 400
CELL = 20

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Змейка — шаг 5")

clock = pygame.time.Clock()
font = pygame.font.SysFont("arial", 28)

snake = [(WIDTH // 2, HEIGHT // 2)]
direction = (CELL, 0)
game_over = False

STEP = pygame.USEREVENT
pygame.time.set_timer(STEP, 150)


def spawn_apple():
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

        if not game_over and event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != (0, CELL):
                direction = (0, -CELL)
            elif event.key == pygame.K_DOWN and direction != (0, -CELL):
                direction = (0, CELL)
            elif event.key == pygame.K_LEFT and direction != (CELL, 0):
                direction = (-CELL, 0)
            elif event.key == pygame.K_RIGHT and direction != (-CELL, 0):
                direction = (CELL, 0)

        if not game_over and event.type == STEP:
            head_x, head_y = snake[0]
            new_head = (head_x + direction[0], head_y + direction[1])

            # Удар о стену
            if (
                new_head[0] < 0
                or new_head[0] >= WIDTH
                or new_head[1] < 0
                or new_head[1] >= HEIGHT
            ):
                game_over = True

            # Удар о себя
            elif new_head in snake:
                game_over = True

            else:
                snake.insert(0, new_head)

                if new_head == apple:
                    apple = spawn_apple()
                else:
                    snake.pop()  # убираем хвост — змейка «ползёт»

    screen.fill((0, 0, 0))

    for x, y in snake:
        pygame.draw.rect(screen, (0, 255, 0), (x, y, CELL, CELL))

    if not game_over:
        pygame.draw.rect(screen, (255, 0, 0), (*apple, CELL, CELL))
    else:
        text = font.render("Игра окончена! Закрой окно.", True, (255, 255, 255))
        screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
