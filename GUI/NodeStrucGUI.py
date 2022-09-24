import pygame.draw
from Classes import NodeStructure
from GlobalVariables import measure_fitness
from Consts import BLACK, WHITE, D_BLUE, create_text

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
    def __init__(self, screen):
        super(NodeGUI, self).__init__()
        self.screen        = screen
        self.render_matrix = []
        self.pygame_text   = create_text(self.val, 12)
        self.pygame_textr  = self.pygame_text.get_rect()
        self.pygame_coords = [0, 0] # x,y
        self.pygame_radius = 18

    def render(self):
        """ When called a circle with it's value should be rendered """
        pygame.draw.circle(self.screen, BLACK, self.pygame_coords, self.pygame_radius)
        self.textr.center = (self.pygame_coords[0], self.pygame_coords[1])
        self.screen.blit(self.pygame_text, self.pygame_textr)
# ------ Class Definition End ------


# ------ Class Definition Start ------
class NodeStructureGUI(NodeStructure):
    def __init__(self):
        super(NodeStructureGUI, self).__init__()
        self.circle_objects = []

    def init_circle_objects(self):
        for arr in self.depth_hashmap:
            i_arr = []
            for node in arr:
                i_arr.append(node)
            self.render_matrix.append(i_arr)

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return f"<NS-GUI {round(float(measure_fitness(self)), 2)}>"
# ------ Class Definition End ------


if __name__ == '__main__':
    nsgui = NodeStructureGUI()
    print(nsgui)