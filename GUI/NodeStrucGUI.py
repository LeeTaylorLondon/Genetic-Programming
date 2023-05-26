from Classes         import NodeStructure, Node, List
from GlobalVariables import measure_fitness, funcrepr, len_
# from GUI.Consts      import BLACK, WHITE, D_BLUE, DRED, create_text, create_text_str, CGREEN, RED
# from NodeGUI         import NodeGUI
import pygame.draw


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


"""
class NodeStructure:
    def __init__(self, root=None, ..., gen_struc=True):
        if root is None: 
            self.root = Node(func_set[rand(0, 3)], None, None, None)
        else: 
            self.root = root
        self.depth_hashmap = self.init_depth_hashmap()
        ...
        # Generate structure of functions and terms
        if gen_struc: self.gen_structure()
"""


WHITE   = (255, 255, 255)
L1BLACK = (25, 25, 25)
BLACK   = (0, 0, 0)
D_BLUE  = (0, 32, 96)
DRED    = (125, 0, 0)
CGREEN  = (0, 145, 0)
RED     = (145, 0, 0)


def create_text(arr, font_size, color=BLACK) -> List[pygame.font.SysFont]:
    rv = []
    font = pygame.font.SysFont('chalkduster.tff', font_size)
    if type(arr) == list:
        for string in arr:
            rv.append(font.render(string, True, color))
    elif type(arr) == str:
        rv.append(font.render(arr, True, color))
    return rv

def create_text_str(arr, font_size, color=BLACK) -> pygame.font.SysFont:
    font = pygame.font.SysFont('chalkduster.tff', font_size)
    if type(arr) == list:
        raise TypeError("Use function create_text(...)")
    elif type(arr) == str:
        return font.render(arr, True, color)


# ------ Class Definition Start ------
class NodeGUI(Node):
    def __init__(self, node, screen, left_=None, right_=None, parent_=None, debug=False):
        super(NodeGUI, self).__init__(val=node.val, left=left_, right=right_, parent=parent_)
        self.node          = node
        self.l             = None
        self.r             = None
        self.p             = None
        self.screen        = screen
        self.color         = CGREEN
        if debug: return
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


# ------ Class Definition Start ------
class NodeStructureGUI(NodeStructure):
    def __init__(self, screen, root=None, depth_lim_lower=1, depth_lim_upper=3, gen_struc=True, ns=None):
        # Todo: pass NodeStructure to NodeStructureGUI(...) to inherit it's values
        """ WIP """
        if ns != None:
            gen_struc = self.inherit_(ns, screen)
        """ ^^ WIP ^^ """
        super(NodeStructureGUI, self).__init__()
        self.screen         = screen
        self.spacingx       = 45
        self.spacingy       = 45
        self.pad            = 10
        self.botboxh        = 25
        self.color          = CGREEN
        self.circle_objects = self.init_circle_objects()
        self.root           = self.circle_objects[0][0] # NodeGUI
        """ Debug : Start """
        if ns != None:
            self.depth_hashmap  = ns.depth_hashmap
            self.circle_objects = self.init_circle_objects()
            # print(f"DEBUG: {self.circle_objects}")
            self.root           = self.circle_objects[0][0]  # NodeGUI
            int_out = self.interpreter()
            print(f"NodeStructureGUI(NodeStructure).self.interpreter() = {int_out}")
            # print(self.depth_hashmap)
        """ Debug : End """
        self.pixel_width    = self.calc_pixel_width()
        self.pixel_height   = self.calc_pixel_height()
        self.hitbox         = self.init_hitbox()        # Rect = [x, y, w, h]
        self.botbox         = self.init_botbox()
        self.pygame_fitness = self.init_pygame_fitness()
        # self.init_hitbox()
        self.init_lrp()

    def inherit_(self, ns, screen):
        # gen_struc = False             # Do not generate new structure
        # nshashmp  = ns.depth_hashmap  # Shortcut to depth_hashmap
        # """ For loop changes each object.type to -> GUI-counter-part """
        # for i, arr in enumerate(ns.depth_hashmap.values()):
        #     for i, node in enumerate(arr):
        #         print(f"node .left .right = {node, node.left, node.right}")
        #         arr[i] = NodeGUI(node, screen, left_=node.left, right_=node.right, parent_=node.parent)
        #         print(f"node .left .right = {node, node.left, node.right}\n")
        #     nshashmp[i] = arr
        # self.ns = nshashmp
        # return gen_struc
        pass

    def apply_y_offset(self, y_offset):
        """ This allows the user to scroll down """
        for arr in self.circle_objects:
            for node in arr:
                node.pygame_coords[1] = node.pygame_coords[1] + y_offset
        self.hitbox[1] += y_offset
        self.botbox[1] += y_offset

    def nodes_to_nodesgui(self):

        pass

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
        l, r, s, bbh = len_(self.circle_objects), self.root.pygame_radius, self.spacingy, self.botboxh
        spacing = (2 * r) + (s * (l - 1)) + abs(bbh)
        return spacing

    def init_pygame_fitness(self):
        f = "F: " + str(round(measure_fitness(self, True), 2))
        x, y, s = self.hitbox[0], self.pixel_height, create_text_str(f, 22, self.color)
        return [x, y, s] # x:int, y:int, s:pygame.text

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
        hitbox = [x - r - self.pad, y - r - self.pad,
                  self.pixel_width + (2 * self.pad),
                  self.pixel_height + (2 * self.pad)]
        return hitbox

    def init_botbox(self):
        r = self.root.pygame_radius
        x = self.root.pygame_coords[0] - r - self.pad
        y = self.calc_pixel_height() + self.root.pygame_coords[1] + self.pad - r
        w = self.calc_pixel_width() + (2 * self.pad)
        h = self.botboxh
        return [x, y - 1, w, h] # x, y, w, h

    def render(self):
        """ For each array storing a list of NodeGUI objects
         it calls their render method. """
        for array in self.circle_objects:
            for node in array:
                node.render()
        self.render_hitbox()
        self.render_botbox()
        self.render_fitness()

    def render_botbox(self):
        pygame.draw.rect(self.screen, self.color, self.botbox, width=1)

    def render_fitness(self):
        s = self.pygame_fitness[2]
        self.screen.blit(s, (self.botbox[0] + self.pad, self.botbox[1] + (self.pad / 2)))

    def render_hitbox(self):
        pygame.draw.rect(self.screen, self.color, self.hitbox, width=1)

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return f"<NS-GUI {round(float(measure_fitness(self)), 2)}>"
# ------ Class Definition End ------


if __name__ == '__main__':
    nsgui = NodeStructureGUI()
    print(nsgui)