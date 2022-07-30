# def add(x, y):
#     if type(y) is List: return y.__add__(x)
#     return x.__add__(y)
#
# def sub(x, y):
#     if type(y) is List: return y.__sub__(x)
#     return x.__sub__(y)
#
# def mul(x, y):
#     if type(y) is List: return y.__mul__(x)
#     return x.__mul__(y)
#
# def div(x, y):
#     if y is 0: return x
#     if type(y) is List: return y.__div__(x)
#     return x.__div__(y)
#
#
# def obj_func(x, out=True):
#     """ Objective behaviour as a function """
#     if x is None: x = [float(x)/10 for x in range(-10, 11, 1)]
#     y = []
#     for xi in x: y.append((xi * xi) + xi + 1)
#     if out: print("Desired output -> " + str(y))
#     return y
#
# def measure_fitness(nstruc):
#     """ Outputs the absolute summed difference of
#      the object fucntion and generated NodeStructure. """
#     desired_y = obj_func(None, out=False)
#     produced_y = nstruc.interpreter(out=False)
#     summed_diff = 0
#     if type(produced_y) is List:
#         for dy,py in zip(desired_y, produced_y):
#             summed_diff += abs(py - dy)
#     else:
#         for dy in desired_y:
#             summed_diff += abs(produced_y - dy)
#     nstruc.fitness = summed_diff
#     return summed_diff
# def crossover(self, other, out=False):
#         """ Replace a subtree in the structure
#          with subtree from another structure. """
#         # Reset calculated values as they take priority during calculations
#         self.reset_cval_all_c()
#         other.reset_cval_all_c()
#         # Random depth and random Node, self.
#         ntype = random()
#         if ntype <= 0.9: n1 = self.rand_node(ntype='func', nstruc=self)
#         else:            n1 = self.rand_node(ntype='term', nstruc=self)
#         if n1 is None:
#             print(n1)
#             print(self.depth_hashmap)
#             print(self.rand_node(ntype='func', nstruc=self, debug=True))
#             print("------------------------")
#             print(self.rand_node(ntype='term', nstruc=self, debug=True))
#             raise TypeError("n1 is None, program failed!")
#         # Determine function or leave to crossover
#         if ntype <= 0.9: n2 = self.rand_node(ntype='func', nstruc=other)
#         else:            n2 = self.rand_node(ntype='term', nstruc=other)
#         # Create reference to parent to update the crossover'd Node
#         if n1.parent is not None: parent_ref = n1.parent
#         # Perform crossover
#         n1.val = n2.val         # Swap values
#         n1.left = n2.left       # Swap left child
#         n1.right = n2.right     # Swap right child
#         if n1.parent is not None: n1.parent = parent_ref  # Swap parent
#         if n1.eval_type() == 'func':
#             n1.left.parent = n1  # Swap parent for left child
#             n1.right.parent = n1 # Swap parent for right child
#         # Refresh self.depth_hashmap
#         self.refresh_depth_hashmap()
#         if out: print("---- REFRESHED DEPTH HASHMAP ----")
#         if out:
#             print("fitv: " + str(measure_fitness(self)))
#             self.print_depth_hashmap(fitv=True, cval=True, objf=True)
#         pass
