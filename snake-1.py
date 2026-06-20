# Шаг 1: Полотно (окно игры)
import pygame

pygame.init()

WIDTH, HEIGHT = 600, 400

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Змейка — шаг 1")

clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))  # чёрный фон
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
