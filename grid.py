import pygame
import numpy as np
import random


class Grid:
    def __init__(self, width, height, scale):
        self.scale = scale

        self.columns = height // scale
        self.rows = width // scale

        self.grid_array = np.ndarray(shape=(self.rows, self.columns))

        # генерация случайного начального поля
        for i in range(self.rows):
            for j in range(self.columns):
                self.grid_array[i][j] = random.randint(0, 1)

    # отрисовка
    def draw(self, color_1, color_2, surface, pause):
        for i in range(self.rows):
            for j in range(self.columns):
                x = i * self.scale
                y = j * self.scale
                if self.grid_array[i][j] == 1:
                    pygame.draw.rect(surface, color_2,
                                     [x, y, self.scale - 1, self.scale - 1])
                else:
                    pygame.draw.rect(surface, color_1,
                                     [x, y, self.scale - 1, self.scale - 1])

        # генерация массива следующего "поколения"
        new_arr = np.ndarray(shape=(self.rows, self.columns))
        if not pause:
            for i in range(self.rows):
                for j in range(self.columns):
                    state = self.grid_array[i][j]
                    neighbours = self.neighbours(i, j)
                    if state == 0 and neighbours == 3:
                        new_arr[i][j] = 1
                    elif state == 1 and (neighbours < 2 or neighbours > 3):
                        new_arr[i][j] = 0
                    else:
                        new_arr[i][j] = state
            self.grid_array = new_arr

    # на щелчок лкм "красить" клетку
    def HandleMouse(self, x, y):
        x = x // self.scale
        y = y // self.scale

        if self.grid_array[x][y] is not None:
            self.grid_array[x][y] = 1

    # функция для подсчета количества соседей
    def neighbours(self, x, y):
        total = 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                x = (x + i + self.rows) % self.rows
                y = (y + j + self.columns) % self.columns
                total += self.grid_array[x][y]

        total -= self.grid_array[x][y]
        return total
