from Classes import Node, List
from GlobalVariables import func_set, obj_func, xt, term_set, whole_set, measure_fitness
from random import randint as rand
from random import random


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
        for d in range(1, 8): rv.update({d: []})
        return rv

    def print_depth_hashmap(self, fitv=False, cval=False, objf=False):
        """ Outs each level of the hashmap. """
        rangevar = max(self.depth_lim, self.depth_max)
        print("self.depth_lim, self.depth_max", self.depth_lim, self.depth_max)
        for d in range(0, rangevar + 1):
            print(d, self.depth_hashmap.get(d))
        if fitv: print("fitv: " + str(measure_fitness(self)))
        if self.root.cval is not None and type(self.root.cval) is List:
            if cval: print("cval: " + str(self.root.cval.printv()))
            if objf: print("objf: " + str(obj_func(xt, out=False)))
        print("--------------------------------")

    def refresh_depth_hashmap(self, out=False):
        """ After a structure change the depth_hashmap
         needs to be updated to represent the new structure. """
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

    ''' Generation methods '''
    def gen_node(self, parent, curr_depth, forcef=False):
        """ Generate an individual func. or term. as a Node """
        # Force leaves (Node(s) @ depth_lim) to become terms
        if curr_depth + 1 == self.depth_lim: t_or_f = 1 # set to term
        else: t_or_f = rand(0, len(whole_set) - 1)
        if forcef: t_or_f = 0
        # Choose random function
        if t_or_f == 0: rand_item = rand(0, len(whole_set[t_or_f]) - 1)
        # Choose random term where x has a P%-chance to be chosen
        else:
            x_or_c = random()
            # P%-chance for a term to be a constant or xt
            if x_or_c > 0.5: rand_item = rand(1, len(whole_set[t_or_f]) - 1)
            else: rand_item = 0
        # Construct Node
        node = Node(whole_set[t_or_f][rand_item], None, None, parent)
        # Store a copy of xt as the value
        if node.val == xt:
            node.val = xt()
            print(node.val)
        return node

    def gen_structure(self):
        """ Generate a collection of linked nodes """
        # Queue of nodes to have children
        nodes = [self.root]
        # Stop gen no more children
        while len(nodes) != 0:
            # Set current_node to nodes[0] & del nodes[0]
            current_node = nodes.pop()
            # Prevent adding children to terminal nodes
            if current_node.type == "term": continue
            # Create left & right Nodes
            lr = [self.gen_node(current_node, current_node.eval_depth()),
                  self.gen_node(current_node, current_node.eval_depth())]
            left, right = lr[0], lr[1]
            """ This should be across an entire level not just left and right """
            # Force switch when .depth_lim is not reached & depth is only terms
            if term_set.__contains__(left.val) and term_set.__contains__(right.val) and\
                current_node.eval_depth() + 1 < self.depth_lim:
                lr[rand(0, 1)] = self.gen_node(current_node, current_node.eval_depth(), forcef=True)
                left, right = lr[0], lr[1] # Update left, right values
            # Force ending nodes into terms
            if current_node.eval_depth() + 1 == self.depth_lim and len(nodes) == 0:
                for node in self.depth_hashmap.get(self.depth_lim):
                    if node.eval_type() == 'func': node.force_switch()
            # Set children nodes to left and right
            current_node.left, current_node.right = left, right
            # Store children in depth_hashmap against depth
            # Use .extend method to enforce a specific order
            lr.extend(self.depth_hashmap[left.eval_depth()])
            self.depth_hashmap[left.eval_depth()] = lr
            # Append left and right node to queue
            if current_node.eval_depth() + 1 != self.depth_lim:
                nodes.append(current_node.left)
                nodes.append(current_node.right)
        self.refresh_depth_hashmap()
        # Find max depth
        max_depth = 0
        while True:
            if len(self.depth_hashmap[max_depth]) != 0:
                max_depth += 1
            else:
                break
        self.depth_max = max_depth - 1
        pass

    ''' Interpreter methods '''
    def interpreter(self, out=True):
        """ Interprets each depth of a NodeStructure,
         storing the calculated values in Node(s) under
         their attribute .cval. The final result is found
         in self.root.cval. """
        self.reset_cval_all_c()
        # curr_depth = self.depth_lim
        # curr_depth = max(self.depth_max, self.depth_lim)
        curr_depth = 3
        while curr_depth != -1:
            nodes = self.depth_hashmap[curr_depth]
            for n in range(0, len(nodes) - 1, 2):
                l, r, p = nodes[n], nodes[n+1], nodes[n].parent
                lv, rv, pv = l.val, r.val, p.val
                if l.parent != r.parent: raise TypeError("Mismatching Parents!")
                # Calculations + try-catch
                try:
                    if l.cval is not None and r.cval is not None:
                        p.cval = pv(l.cval, r.cval)
                    elif l.cval is not None: p.cval = pv(l.cval, rv)
                    elif r.cval is not None: p.cval = pv(lv, r.cval)
                    else: p.cval = pv(lv, rv)
                # Calculations -> catch
                except TypeError as e:
                    self.print_depth_hashmap()
                    print(lv, rv, l.cval, r.cval)
                    raise e
                # Debug
                if out: print('.interpreter() -> | Depth:', curr_depth, '|Result:', p.cval)
                if out and type(p.cval) == List: p.cval.printv()
                # Assign calculated root value
                # Todo: fix NotImplemented either assignment error
                # Todo: or incorrect
                self.root.cval = p.cval
            curr_depth -= 1
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

    def isleft(self, node, debug=False):
        """ Returns TRUE if the node is the left of another node
         otherwise returns false. """
        for depthlevel in self.depth_hashmap.values():
            if node in depthlevel:
                # Debug
                if debug:
                    print("---DEBUG---")
                    print("depthlevel:", depthlevel)
                    print("node:", node)
                    print("depthlevel.index(node):", depthlevel.index(node))
                    print("^ % 2 == 0", depthlevel.index(node) % 2)
                    print("---DEBUG---")
                # Debug
                return depthlevel.index(node) % 2 == 0
        raise TypeError("isleft should have returned False or True")

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
        q, qnext = [], []
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

