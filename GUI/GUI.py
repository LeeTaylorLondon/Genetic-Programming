from typing import List, NoReturn, Tuple
from Classes import NodeStructure
from GlobalVariables import func_set, term_set, funcrepr
from Consts import WHITE, BLACK, D_BLUE, create_text
import pygame


WIDTH, HEIGHT = 780, 450


class Window:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.run = True
        self.clock = pygame.time.Clock()
        self.nss = [NodeStructure()] # nss = NodeStructure(s)
        # continuous loop
        self.render()

    def draw_text(self, coords:List[Tuple[int, int]]) -> NoReturn:
        for text_obj, xy_pair in zip(self.nst[0][0], coords):
            self.screen.blit(text_obj, xy_pair)

    def draw_centered_text(self, x, y, r=25.0):
        pygame.draw.circle(self.screen, BLACK, (x, y), r)
        txt = create_text('4', 48, WHITE)[0]
        trect = txt.get_rect()
        trect.center = (x, y)
        self.screen.blit(txt, trect)

    def render(self) -> NoReturn:
        self.nss[0].set_node_depths()
        self.nss[0].print_depth_hashmap()
        while self.run:
            for event in pygame.event.get():
                # Bind key to function(s)
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        self.run = False
                    if event.key == pygame.K_t:
                        pass
                    if event.key == pygame.K_d:
                        pass
                    if event.key == pygame.K_c:
                        pass
            self.screen.fill(WHITE)
            # --[render start]--

            self.draw_centered_text(40, 40)

            # --[render end]--
            pygame.display.flip()
            self.clock.tick(144)
        pygame.quit()


if __name__ == '__main__':
    global w
    w = Window()
