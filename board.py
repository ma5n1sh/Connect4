import numpy as np
import pygame
import copy


def draw_red_piece(screen, i, j, piece_col_base, piece_row_base, offset):
    pygame.draw.circle(screen, (255, 0, 0), (piece_col_base + j * offset, piece_row_base + i * offset), radius=30)


def draw_yellow_piece(screen, i, j, piece_col_base, piece_row_base, offset):
    pygame.draw.circle(screen, (255, 255, 0), (piece_col_base + j * offset, piece_row_base + i * offset), radius=30)


class Board:
    def __init__(self, screen=None):
        self.board = np.zeros((6, 7), dtype=bool)
        self.col_pos = np.ones(7) * 5
        self.piece_col_base, self.piece_row_base, self.offset = 36, 99, 70
        self.screen = screen
        self.board_img = pygame.image.load('res/Images/board.png')

    def set_piece(self, j, val):
        if j > -1 and self.col_pos[j] > -1:
            self.board[int(self.col_pos[j]), j] = val
            self.col_pos[j] -= 1

    def update_board(self):
        for i in range(6):
            for j in range(7):
                if i <= self.col_pos[j]:
                    continue
                if self.board[i, j]:
                    draw_red_piece(self.screen, i, j, self.piece_col_base, self.piece_row_base, self.offset)
                elif not self.board[i, j]:
                    draw_yellow_piece(self.screen, i, j, self.piece_col_base, self.piece_row_base, self.offset)

    def display_game_board(self):
        self.screen.blit(self.board_img, (0, 60))

    def clone(self):
        b = Board()
        b.board = copy.deepcopy(self.board)
        b.col_pos = copy.deepcopy(self.col_pos)
        return b
