from typing import List, NoReturn, Tuple
import pygame


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
D_BLUE = (0, 32, 96)
WIDTH, HEIGHT = 780, 380


def create_text(arr:List[str], font_size:int) -> List[pygame.font.SysFont]:
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
        self.text = create_text(["Input to Auto Encoder",
                                 "Auto Encoder Output",
                                 "[Key D: Pass Input to Auto Encoder]",
                                 "[Key T: Load Random Image]",
                                 "[Key C: Clear Input]"],
                                16)
        # continuous loop
        self.render()

    def draw_text(self, coords:List[Tuple[int, int]]) -> NoReturn:
        for text_obj, xy_pair in zip(self.text, coords):
            self.screen.blit(text_obj, xy_pair)

    def render(self) -> NoReturn:
        while self.run:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        pass
                    if event.key == pygame.K_t:
                        pass
                    if event.key == pygame.K_d:
                        pass
                    if event.key == pygame.K_c:
                        pass
            self.screen.fill(WHITE)
            # --[render start]--

            # --[render end]--
            pygame.display.flip()
            self.clock.tick(144)
        pygame.quit()


if __name__ == '__main__':
    Window()
