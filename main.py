import pygame
import grid

# разрешение в пикселях
WIDTH, HEIGHT = 1920, 1080
FPS = 30


pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))

clock = pygame.time.Clock()


scaler = 20

Grid = grid.Grid(WIDTH, HEIGHT, scaler)
Grid.first_gen()

pause = False
run = True
while run:
    clock.tick(FPS)
    screen.fill("black")

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_ESCAPE:
                run = False
            if event.key == pygame.K_SPACE:
                pause = not pause

    Grid.Conway(off_color="white", on_color="blue", surface=screen, pause=pause)

    if pygame.mouse.get_pressed()[0]:
        X, Y = pygame.mouse.get_pos()
        Grid.HandleMouse(X, Y)

    pygame.display.update()

pygame.quit()
