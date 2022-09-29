from Classes         import NodeStructure, Node, List
from GlobalVariables import measure_fitness, funcrepr
from Consts          import BLACK, WHITE, D_BLUE, create_text, create_text_str, CGREEN, RED
import pygame.draw

# ------ Class Definition Start ------
class NodeGUI(Node):
    def __init__(self, node, screen):
        super(NodeGUI, self).__init__(val=node.val)
        self.node          = node
        self.l             = None
        self.r             = None
        self.p             = None
        self.screen        = screen
        self.color         = CGREEN
        self.pygame_val    = self.init_pygame_val()
        self.pygame_text   = create_text_str(self.pygame_val, 22, self.color)
        self.pygame_textr  = self.pygame_text.get_rect()
        self.pygame_radius = 18
        self.pygame_coords = [0, int(self.pygame_radius)] # x,y
        self.pygame_lwidth = 3 # 'line'-width (must be int)
        self.pygame_lcolor = self.color
        self.pygame_ncolor = BLACK

    def init_pygame_text(self):
        return create_text_str(self.pygame_val, 22, self.color)

    def init_pygame_val(self):
        # if type(self.val) != list and type(self.val) != int and type(self.val) != List:
        if type(self.val) not in [List, list, int]:
            return str.upper(funcrepr(self.val))
        else: return str(self.val)

    def set_pygame_coords(self, x, y):
        """ Used in NodeStrucGUI.init_circle_objects(...) """
        self.pygame_coords[0], self.pygame_coords[1] = x, y

    def render(self):
        """ This method draws each Node as a circle, layered with it's
         respective value and any line(s) to it's children. """
        sx, sy, sr = self.pygame_coords[0], self.pygame_coords[1], self.pygame_radius
        # These lines draw a connecting line from a node to it's children
        if type(self.l) == NodeGUI:
            lx, ly = self.l.pygame_coords
            pygame.draw.line(self.screen, self.pygame_lcolor, [sx, sy], [lx, ly], width=self.pygame_lwidth)
        if type(self.r) == NodeGUI:
            rx, ry = self.r.pygame_coords
            pygame.draw.line(self.screen, self.pygame_lcolor, [sx, sy], [rx, ry], width=self.pygame_lwidth)
        # Draw value
        pygame.draw.circle(self.screen, self.pygame_ncolor, [sx, sy], sr)
        self.pygame_textr.center = (sx, sy)
        self.screen.blit(self.pygame_text, self.pygame_textr)

    def __str__(self):
        return f"<NodeGUI {self.val}>"
# ------ Class Definition End ------