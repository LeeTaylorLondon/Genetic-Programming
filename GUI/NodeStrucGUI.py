import pygame.draw
from Classes import NodeStructure, Node, List
from GlobalVariables import measure_fitness, funcrepr, len_
from Consts import BLACK, WHITE, D_BLUE, DRED, create_text, create_text_str
from NodeGUI import NodeGUI


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
class NodeStructureGUI(NodeStructure):
    def __init__(self, screen):
        super(NodeStructureGUI, self).__init__()
        self.screen         = screen
        self.spacingx       = 45
        self.spacingy       = 45
        self.circle_objects = self.init_circle_objects()
        self.root           = self.circle_objects[0][0] # NodeGUI
        self.pixel_width    = self.calc_pixel_width()
        self.pixel_height   = self.calc_pixel_height()
        self.hitbox         = self.init_hitbox() # Rect = [x, y, w, h]
        # self.init_hitbox()
        self.init_lrp()

    def calc_pixel_width(self):
        """ Calculates and returns the pixel width
        WITHOUT padding width of the NodeStructure """
        longest_len_i, longest_len_val = -1, -1
        for i, arr in enumerate(self.circle_objects):
            if len(arr) > longest_len_val:
                longest_len_i, longest_len_val = i, len(arr)
        # Width_of_Nstruc = (2*Radius) + Spacing(#Nodes - 1) + Padding
        warr = self.circle_objects[longest_len_i]  # 'w'arr = 'widest' array
        l, r, s = len(warr), warr[0].pygame_radius, self.spacingx  # Radius, Node-Spacing
        spacing = (2 * r) + (s * (l - 1))
        return spacing

    def calc_pixel_height(self):
        l, r, s = len_(self.circle_objects), self.root.pygame_radius, self.spacingy
        spacing = (2 * r) + (s * (l - 1))
        return spacing

    def init_circle_objects(self):
        """ Returns a matrix storing arrays which store NodeGUI-obj's
         also sets the x,y for each object to be rendered at. """
        render_matrix, y = [], 0
        for arr in self.depth_hashmap.values():
            y += self.spacingy
            x, i_arr = 0, []
            for node in arr:
                x += self.spacingx
                n_gui_obj = NodeGUI(node, self.screen)
                n_gui_obj.set_pygame_coords(x, y)
                i_arr.append(n_gui_obj)
            render_matrix.append(i_arr)
        return render_matrix

    def init_lrp(self):
        """ Initialises self.l, self.r, and self.p (left, right, parent)
        this is used for rendering purposes to render 'lined' links between
        parents and children.
        Selects 'one' then assigns l,r by selecting below 'two'. """
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

    def init_hitbox(self):
        x, y = self.root.pygame_coords
        r    = self.root.pygame_radius
        pad  = 10
        hitbox = [x - r - pad, y - r - pad, self.pixel_width + (2 * pad), self.pixel_height + (2 * pad)]
        return hitbox

    def render(self):
        """ For each array storing a list of NodeGUI objects
         it calls their render method. """
        for array in self.circle_objects:
            for node in array:
                node.render()
        self.render_hitbox()

    def render_hitbox(self):
        pygame.draw.rect(self.screen, DRED, self.hitbox, width=1)

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return f"<NS-GUI {round(float(measure_fitness(self)), 2)}>"
# ------ Class Definition End ------


if __name__ == '__main__':
    nsgui = NodeStructureGUI()
    print(nsgui)