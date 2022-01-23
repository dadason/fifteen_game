import pygame
import numpy as np


class Board:
    # создание поля размером width на height
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        # отступы слева и сверху, размер ячейки
        self.left = 20
        self.top = 20
        self.cell_size = 30
        self.current_cell = ()
        self._start_field()

    def _start_field(self):
        self.num_dict = {}
        num_list = np.random.permutation(16)
        for y in range(self.height):
            for x in range(self.width):
                self.num_dict[(x, y)] = num_list[4 * x + y]
                if self.num_dict[(x, y)] == 0:
                    self.empty_cell = (x, y)
                    print(x, y)

    def draw_num(self):
        for y in range(self.height):
            for x in range(self.width):
                if self.num_dict[(x, y)] == 0:
                    continue
                font = pygame.font.Font(None, 30)
                text = font.render(str(self.num_dict[(x, y)]), False, (100, 255, 100))
                screen.blit(text, (x * self.cell_size + self.left + int(self.cell_size / 2),
                                   y * self.cell_size + self.top + int(self.cell_size / 2)))

    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self, screen):
        for y in range(self.height):
            for x in range(self.width):
                pygame.draw.rect(screen, pygame.Color(255, 255, 255), (
                    x * self.cell_size + self.left, y * self.cell_size + self.top, self.cell_size,
                    self.cell_size), 1)
        self.draw_num()
        if self.is_win():
            pass #завершить игру
        # if self.current_cell:  # не пусто
        #     if (self.current_cell[0] >= 0 and self.current_cell[0] <= 3) and \
        #             (self.current_cell[1] >= 0 and self.current_cell[1] <= 3):
        #         self.on_click(self.current_cell, screen)
    def is_win(self):
        pass
        #проверка поля на выигрыш

    def get_click(self, mouse_pos, screen):
        self.current_cell = self.get_cell(mouse_pos)
        self.on_click(self.current_cell, screen)

    def get_cell(self, mouse_pos):
        mouse_x, mouse_y = mouse_pos
        cell_coords = (mouse_x - self.left) // self.cell_size, \
                      (mouse_y - self.top) // self.cell_size

        return cell_coords

    def on_click(self, cell_coords, screen):
        if cell_coords[0] < 0 or cell_coords[0] > 3 or cell_coords[1] < 0 or cell_coords[1] > 3:
            return
        if (cell_coords[0] + 1, cell_coords[1]) == self.empty_cell or\
                (cell_coords[0] - 1, cell_coords[1]) == self.empty_cell or\
                (cell_coords[0], cell_coords[1] + 1) == self.empty_cell or\
                (cell_coords[0], cell_coords[1] - 1) == self.empty_cell:
            b = self.num_dict[cell_coords]
            self.num_dict[cell_coords] = 0
            self.num_dict[self.empty_cell] = b
            self.empty_cell = cell_coords
        # rect_centre = (cell_coords[0] * self.cell_size + self.left, cell_coords[1] * self.cell_size + self.top)
        #
        # # Drawing Rectangle
        # pygame.draw.rect(screen, (0, 255, 25),
        #                  pygame.Rect(rect_centre[0], rect_centre[1], self.cell_size, self.cell_size))
        # pygame.display.flip()


pygame.init()
pygame.font.init()
size = 600, 600
screen = pygame.display.set_mode(size)
board = Board(4, 4)
board.set_view(50, 50, 55)
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            board.get_click(event.pos, screen)
            pygame.display.update()
            break

    screen.fill((0, 0, 0))
    board.render(screen)  # прорисовка поля
    pygame.display.flip()