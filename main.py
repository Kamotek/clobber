import pygame

from game.game import Game
pygame.init()
pygame.font.init()


if __name__ == '__main__':
    Game(mode='PvAI',
         ai1_type='aggressive', ai1_algo='alpha_beta', ai1_depth=3,
         ai2_type='aggressive', ai2_algo='alpha_beta', ai2_depth=3).run()
