from Classes import NodeStructure, GeneticProgram
from GlobalVariables import func_set, measure_fitness

# Testing NodeStructure.__copy__()
# nsObj = NodeStructure()
# nsObjC = nsObj.__copy__()

# Testing generation depth 3
""" 
Naming: nsd31 -> NodeStructureDepth3[Instance]1
Results: 
 Depth 3 - Good! 
"""
# nsd31 = NodeStructure(depth_lim_lower=3, depth_lim_upper=3)
# strucs = [nsObj, nsObjC, nsd31]

# AttributeError: 'int' object has no attribute '__div__'
# Testing ^^^
x, y = 4, 4
print(x.__truediv__(y))
print(4 / 4)

# Testing Genetic Program
runs = 1350
for _ in range(runs):
    print('>>>', _, '<<<')
    print('S1')
    gp   = GeneticProgram()
    print('S2')
    # Todo: fix infinite loop >here<
    sarr = gp.selection()
    print('S3')
    gp._crossover(sarr)
print (str(runs) + " runs complete!")

# random_node = nsObj.rand_node()
# truth_value = nsObj.isleft(random_node)
def test_isleft():
    rn = nsObj.rand_node()
    tv = nsObj.isleft(rn)
    print(rn, tv)

def outf(arr=None, out=False):
    """ Print fitness for each population member """
    if arr is None:
        pass
        # arr = strucs
    rv = "|"
    for struc in arr: rv = rv + str(round(measure_fitness(struc), 3)) + "|"
    if out: print(rv)
    return rv

