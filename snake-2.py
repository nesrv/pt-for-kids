# Шаг 2: Голова змейки
import pygame

pygame.init()

WIDTH, HEIGHT = 600, 400
CELL = 20  # размер одной клетки

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Змейка — шаг 2")

clock = pygame.time.Clock()

# Список частей змейки: пока только голова (x, y)
snake = [(WIDTH // 2, HEIGHT // 2)]

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))

    # Рисуем каждый сегмент змейки
    for x, y in snake:
        pygame.draw.rect(screen, (0, 255, 0), (x, y, CELL, CELL))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
