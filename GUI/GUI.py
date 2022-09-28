from typing          import List, NoReturn, Tuple
from Classes         import NodeStructure
from NodeStrucGUI    import NodeStructureGUI
from GlobalVariables import func_set, term_set, funcrepr
from Consts          import WHITE, BLACK, D_BLUE, create_text, L1BLACK
import pygame


WIDTH, HEIGHT = 780, 450


class Window:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.run    = True
        self.clock  = pygame.time.Clock()
        # Non-pygame attrs
        # self.ns      = NodeStructureGUI(self.screen)
        self.ns      = [NodeStructureGUI(self.screen) for _ in range(2)]
        self.nsspace = 10
        self.init_ns() # Prevents overlapping NoStrucs
        # continuous loop
        self.render()

    def init_ns(self):
        """ This method prevents NodeStrucGUIs from overlapping
         by applying an offset to each NSGUI object. """
        if type(self.ns) != list: return False
        for nsi,ns in enumerate(self.ns[:-1]):
            ns.set_node_depths()
            # Locate longest list in matrix of node-objects
            longest_len_i, longest_len_val = -1, -1
            for i,arr in enumerate(ns.circle_objects):
                if len(arr) > longest_len_val: longest_len_i, longest_len_val = i, len(arr)
            # Width_of_Nstruc = (2*Radius) + Spacing(#Nodes - 1) + Padding
            warr    = ns.circle_objects[longest_len_i]              # Widest array
            l, r, s = len(warr), warr[0].pygame_radius, ns.spacingx # Radius, Node-Spacing
            spacing = (2 * r) + (s * (l - 1)) + self.nsspace
            # Apply spacing -> to the next one
            for arr in self.ns[nsi+1].circle_objects:
                for nodegui in arr:
                    x, y = nodegui.pygame_coords
                    nodegui.set_pygame_coords(x+spacing, y)
        pass

    def debug_circleobjs(self):
        for arr in self.ns.circle_objects:
            for obj in arr:
                print(obj.pygame_coords)
        pass

    def render(self) -> NoReturn:
        # self.ns.set_node_depths()
        # self.ns.print_depth_hashmap()
        print(len(self.ns))
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

            # self.ns.render()
            for ns in self.ns:
                ns.render()
            # print(self.ns.circle_objects)

            # --[render end]--
            pygame.display.flip()
            self.clock.tick(144)
        pygame.quit()


if __name__ == '__main__':
    global w
    w = Window()
    # r = w.ns.root

