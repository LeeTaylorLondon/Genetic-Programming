from typing          import List, NoReturn, Tuple
from Classes         import NodeStructure
from NodeStrucGUI    import NodeStructureGUI
from GlobalVariables import func_set, term_set, funcrepr
from Consts          import WHITE, BLACK, D_BLUE, create_text, L1BLACK
import pygame


WIDTH, HEIGHT = 1450, 452


class Window:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.run    = True
        self.clock  = pygame.time.Clock()
        # Non-pygame attrs
        # self.ns      = NodeStructureGUI(self.screen)
        self.ns      = [NodeStructureGUI(self.screen) for _ in range(7)]
        self.nsspace = 25
        self.overlap = 0
        self.init_ns() # Prevents overlapping NoStrucs
        # continuous loop
        self.render()

    def init_ns(self):
        """ This method prevents NodeStrucGUIs from overlapping
         by applying an offset to each NSGUI object. """
        if type(self.ns) != list:
            return False
        for nsi,ns in enumerate(self.ns[:-1]): # Do all but last one
            ns.set_node_depths()
            spacing = ns.pixel_width + self.nsspace
            self.overlap += spacing
            self.ns[nsi+1].hitbox[0] += self.overlap
            # Apply spacing -> to the next one
            for arr in self.ns[nsi+1].circle_objects:
                for nodegui in arr:
                    x, y = nodegui.pygame_coords
                    nodegui.set_pygame_coords(x+self.overlap, y)
        pass

    def debug_circleobjs(self):
        for arr in self.ns.circle_objects:
            for obj in arr:
                print(obj.pygame_coords)
        pass

    def render(self) -> NoReturn:
        # self.ns.set_node_depths()
        # self.ns.print_depth_hashmap()
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
            self.screen.fill(L1BLACK)
            # --[render start]--

            """ Render each NodeStructure """
            for ns in self.ns:
                ns.render()

            # --[render end]--
            pygame.display.flip()
            self.clock.tick(144)
        pygame.quit()


if __name__ == '__main__':
    global w
    w = Window()
    # r = w.ns.root

