from random import random
from random import randint as rand
from GlobalVariables import func_set, xt, term_set
from Classes import List


""" CLASS Node Definition """
class Node:
    def __init__(self, val, left=None, right=None, parent=None):
        # if not term_set.__contains__(val) and not func_set.__contains__(val):
        #     print(val, type(val))
        #     try:
        #         print("len(val) ->", len(val))
        #         print(val.printv())
        #     except AttributeError as e:
        #         pass
        #     raise TypeError("Unaccepted val to create Node()!")
        self.val = val
        # if val is xt: self.val = xt.__copy__()
        self.cval   = None # Collapsed/Calculated Value
        self.type   = self.eval_type()
        self.left   = left
        self.right  = right
        self.parent = parent
        self.queued = False
        self.mark_calc = False # Denotes if it's already added to a calculation

    def has_children(self):
        if self.left is not None and self.right is not None: return True
        else: return False

    def eval_type(self):
        if func_set.__contains__(self.val): return "func"
        return "term"

    def eval_depth(self):
        curr_node, depth = self, 0
        while curr_node.parent is not None:
            curr_node = curr_node.parent
            depth += 1
        return depth

    def chance_switch(self):
        if self.eval_type() == "func":
            if random() > 0.1: self.force_switch()
        elif self.eval_type() == "term":
            if random() > 0.9: self.force_switch()

    def force_switch(self):
        if self.eval_type() == "term":
            self.val = func_set[rand(0, len(func_set) - 1)]
        if self.eval_type() == "func":
            self.val = term_set[rand(0, len(term_set) - 1)]

    def printf(self, inp):
        """ Replacement for print_func() """
        if type(inp) is list:
            rv = ""
            for e in inp:
                if str(type(e)).__contains__('function'):
                    rv = rv + str(e).split(" ")[1] + " "
                else:
                    rv = rv + str(e) + " "
            return rv
        elif str(type(inp)).__contains__('function'):
            return str(inp).split(" ")[1]
        return str(inp)

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        if self.cval is None: return "<D=" + str(self.eval_depth()) + "|" + self.printf(self.val) + ">"
        else: return "<D=" + str(self.eval_depth()) + "|" + self.printf(self.val) + "|" + self.printf(self.cval) + ">"

    def __copy__(self, arr=None):
        """ Node Attrs: val, cval, type, left, right, parent, mark_Calc, queued
        Creates a reference to the newly created Node and the Node 'Copied FROM'.
        """
        if arr is not None:
            # 'rv' = new copy, 'self' = original Node
            if type(self.val) is List: val_copy = self.val.__copy__()
            else: val_copy = self.val
            rv = Node(val_copy)
            arr.append([rv, self])
            return rv
        return Node(self.val), self
