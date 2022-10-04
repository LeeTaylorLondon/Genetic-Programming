from typing          import List, NoReturn, Tuple
from Classes         import NodeStructure, GeneticProgram
from NodeStrucGUI    import NodeStructureGUI
from GlobalVariables import func_set, term_set, funcrepr
from Consts          import WHITE, BLACK, D_BLUE, create_text, L1BLACK, RED, CGREEN
import pygame


WIDTH, HEIGHT = 897, 452


class Window:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
        self.run    = True
        self.clock  = pygame.time.Clock()
        # Non-pygame attrs
        # self.ns      = NodeStructureGUI(self.screen)
        self.popsize = 8
        self.gens    = 1
        self.gp      = GeneticProgram(count=self.popsize)
        print("gp.ns =", self.gp.population)   # DEBUG DEBUG
        self.ns      = [[NodeStructureGUI(self.screen, ns) for ns in self.gp.population]]
        print("self.ns =", self.ns)            # DEBUG DEBUG
        for _ in range(self.gens):
            self.ns.append([NodeStructureGUI(self.screen) for x in range(self.popsize - 7)])
        # self.ns      = [NodeStructureGUI(self.screen) for _ in range(6)]
        self.xoverlap = 0
        self.yoverlap = 0
        self.nsspace = 25
        self.yoffset = 25 # Speed of scrolling
        self.yoffse_ = 0  # Var applied
        self.init_nss() # Prevents overlapping GUI elements
        # continuous loop
        self.render()

    def init_nss(self):
        """ This method prevents NodeStrucGUIs from overlapping
         by applying an offset to each NSGUI object. """
        if type(self.ns) != list:
            return False
        for i,arr in enumerate(self.ns):
            self.xoverlap = 0
            self.activate_yoverlap(i)
            for nsi,ns in enumerate(arr[:-1]): # Do all but last one
                ns.set_node_depths()
                spacing        = ns.pixel_width + self.nsspace
                self.xoverlap += spacing
                # Increase 'X' values
                arr[nsi+1].hitbox[0]         += self.xoverlap
                arr[nsi+1].pygame_fitness[0] += self.xoverlap
                arr[nsi+1].botbox[0]         += self.xoverlap
                # Apply spacing -> to the next one
                for coarr in arr[nsi+1].circle_objects:
                    for nodegui in coarr:
                        x, y = nodegui.pygame_coords
                        nodegui.set_pygame_coords(x+self.xoverlap, y)
        pass

    def activate_yoverlap(self, i):
        if i == 0: return  # Cannot apply height to first NSGUI
        y = -1  # y = Height in pixels
        # for-loop and if-statement calculate max height
        for ns in self.ns[i-1]:
            if (c:= ns.calc_pixel_height()) > y:
                y = c
        y += self.ns[0][0].pad * 3
        y += self.ns[0][0].botboxh
        y += self.yoverlap
        # Apply height diff
        for ns in self.ns[i]:
            ns.apply_y_offset(y)
        # Allows multiple levels of population members or generations
        if y > self.yoverlap: self.yoverlap = y

    def debug_circleobjs(self):
        for arr in self.ns.circle_objects:
            for obj in arr:
                print(obj.pygame_coords)
        pass

    def change_nscolor(self, i=0, v=0, new_color=RED, old_color=CGREEN):
        if type(i) in [list, tuple]:
            for x in i:
                self.change_nscolor(x, new_color=new_color)
            return
        # If statement allows for alternating back to original/another color
        if self.ns[v][i].color == new_color:
            new_color = old_color
        # Re-assign color and regenerate some objects
        self.ns[v][i].color = new_color
        self.ns[v][i].pygame_fitness = self.ns[v][i].init_pygame_fitness()
        for arr in self.ns[v][i].circle_objects:
            for nod in arr:
                nod.color = new_color
                nod.pygame_lcolor = new_color
                nod.pygame_text = nod.init_pygame_text()

    def apply_scrolling(self):
        # Scrolling
        for vec in self.ns:
            for nsobj in vec:
                nsobj.apply_y_offset(self.yoffse_)
        self.yoffse_ = 0

    def add_nodestruc(self, ns, v=0, i=0):
        """ Calculate and apply x & y offset from the respective 'vector' """
        xoffset, yoffset = 0, 0
        # Calculate Y spacing
        rn = self.ns[v][0].circle_objects[0][0]
        yoffset = rn.pygame_coords[1] - (rn.pygame_radius * 2) - ns.pad + 1
        # Change height
        ns.apply_y_offset(yoffset)
        # Calculate X spacing
        for nsgui in self.ns[v]:
            xoffset += nsgui.calc_pixel_width()
            xoffset += self.nsspace
        # self.activate_yoverlap(i)
        ns.hitbox[0]         += xoffset
        ns.pygame_fitness[0] += xoffset
        ns.botbox[0]         += xoffset
        # Apply spacing -> to the next one
        for coarr in ns.circle_objects:
            for nodegui in coarr:
                x, y = nodegui.pygame_coords
                nodegui.set_pygame_coords(x + xoffset, y)
        self.ns[v].insert(i, ns)

    def render(self) -> NoReturn:
        # self.ns.set_node_depths()
        # self.ns.print_depth_hashmap()
        while self.run:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 4:
                        self.yoffse_ = self.yoffset
                    if event.button == 5:
                        self.yoffse_ = self.yoffset * -1
                # Bind key to function(s)
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        self.run = False
                    if event.key == pygame.K_s:
                        # self.change_nscolor(i=[x for x in range(0, len(self.ns))])
                        s1, s2 = self.gp.selection()
                        self.change_nscolor(i=[s1, s2])
                        # self.change_nscolor(i=[s1, s2], new_color=D_BLUE)
                    if event.key == pygame.K_d:
                        # self.debug_circleobjs()
                        for obj in self.ns: obj.print_depth_hashmap()
                    if event.key == pygame.K_c:
                        # self.change_nscolor()
                        sarr = self.gp.selection(), self.gp.selection()
                        nsco = self.gp.crossover(sarr, debug=False)
                        nsco = NodeStructureGUI(self.screen, nsco)
                        print(nsco)
                        self.change_nscolor(sarr, v=0)
                        self.add_nodestruc(nsco, v=1)
            self.screen.fill(L1BLACK)
            self.apply_scrolling()
            # --[render start]--
            """ Render each NodeStructure """
            for vec in self.ns:
                for ns in vec:
                    ns.render()
            # --[render end]--
            pygame.display.flip()
            self.clock.tick(144)
        pygame.quit()


if __name__ == '__main__':
    global w
    w = Window()
    # r = w.ns.root

