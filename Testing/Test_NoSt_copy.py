from Classes import NodeStructure
from GlobalVariables import func_set


ns1 = NodeStructure()
ns1.print_depth_hashmap()

nsc = ns1.__copy__()
nsc.print_depth_hashmap()

print("func_set[0] -> " + str(func_set[0]))
ns1.root.val = func_set[0]
ns1.print_depth_hashmap()

nsc.print_depth_hashmap()

nsc.root.left.val = 99
nsc.print_depth_hashmap()
