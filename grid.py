import pygame
import numpy as np
import random


class Grid:
    def __init__(self, width, height, scale):
        self.scale = scale

        self.columns = int(height / scale)
        self.rows = int(width / scale)

        self.size = (self.rows, self.columns)
        self.grid = np.ndarray(shape=self.size)

    def first_gen(self):
        for x in range(self.rows):
            for y in range(self.columns):
                self.grid[x][y] = random.randint(0, 1)

    def Conway(self, off_color, on_color, surface, pause):
        for x in range(self.rows):
            for y in range(self.columns):
                y_pos = y * self.scale
                x_pos = x * self.scale
                # random_color = (random.randint(10, 255), random.randint(10, 255), random.randint(10, 255))
                if self.grid[x][y] == 1:
                    pygame.draw.rect(surface, on_color,
                                     [x_pos, y_pos, self.scale - 1, self.scale - 1])
                else:
                    pygame.draw.rect(surface, off_color,
                                     [x_pos, y_pos, self.scale - 1, self.scale - 1])

        next = np.ndarray(shape=self.size)
        if not pause:
            for x in range(self.rows):
                for y in range(self.columns):
                    state = self.grid[x][y]
                    neighbours = self.get_neighbours(x, y)
                    if state == 0 and neighbours == 3:
                        next[x][y] = 1
                    elif state == 1 and (neighbours < 2 or neighbours > 3):
                        next[x][y] = 0
                    else:
                        next[x][y] = state
            self.grid = next

    def HandleMouse(self, x, y):
        _x = x // self.scale
        _y = y // self.scale

        if self.grid[_x][_y] is not None:
            self.grid[_x][_y] = 1

    def get_neighbours(self, x, y):
        total = 0
        for n in range(-1, 2):
            for m in range(-1, 2):
                x_edge = (x + n + self.rows) % self.rows
                y_edge = (y + m + self.columns) % self.columns
                total += self.grid[x_edge][y_edge]

        total -= self.grid[x][y]
        return total
