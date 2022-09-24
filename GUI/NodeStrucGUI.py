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
        self.screen        = screen
        self.pygame_val    = self.init_pygame_val()
        self.pygame_text   = create_text_str(self.pygame_val, 18, WHITE)
        self.pygame_textr  = self.pygame_text.get_rect()
        self.pygame_coords = [0, 0] # x,y
        self.pygame_radius = 32

    def init_pygame_val(self):
        if type(self.val) != list and type(self.val) != int and type(self.val) != List:
            return funcrepr(self.val)
        else: return str(self.val)

    def set_pygame_coords(self, x, y):
        self.pygame_coords[0], self.pygame_coords[1] = x, y

    def render(self):
        """ A circle with it's value should be rendered """
        pygame.draw.circle(self.screen, BLACK, self.pygame_coords, self.pygame_radius)
        self.pygame_textr.center = (self.pygame_coords[0], self.pygame_coords[1])
        self.screen.blit(self.pygame_text, self.pygame_textr)
# ------ Class Definition End ------


# ------ Class Definition Start ------
class NodeStructureGUI(NodeStructure):
    def __init__(self, screen):
        super(NodeStructureGUI, self).__init__()
        self.screen         = screen
        self.circle_objects = self.init_circle_objects()

    def init_circle_objects(self):
        render_matrix, x, y = [], 0, 0
        for arr in self.depth_hashmap.values():
            y += 75
            i_arr = []
            for node in arr:
                x += 75
                n_gui_obj = NodeGUI(node, self.screen)
                n_gui_obj.set_pygame_coords(x, y)
                i_arr.append(n_gui_obj)
            render_matrix.append(i_arr)
        return render_matrix

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