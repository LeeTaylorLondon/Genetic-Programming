from typing import List, NoReturn, Tuple
from Classes import NodeStructure
from GlobalVariables import func_set, term_set, funcrepr
import pygame


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
D_BLUE = (0, 32, 96)
WIDTH, HEIGHT = 780, 450


def create_text(arr, font_size) -> List[pygame.font.SysFont]:
    rv = []
    font = pygame.font.SysFont('chalkduster.tff', font_size)
    if type(arr) == list:
        for string in arr:
            rv.append(font.render(string, True, BLACK))
    elif type(arr) == str:
        rv.append(font.render(arr, True, BLACK))
    return rv


class Window:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.run = True
        self.clock = pygame.time.Clock()
        # non pygame attrs
        # self.text = create_text(["Input to Auto Encoder",
        #                          "Auto Encoder Output",
        #                          "[Key D: Pass Input to Auto Encoder]",
        #                          "[Key T: Load Random Image]",
        #                          "[Key C: Clear Input]"],
        #                         16)
        self.nss = [NodeStructure()] # nss = NodeStructure(s)
        # continuous loop
        self.render()

    def draw_text(self, coords:List[Tuple[int, int]]) -> NoReturn:
        for text_obj, xy_pair in zip(self.nst[0][0], coords):
            self.screen.blit(text_obj, xy_pair)

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

            self.screen.blit(create_text('Sample text', 48)[0], (0, 0))

            # --[render end]--
            pygame.display.flip()
            self.clock.tick(144)
        pygame.quit()


if __name__ == '__main__':
    global w
    w = Window()
