import pygame

from game.variables import *


class Renderer:
    def __init__(self, screen, board):
        self.screen = screen
        self.board = board


    def draw(self, valid_moves, turn_message):
        status_font = pygame.font.Font(None, 36)
        button_font = pygame.font.Font(None, 48)

        for r in range(self.board.size):
            for c in range(self.board.size):
                rect = pygame.Rect(c * CELL_SIZE, r * CELL_SIZE, CELL_SIZE, CELL_SIZE)
                color = LIGHT_GRAY if (r + c) % 2 == 0 else DARK_GRAY
                pygame.draw.rect(self.screen, color, rect)

        for (vr, vc) in valid_moves:
            rect = pygame.Rect(vc * CELL_SIZE, vr * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(self.screen, GREEN, rect, 4)

        for r in range(self.board.size):
            for c in range(self.board.size):
                val = self.board.grid[r][c]
                if val:
                    center = (c * CELL_SIZE + CELL_SIZE // 2,
                              r * CELL_SIZE + CELL_SIZE // 2)
                    color = WHITE_STONE if val == 1 else BLACK_STONE
                    pygame.draw.circle(self.screen, color, center, CELL_SIZE // 3)
                    pygame.draw.circle(self.screen, BLACK, center, CELL_SIZE // 3, 2)

        for i in range(self.board.size + 1):
            pygame.draw.line(self.screen, BLACK,
                             (0, i * CELL_SIZE), (WIDTH, i * CELL_SIZE), 2)
            pygame.draw.line(self.screen, BLACK,
                             (i * CELL_SIZE, 0), (i * CELL_SIZE, self.board.size * CELL_SIZE), 2)
        status_rect = pygame.Rect(0, HEIGHT - MARGIN, WIDTH, MARGIN)
        pygame.draw.rect(self.screen, GOLD, status_rect)
        pygame.draw.rect(self.screen, BLACK, status_rect, 2)
        text = status_font.render(turn_message, True, BLACK)
        self.screen.blit(text, (10, HEIGHT - MARGIN + (MARGIN - text.get_height()) // 2))

        btn = button_font.render("FORFEIT", True, BLACK)

        bx = WIDTH - btn.get_width() - 10
        by = HEIGHT - MARGIN + (MARGIN - btn.get_height()) // 2
        self.screen.blit(btn, (bx, by))
