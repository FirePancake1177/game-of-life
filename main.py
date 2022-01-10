import pygame
import grid

# разрешение вашего экрана в пикселях
WIDTH = 1920
HEIGHT = 1080
FPS = 30

# масштабирование
SCALE = 25


pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# создание экземпляра класса Grid
Grid = grid.Grid(WIDTH, HEIGHT, SCALE)

pause = False
run = True

# цикл pygame
while run:
    clock.tick(FPS)
    screen.fill("black")

    # обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_ESCAPE:
                run = False
            if event.key == pygame.K_SPACE:
                pause = not pause

    Grid.draw(color_1="white", color_2="green", surface=screen, pause=pause)

    # обработка нажатия левой кнопки мыши
    if pygame.mouse.get_pressed()[0]:
        X, Y = pygame.mouse.get_pos()
        Grid.click(X, Y)

    pygame.display.update()

pygame.quit()
