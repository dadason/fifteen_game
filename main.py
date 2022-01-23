import pygame


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
                font = pygame.font.Font(None, 30)
                text = font.render(str(y * 4 + x), False, (100, 255, 100))
                screen.blit(text, (x * self.cell_size + self.left + int(self.cell_size / 2),
                                   y * self.cell_size + self.top + int(self.cell_size / 2)))

    def get_click(self, mouse_pos, screen):
        cell = self.get_cell(mouse_pos)
        self.on_click(cell, screen)

    def get_cell(self, mouse_pos):
        mouse_x, mouse_y = mouse_pos
        cell_coords = (mouse_x - self.left) // self.cell_size, \
                      (mouse_y - self.top) // self.cell_size

        return cell_coords

    def on_click(self, cell_coords, screen):
        rect_centre = (cell_coords[0]*self.cell_size + self.left, cell_coords[1] * self.cell_size+ self.top)
        print(self.left,self.top,rect_centre)
        #pygame.draw.circle(screen, (0, 255, 25), rect_centre, 15)

        # Drawing Rectangle
        pygame.draw.rect(screen, (0,255,25), pygame.Rect(rect_centre[0], rect_centre[1],self.cell_size,self.cell_size))
        pygame.display.flip()
        print(cell_coords)


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
            # pygame.draw.circle(screen, (0, 255, 25), event.pos, 15)
            board.get_click(event.pos, screen)
            pygame.display.update()
            break

    screen.fill((0, 0, 0))
    board.render(screen)  # прорисовка поля
    pygame.display.flip()