from typing import List, NoReturn, Tuple
from Classes import NodeStructure
import pygame


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
D_BLUE = (0, 32, 96)
WIDTH, HEIGHT = 780, 450


def create_text(arr, font_size:int) -> List[pygame.font.SysFont]:
    rv = []
    font = pygame.font.SysFont('chalkduster.tff', font_size)
    for s in arr:
        rv.append(font.render(s, True, BLACK))
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
        self.nst = [[] for _ in self.nss] # nst = NodeStructureText
        self.nsp = [[] for _ in self.nss] # nsp = NodeStructurePos
        # continuous loop
        self.render()

    def draw_text(self, coords:List[Tuple[int, int]]) -> NoReturn:
        for text_obj, xy_pair in zip(self.nst[0][0], coords):
            self.screen.blit(text_obj, xy_pair)

    def load_node_structure(self, debug=True):
        for nstarr in range(len(self.nst)):
            for i,arr in enumerate(self.nss[0].depth_hashmap.values()):
                vec = []
                for val in arr:
                    vec.append(create_text(str(val.val), 32))
                self.nst[nstarr - 1].append(vec)
        if debug:
            for arr in self.nst:
                for vec in arr:
                    print(vec)

    def position_node_structure(self) -> List[Tuple[int, int]]:
        x, y = int(WIDTH / 2), int(HEIGHT / 2)
        return [(x, y)]

    def render(self) -> NoReturn:
        self.load_node_structure()
        while self.run:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        self.run = False
                    if event.key == pygame.K_t:
                        self.load_node_structure()
                    if event.key == pygame.K_d:
                        self.load_node_structure()
                        self.screen.blit(self.nst[0][0][0][0], (0, 0))
                        # self.draw_text(self.position_node_structure())
                    if event.key == pygame.K_c:
                        pass
            self.screen.fill(WHITE)
            # --[render start]--
            self.screen.blit(self.nst[0][0][0][0], (0, 0))
            # --[render end]--
            pygame.display.flip()
            self.clock.tick(144)
        pygame.quit()


if __name__ == '__main__':
    global w
    w = Window()
