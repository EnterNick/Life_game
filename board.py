import math

import pygame
from copy import deepcopy


class Board:
    def __init__(self, width, height):
        self.updating = False
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        self.left = 10
        self.top = 10
        self.cell_size = 20
        self.pheight = self.height * self.cell_size
        self.pwidth = self.width * self.cell_size

    def start(self):
        self.updating = True

    def stop(self):
        self.updating = False

    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self, screen):
        for i in range(self.height):
            for j in range(self.width):
                pygame.draw.rect(screen, "white", (
                    self.left + j * self.cell_size, self.top + i * self.cell_size, self.cell_size, self.cell_size),
                                 1)
                if self.board[i][j] == 1:
                    pygame.draw.rect(screen, (255, 211, 58), (
                        self.left + j * self.cell_size + 1, self.top + i * self.cell_size + 1, self.cell_size - 2,
                        self.cell_size - 2),
                                     0)

    def get_cell(self, mouse_pos):
        x, y = mouse_pos
        i = (y - self.top) // self.cell_size
        j = (x - self.left) // self.cell_size
        if pygame.Rect(0, 0, self.height, self.width).collidepoint(i, j):
            return i, j
        else:
            return None

    def on_click(self, cell_coords):
        if cell_coords:
            x, y = cell_coords
            self.board[x][y] = 0 if self.board[x][y] else 1

    def get_click(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        self.on_click(cell)

    def neighbors(self, s, row_number, column_number):
        n = 0
        lst = []
        for i in range(row_number - 1, row_number + 2):
            for j in range(column_number - 1, column_number + 2):
                if 0 <= i < self.height and 0 <= j < self.width and s[i][j]:
                    n += 1
                    lst.append((i, j))
        return n

    def update(self):
        cells = deepcopy(self.board)
        for i in range(self.height):
            for j in range(self.width):
                a = self.neighbors(cells, i, j)
                a = a - 1 if cells[i][j] else a
                if a == 3:
                    self.board[i][j] = 1
                elif a not in [2, 3]:
                    self.board[i][j] = 0

    def reset(self):
        self.board = [[0] * self.width for _ in range(self.height)]

    def set_size(self, n):
        if n > self.width:
            for i in self.board:
                i.extend([0] * (n - self.width))
            for _ in range(n):
                self.board.append([0] * n)
        else:
            self.board = self.board[:n]
            for i in self.board:
                for _ in range(self.width - n):
                    i.pop(-1)
        self.cell_size = math.ceil(self.pwidth / n)
        self.width = self.height = n
