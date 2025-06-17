import pygame
import sys
from game.board import Board
from game.renderer import Renderer
from game.variables import WIDTH, HEIGHT, FPS, CELL_SIZE, WHITE, BLACK, FONT_SIZE
from heuristics.utils import calculate_possible_moves
from game.player import HumanPlayer, AIPlayer

AI_TYPES = {
    'aggressive': 'aggressive',
    'defensive': 'defensive',
    'positional': 'positional',
    'random': 'random'
}

ALGO_TYPES = ['minimax', 'alpha_beta']

class Game:
    def __init__(
        self,
        mode='PvP',
        ai1_type='aggressive', ai1_algo='alpha_beta', ai1_depth=3,
        ai2_type='aggressive', ai2_algo='alpha_beta', ai2_depth=3
    ):
        pygame.init()
        pygame.font.init()
        self.font = pygame.font.SysFont(None, FONT_SIZE)
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Clobber Game")
        self.clock = pygame.time.Clock()
        self.board = Board()
        self.renderer = Renderer(self.screen, self.board)
        self.mode = mode
        self.turn = 0
        self.status_msgs = [
            "Białe: Wybierz pionka do ruchu",
            "Białe: Wybierz gdzie ruszyć",
            "Czarne: Wybierz pionka do ruchu",
            "Czarne: Wybierz gdzie ruszyć"
        ]
        if mode == 'PvP':
            self.players = [HumanPlayer(1), HumanPlayer(2)]
        elif mode == 'PvAI':
            self.players = [
                HumanPlayer(1),
                AIPlayer(2, ai1_type, ai1_algo, ai1_depth)
            ]
        elif mode == 'AIvAI':
            self.players = [
                AIPlayer(1, ai1_type, ai1_algo, ai1_depth),
                AIPlayer(2, ai2_type, ai2_algo, ai2_depth)
            ]
        else:
            raise ValueError(f"Unknown mode: {mode}")

    def run(self):
        running, winner = True, None
        while running:
            self.clock.tick(FPS)
            current = self.players[self.turn]
            pid = current.id
            if not calculate_possible_moves(self.board, pid):
                winner = 3 - pid; break
            for ev in pygame.event.get():
                if ev.type == pygame.QUIT: running=False
                elif ev.type == pygame.MOUSEBUTTONDOWN and current.is_human():
                    x,y=ev.pos
                    if y < self.board.size*CELL_SIZE:
                        sel=current.handle_click((y//CELL_SIZE,x//CELL_SIZE), self.board)
                        if sel:
                            s,d=sel; self.board.move_piece(s,d); self._advance()
            if not running: break
            if not current.is_human():
                m=current.get_move(self.board)
                if m: s,d=m; self.board.move_piece(s,d); self._advance()
            self.screen.fill(WHITE)
            hl=[]; act=self.players[self.turn]
            if hasattr(act,'selected') and act.selected: hl=act.valid_moves
            idx=self.turn*2 + (1 if getattr(act,'selected',False) else 0)
            self.renderer.draw(hl,self.status_msgs[idx])
            pygame.display.flip()
        res = f"Gracz {winner} wygrywa!" if winner else "Koniec Gry"
        pygame.time.delay(200); self.screen.fill(WHITE)
        lab=self.font.render(res,True,BLACK)
        rc=lab.get_rect(center=(WIDTH//2,HEIGHT//2)); self.screen.blit(lab,rc)
        pygame.display.flip(); pygame.time.delay(3000)
        pygame.quit(); sys.exit()

    def _advance(self): self.turn=1-self.turn
