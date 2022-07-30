from Classes import NodeStructure


for _ in range(100):
    ns1 = NodeStructure(depth_lim_lower=2)
    print(ns1.interpreter())
