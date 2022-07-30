from Classes import List
from types import FunctionType


# -- Function set definitions & other functions --
def add(x, y):
    if type(y) is List: return y.__add__(x)
    if type(y) is float and type(x) is not List: x, y = float(x), float(y)
    return x.__add__(y)

def sub(x, y):
    if type(y) is List: return y.__sub__(x)
    if type(y) is float and type(x) is not List: x, y = float(x), float(y)
    return x.__sub__(y)

def mul(x, y):
    if type(y) is List: return y.__mul__(x)
    if type(y) is float and type(x) is not List: x, y = float(x), float(y)
    return x.__mul__(y)

def div(x, y):
    if y == 0: return x
    if type(y) is List: return y.__truediv__(x)
    if type(y) is FunctionType: raise TypeError("other is type 'function'")
    if type(y) is float and type(x) is not List: x, y = float(x), float(y)
    return x.__truediv__(y)

def obj_func(x, out=True):
    """ Objective behaviour as a function """
    if x is None: x = [float(x)/10 for x in range(-10, 11, 1)]
    y = []
    for xi in x: y.append((xi * xi) + xi + 1)
    if out: print("Desired output -> " + str(y))
    return y

def measure_fitness(nstruc, clear_cval=False):
    """ Outputs the absolute summed difference of
     the object fucntion and generated NodeStructure. """
    desired_y   = obj_func(None, out=False)
    produced_y  = nstruc.interpreter(out=False)
    summed_diff = 0
    if type(produced_y) is List:
        for dy,py in zip(desired_y, produced_y):
            summed_diff += abs(py - dy)
    else:
        for dy in desired_y:
            try:
                summed_diff += abs(produced_y - dy)
            except TypeError as e:
                print("-----DEBUG------")
                nstruc.print_depth_hashmap()
                print("inter-val: ", nstruc.interpreter())
                raise e
    nstruc.fitness = summed_diff
    if clear_cval: nstruc.reset_cval_all_c()
    del desired_y, produced_y
    return summed_diff

def return_xt():
    rv = [float(n_)/10 for n_ in range(-10, 11, 1)]
    rv = List(rv)
    return rv

# -- Global variables --
# xt = [float(n_)/10 for n_ in range(-10, 11, 1)]
# xt = List(xt)
xt = return_xt
func_set  = (sub, add, mul, div)
term_set  = (xt(), -5, -4, -3, -2, -1, 1, 2, 3, 4, 5) # Omitted 0
whole_set = (func_set, term_set)
