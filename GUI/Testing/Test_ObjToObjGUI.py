from Classes            import Node, NodeStructure, List
from GlobalVariables    import funcrepr
from GUI.NodeGUI        import NodeGUI


ns   = NodeStructure()
n    = ns.root
nsrl = n.left.val
nsrr = n.right.val
nsrlstr, nsrrstr = " Φ ", " Φ "


def str_(node_value):
    if type(node_value) not in [int, list, List]:
        return f"({funcrepr(node_value)})"
    else: return str(node_value)


nsrlstr = str_(n.left.val)
nsrrstr = str_(n.right.val)


ns.print_depth_hashmap(hidden=True)
print()
print(f"n.val={funcrepr(ns.root.val)} n.left={nsrlstr} n.right={nsrrstr}")


nrgui = NodeGUI(n, screen=None, debug=True, left_=n.left, right_=n.right, parent_=n.parent) # Node-Root-GUI


nsrlstr2, nsrrstr2 = " Φ ", " Φ "
nsrlstr2 = str_(nrgui.left.val)
nsrrstr2 = str_(nrgui.right.val)


print()
print(f"n.val={funcrepr(ns.root.val)} n.left={nsrlstr} n.right={nsrrstr}")
