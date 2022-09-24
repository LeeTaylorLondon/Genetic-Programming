from typing          import List, NoReturn, Tuple
from Classes         import NodeStructure
from NodeStrucGUI    import NodeStructureGUI
from GlobalVariables import func_set, term_set, funcrepr
from Consts          import WHITE, BLACK, D_BLUE, create_text
import pygame


WIDTH, HEIGHT = 780, 450


class Window:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.run = True
        self.clock = pygame.time.Clock()
        # Non-pygame attrs
        self.ns = NodeStructureGUI(self.screen)
        print(self.ns)
        # continuous loop
        self.render()

    def debug_circleobjs(self):
        for arr in self.ns.circle_objects:
            for obj in arr:
                print(obj.pygame_coords)
        pass

    def render(self) -> NoReturn:
        self.ns.set_node_depths()
        self.ns.print_depth_hashmap()
        while self.run:
            for event in pygame.event.get():
                # Bind key to function(s)
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        self.run = False
                    if event.key == pygame.K_t:
                        pass
                    if event.key == pygame.K_d:
                        self.debug_circleobjs()
                    if event.key == pygame.K_c:
                        pass
            self.screen.fill(WHITE)
            # --[render start]--

            self.ns.render()
            # print(self.ns.circle_objects)

            # --[render end]--
            pygame.display.flip()
            self.clock.tick(144)
        pygame.quit()


if __name__ == '__main__':
    global w
    w = Window()
