# Шаг 1: Полотно (окно игры)
import pygame

pygame.init()  # включаем pygame

WIDTH, HEIGHT = 600, 400  # размер окна

# создаём окно — это «холст», на котором будет игра
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Змейка — шаг 1")

clock = pygame.time.Clock()  # не даёт игре работать слишком быстро

running = True
# главный цикл — повторяется, пока окно открыто
while running:
    # проверяем все события (нажатия, закрытие окна...)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # нажали крестик
            running = False

    screen.fill((0, 0, 0))  # заливаем фон чёрным
    pygame.display.flip()   # показываем нарисованное на экране
    clock.tick(60)          # ~60 кадров в секунду

pygame.quit()
