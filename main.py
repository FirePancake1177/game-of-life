import pygame
import grid

# разрешение экрана
WIDTH, HEIGHT = 1920, 1080

screen_size = (WIDTH, HEIGHT)

pygame.init()
pygame.display.set_caption("Игра Жизнь")
screen = pygame.display.set_mode(screen_size)
clock = pygame.time.Clock()

FPS = 30

# масштабирование
SCALE = 25

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

    Grid.draw(color_1="white", color_2="blue", surface=screen, pause=pause)

    # обработка нажатия левой кнопки мыши
    if pygame.mouse.get_pressed()[0]:
        X, Y = pygame.mouse.get_pos()
        Grid.click(X, Y)

    pygame.display.update()

pygame.quit()
