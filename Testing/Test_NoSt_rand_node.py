from Classes import NodeStructure


ns1 = NodeStructure(depth_lim_lower=3, depth_lim_upper=3)

while True:
    print(ns1.rand_node())
    print(ns1.rand_node(ntype='term'), 'term')
    print(ns1.rand_node(ntype='func'), 'func')
