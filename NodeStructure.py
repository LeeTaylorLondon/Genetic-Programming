from Classes            import Node, List
from GlobalVariables    import func_set, obj_func, xt, term_set, whole_set, measure_fitness
from random             import randint as rand
from random             import random


""" -- Class Containing Nodes -- """
class NodeStructure:
    def __init__(self, root=None, depth_lim_lower=1, depth_lim_upper=3, gen_struc=True):
        if root is None: self.root = Node(func_set[rand(0, 3)], None, None, None)
        else: self.root = root
        self.depth_lim  = rand(depth_lim_lower, depth_lim_upper)
        self.depth_max  = self.depth_lim
        self.depth_hashmap = self.init_depth_hashmap()
        self.func_chance   = 0.5
        self.fitness = None
        self.queued  = False
        self.genetic_makeup = 'natural'
        # Generate structure of functions and terms
        if gen_struc: self.gen_structure()
        self.depth_lim = max(self.depth_lim, self.depth_max)

    ''' Depth methods '''
    def init_depth_hashmap(self):
        """ Initialise a blank hashmap starting with the root.
         Used in gen_structure to become multi-level.
         Used in crossover to represent the new structure. """
        rv = {0: [self.root]}
        for d in range(1, 16): rv.update({d: []})
        return rv

    def print_depth_hashmap(self, fitv=False, cval=False, objf=False, hidden=False):
        """ Outs each level of the hashmap. """
        rangevar = max(self.depth_lim, self.depth_max)
        if hidden:
            print(f"F: {round(measure_fitness(self), 3)}")
            for i,arr in enumerate(self.depth_hashmap.values()):
                if len(arr) != 0: print([(len(arr)) * " Φ "])
        return
        print("--------------------------------")
        print("self.depth_lim, self.depth_max", self.depth_lim, self.depth_max)
        for d in range(0, rangevar + 1):
            print(d, self.depth_hashmap.get(d))
        if fitv: print("fitv: " + str(measure_fitness(self)))
        if self.root.cval is not None and type(self.root.cval) is List:
            if cval: print("cval: " + str(self.root.cval.printv()))
            if objf: print("objf: " + str(obj_func(xt, out=False)))
        print("--------------------------------\n")

    def refresh_depth_hashmap(self, out=False):
        """ After a structure change the depth_hashmap
         needs to be updated to represent the new structure.
        """
        self.depth_hashmap = self.init_depth_hashmap()
        # for d in range(0, self.depth_lim):
        # for d in range(0, self.find_max_depth() + 1):
        for d in range(0, 8):
            # dn = node at depth, d.
            for dn in range(0, len(self.depth_hashmap[d])):
                lr = [self.depth_hashmap[d][dn].left,
                      self.depth_hashmap[d][dn].right]
                # Store children in depth_hashmap against depth
                left, right = lr[0], lr[1]
                if left is None and right is None: continue
                if left is not None and right is not None:
                    drtemp = right.eval_depth()
                    self.depth_hashmap[drtemp].append(left)
                    self.depth_hashmap[drtemp].append(right)
                elif left is None:
                    drtemp = right.eval_depth()
                    self.depth_hashmap[drtemp].append(left)
                    self.depth_hashmap[drtemp].append(right)
                elif right is None:
                    dltemp = left.eval_depth()
                    self.depth_hashmap[dltemp].append(left)
                    self.depth_hashmap[dltemp].append(right)
        pass

    def find_max_depth(self, update_self=True):
        """ Returns the height of the deepest Node.
         self.depth_max is updated. """
        # Init depth, max_depth, queue (q), queue_popped (qp)
        d, max_d = int(self.depth_lim), int(self.depth_lim)
        qp, q = [node for node in self.depth_hashmap[d]],\
                [node for node in self.depth_hashmap[d]]
        # While there are more Node(s) to process execute...
        while len(q) != 0:
            # Current node is popped from the queue
            node = q.pop()
            # Check current node depth is higher than max_depth
            if node.eval_depth() > max_d: max_d = node.eval_depth()
            # Append any children to the queue for processing
            if node.left is not None and node.left not in qp:
                q.extend([node.left])
                qp.append(node.left)
            if node.right is not None and node.right not in qp:
                q.extend([node.right])
                qp.append(node.right)
        # Update self.depth_max and return max_value found
        # if update_self: self.depth_max = max_d
        return max_d

    def set_node_depths(self):
        """ Set Node.depth for each Node in a NodeStruc
        Used for GUI/GUI.py """
        for arr in self.depth_hashmap.values():
            for node in arr:
                node.depth = node.eval_depth()

    ''' Generation methods '''
    def gen_node(self, parent, curr_depth, type_=-1):
        """ Generate an individual func. or term. as a Node """
        # Determine type of node
        if type_ not in [-1, 0, 1]:
            raise ValueError("NodeStructure.gen_node(...) param 'type_' must be one of [-1, 0, 1].")
        # Choose type
        if type_ == -1:
            type_ = rand(0, 1)
        # if type is function -> Random function
        if type_ == 0:
            rand_item = rand(0, len(whole_set[type_]) - 1)
        # if type is term -> Random term value
        else:
            # P%-chance for a term to be a constant or xt
            if random() > 0.5:
                rand_item = rand(1, len(whole_set[type_]) - 1)
            else:
                rand_item = 0
        # Construct Node
        node = Node(whole_set[type_][rand_item], None, None, parent)
        # Store a copy of xt as the value
        if node.val == xt:
            node.val = xt()
            print(node.val)
        return node

    def explore(self, out=False):
        unexplored = [self.root]
        i = 0
        while len(unexplored) != 0:
            popped = unexplored.pop()
            unexplored.append(popped.left)
            unexplored.append(popped.right)
            unexplored = [n for n in unexplored if n != None]
            if out: print(i, popped)
            i += 1
            yield popped

    def calc_max_depth(self):
        """ Calculate and return the maximum depth.
        todo: investigate why this returns 0 sometimes
            when it should not.
        """
        return_val = 0
        for node in self.explore():
            return_val = max(return_val, node.eval_depth())
        return return_val

    def change_self(self):
        ...

    def gen_children(self, node, types=[-1, -1]):
        """ list[int] : types == 0 or 1 """
        # Do not generate children for terminal nodes
        if node.type == 'term':
            return [node, node]
        # Generate 2 new nodes
        left  = self.gen_node(node, node.eval_depth(), types[0])
        right = self.gen_node(node, node.eval_depth(), types[1])
        # Link parents and children
        node.left = left
        node.right = right
        left.parent = node
        right.parent = node
        # Mark EOF
        return left, right

    def gen_structure(self):
        """ Generate a NodeStructure """
        # Generate a structure of nodes
        # While not at depth limit or no more branches
        nodes = [self.root]
        while self.calc_max_depth() != self.depth_lim and len(nodes) > 0:
            # Generate children
            current_node = nodes.pop()
            new_nodes = self.gen_children(current_node)
            # Store branches to generate further on
            for new_node in new_nodes:
                if new_node.eval_type() == 'func':
                    nodes.append(new_node)
        # Force ending nodes to be terms
        # Replace nodes at depth limit with terms :)
        for node in self.explore():
            if node.eval_depth() == self.calc_max_depth() - 1:
                self.gen_children(node, types=[1, 1])
            if node.eval_type() == 'func' and (node.left is None or node.right is None):
                print(f"node.eval_type() == 'func' and (node.left is None or node.right is None) -> "
                      f"{node, node.val, node.left, node.right}")
                new_nodes = self.gen_children(node, types=[1, 1])
        # Handle depth hashmap
        for node in self.explore():
            # Populate depth hashmap for interpreter to perform calculations for fitness calc.
            the_list = self.depth_hashmap.get(node.eval_depth())
            the_list.append(node)
            self.depth_hashmap.update({node.eval_depth(): the_list})
        # Depth hashmap, depth 0 is wrong - this solves it
        self.depth_hashmap.update({0: [self.depth_hashmap.get(0)[0]]})
        # ---
        # Out the nodes to the console
        print('NodeStructure.gen_structure()')
        for node in self.explore():
            print(node)
        print(self.depth_hashmap)
        print('NodeStructure.gen_structure() END')
        print()
        # Update the depth hashmap

        pass

    ''' Interpreter methods '''
    def interpreter(self, out=True):
        """ Interprets each depth of a NodeStructure,
         storing the calculated values in Node(s) under
         their attribute .cval. The final result is found
         in self.root.cval. """
        # Acquire matrix of nodes
        nodes_matrix = list(self.depth_hashmap.values())[::-1]
        nodes_matrix = [arr for arr in nodes_matrix if arr != []]
        # Debug
        print(f'node_structure_max_depth = {self.calc_max_depth()}')
        print(self.depth_hashmap)
        print(f'nodes_matrix = {nodes_matrix}')
        # Perform calculations
        for node_arr in nodes_matrix:
            for node in node_arr:
                if node.eval_type() == 'func':
                    # Derive left, right, parent nodes and values
                    l, r, p = node.left, node.right, node
                    try:
                        lv, rv, pv = l.val, r.val, p.val
                    except AttributeError as e:
                        print(f"l, r, p = {l, r, p}")
                        raise e
                    # Perform calculations
                    if l.cval is not None and r.cval is not None:
                        p.cval = pv(l.cval, r.cval)
                    elif l.cval is not None:
                        p.cval = pv(l.cval, rv)
                    elif r.cval is not None:
                        p.cval = pv(lv, r.cval)
                    else:
                        p.cval = pv(lv, rv)
                    print(f"p.cval = {p.cval}")
        # Debug
        print(f"self.root.cval = {self.root.cval}")
        print(f"self.root = {self.root}")
        print(f"self.depth_hashmap.values())[0][0] = {list(self.depth_hashmap.values())[0][0]}")
        print(f"list(self.depth_hashmap.values())[0][0] == self.root = {list(self.depth_hashmap.values())[0][0] == self.root}")
        self.root.cval = list(self.depth_hashmap.values())[0][0].cval
        return self.root.cval


    def reset_cval_all_c(self):
        for d in range(0, 8):
            for dn in range(0, len(self.depth_hashmap[d]) - 1):
                node = self.depth_hashmap[d][dn]
                if type(node.cval) == List:
                    while len(node.cval) != 0:
                        del node.cval[0]
                    node.cval = xt()
                else:
                    del node.cval
                    node.cval = None
        pass

    ''' GeneticProgram (class) methods '''
    def rand_node(self, ntype=None, nstruc=None, debug=False):
        """ Return: reference to random Node in NodeStructure.

        You may determine the type of Node returned, function or term
         default is random-type. :param: ntype
        You may determine the NodeStructure, default is self.
         :param: nstruc
        """
        node_arr = []
        if ntype is None:  ntype  = ['term', 'func'][rand(0, 1)]
        # if debug: print("ntype", ntype)
        if nstruc is None: nstruc = self
        # For every list of Node(s)
        for arr in list(nstruc.depth_hashmap.values())[0][1:]:
            if len(arr) == 0: break
            for elm in arr:
                if elm.eval_type() == ntype:
                    node_arr.append(elm)
        if len(node_arr) == 0:
            # print(list(nstruc.depth_hashmap.values())) # DEBUG
            dept_arr = list(nstruc.depth_hashmap.values())[1]
            node_arr = [dept_arr[rand(0, len(dept_arr) - 1)]]
            # raise TypeError(".rand_node() returned None")
        if len(node_arr) == 1: return node_arr[0]
        return node_arr[rand(0, len(node_arr) - 1)]

    ''' Other methods '''
    def yield_all_nodes(self):
        """ Yields each Node from a collection of Node(s) """
        q = [self.root]
        while len(q) != 0:
            q_top = q.pop()
            if isinstance(q_top.left, Node) and q_top.left is not None:
                q.append(q_top.left)
            if isinstance(q_top.right, Node) and q_top.right is not None:
                q.append(q_top.right)
            yield q_top, q
            if q is []: return
        return

    def count_funcs(self):
        """ For function node is counted, count is returned """
        ynodes, count = self.yield_all_nodes(), 0
        while True:
            yield_return = ynodes.next()
            if yield_return[0].eval_type() == 'func': count += 1
            if len(yield_return[1]) == 0:
                return count

    def print_all_nodes(self):
        """ For the data of each node in a collection is printed to the console """
        ynodes = self.yield_all_nodes()
        print("nodes.depth_lim -> " + str(self.depth_lim))
        while True:
            yield_return = ynodes.next()
            print("nodes.next() -> " + str(yield_return[0]))
            if len(yield_return[1]) == 0:
                return

    def __copy__(self):
        rootc, og   = self.root.__copy__()
        q, qnext    = [], []
        # Queue the originals (not copies to check for children)
        # ... and to copy from
        rootc.left  = og.left.__copy__(q)
        rootc.right = og.right.__copy__(q)
        rootc.left.parent, rootc.right.parent, = rootc, rootc
        # Linking loop
        while len(q) != 0:
            copy, og = q.pop()
            if not og.has_children(): continue
            copy.left  = og.left.__copy__(q)
            copy.right = og.right.__copy__(q)
            copy.left.parent, copy.right.parent = copy, copy
        pass
        # End - Create NodeStructure from root value and return
        rv = NodeStructure(root=rootc, gen_struc=False)
        rv.refresh_depth_hashmap()
        # Debug Debug Debug Debug
        # print(">>> NodeStructure.__copy__(self) <<<")
        # rv.print_depth_hashmap()
        # Find max depth
        max_depth = 0
        while True:
            if len(self.depth_hashmap[max_depth]) != 0:
                max_depth += 1
            else:
                break
        rv.depth_max = max_depth - 1
        rv.genetic_makeup = 'copy'
        return rv

    def __str__(self):
        # try:
        #     return "<NS" + " D:" + str(self.depth_max) + " " + "F:" + str(measure_fitness(self, True)) + ">"
        # except (AttributeError, TypeError) as e:
        #     print('self.depth_max', self.depth_max)
        #     print('self.depth_hashmap', self.depth_hashmap)
        #     raise e
        return f'<NS {round(float(measure_fitness(self)), 2)}>'
        # return "<NS>"

    def __repr__(self):
        return self.__str__()

