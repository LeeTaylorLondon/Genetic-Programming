import pygame.draw
from Classes import NodeStructure, Node, List
from GlobalVariables import measure_fitness, funcrepr
from Consts import BLACK, WHITE, D_BLUE, create_text, create_text_str


"""
Purpose: GUI version of NodeStructure, this class is used 
to store and render from. This class inherits from NodeStructure 
and will have extra attributes and methods to render from.

Idea: objects to render - 
copy of self.depth_hashmap.values() which is a matrix of Node(s)
for each Node store an ellipses w/ it's value as a text value. 
Possibly store it in a similar fashion as a matrix of array's storing 
 render-able objects which are shapes and text. 
 
Idea2: generating coordinates -
Create relativity calculations. Possibly impose the whole NS-GUI
 onto a giant invisible square. Store these somewhere? 
"""


# ------ Class Definition Start ------
class NodeGUI(Node):
    def __init__(self, node, screen):
        super(NodeGUI, self).__init__(val=node.val)
        self.node          = node
        self.l             = None
        self.r             = None
        self.p             = None
        self.screen        = screen
        self.pygame_val    = self.init_pygame_val()
        self.pygame_text   = create_text_str(self.pygame_val, 18, WHITE)
        self.pygame_textr  = self.pygame_text.get_rect()
        self.pygame_coords = [0, 0] # x,y
        self.pygame_radius = 32

    def init_pygame_val(self):
        # if type(self.val) != list and type(self.val) != int and type(self.val) != List:
        if type(self.val) not in [List, list, int]:
            return funcrepr(self.val)
        else: return str(self.val)

    def set_pygame_coords(self, x, y):
        self.pygame_coords[0], self.pygame_coords[1] = x, y

    def render(self):
        """ A circle with it's value should be rendered """
        sx, sy, sr = self.pygame_coords[0], self.pygame_coords[1], self.pygame_radius
        # These lines draw a connecting line from a node to it's children
        if type(self.l) == NodeGUI:
            lx, ly = self.l.pygame_coords
            pygame.draw.line(self.screen, BLACK, [sx, sy], [lx, ly], width=6)
        if type(self.r) == NodeGUI:
            rx, ry = self.r.pygame_coords
            pygame.draw.line(self.screen, BLACK, [sx, sy], [rx, ry], width=6)
        # Draw value
        pygame.draw.circle(self.screen, BLACK, [sx, sy], sr)
        self.pygame_textr.center = (sx, sy)
        self.screen.blit(self.pygame_text, self.pygame_textr)

    def __str__(self):
        return f"<NodeGUI {self.val}>"
# ------ Class Definition End ------


# ------ Class Definition Start ------
class NodeStructureGUI(NodeStructure):
    def __init__(self, screen):
        super(NodeStructureGUI, self).__init__()
        self.screen         = screen
        self.circle_objects = self.init_circle_objects()
        self.root           = self.circle_objects[0][0] # NodeGUI
        # self.init_left_right()
        self.init_lrp()

    def init_circle_objects(self):
        render_matrix, y = [], 0
        for arr in self.depth_hashmap.values():
            y += 75
            x, i_arr = 0, []
            for node in arr:
                x += 75
                n_gui_obj = NodeGUI(node, self.screen)
                n_gui_obj.set_pygame_coords(x, y)
                i_arr.append(n_gui_obj)
            render_matrix.append(i_arr)
        return render_matrix

    def init_lrp(self):
        """ Selects 'one' then assigns l,r by selecting below 'two' """
        cn = self.root
        for ai,arr in enumerate(self.circle_objects):
            bc = 0
            for ni,node in enumerate(arr):
                cn = self.circle_objects[ai][ni]
                if node.type == 'func':
                    try: cn.l = self.circle_objects[ai+1][bc]
                    except IndexError as e: pass
                    try: cn.r = self.circle_objects[ai+1][bc+1]
                    except IndexError as e: pass
                    bc += 2
        pass

    def render(self):
        for array in self.circle_objects:
            for node in array:
                node.render()

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return f"<NS-GUI {round(float(measure_fitness(self)), 2)}>"
# ------ Class Definition End ------


if __name__ == '__main__':
    nsgui = NodeStructureGUI()
    print(nsgui)