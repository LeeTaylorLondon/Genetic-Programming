from Classes import NodeStructure, Node
from GlobalVariables import measure_fitness, obj_func, term_set, func_set
from random import random as rf
from random import randint as rand
from typing import List


class GeneticProgram:
    def __init__(self, count=4):
        self.pcount = count
        self.population = [NodeStructure() for _ in range(count)]
        # self.pm = [[ns.__copy__() for ns in self.population]]

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return str(self.population)

    def fitness_check(self):
        """ Check fitness of each population member """
        for i, p in enumerate(self.population):
            # if fitness of p is 0 then replace that one by index
            if measure_fitness(p, False) == 0.0:
                return i
        return -1

    def fitness_check_desired(self, i):
        """ class.GeneticProgram.fitness_check() returns the index
        of a population member with 0.0 fitness. This function checks
        the equality of the computed-value and objective-function.
        Computed-value from the population member with a fitness of 0.
        """
        root_cval = self.population[i].root.cval
        objective = obj_func(None, out=False)
        for x, y in zip(root_cval, objective):
            if x != y: return False
        return True

    def selection(self, debug=False):
        """ Select a population member proportionate to the
        fitness of the population """
        farr = [measure_fitness(ns) for ns in self.population]
        plis = [f / sum(farr) for f in farr]
        # Roll probability values
        roll = [plis[0]]
        for i, v in enumerate(plis[1:]):
            roll.append(v + roll[i])
        roll[-1] = 1.0
        # Compare random-float and random-probability
        rfv, rv = rf(), -1
        for rp in roll[::-1]:
            if rfv < rp: rv = roll.index(rp)
        # Debug
        if debug:
            print(f"plis={plis}\nroll={roll}\nrv={rv}")
        return rv

    def _rand_node(self, structure: NodeStructure):
        # Get matrix of nodes and remove empty layers
        node_matrix = list(structure.depth_hashmap.values())
        node_matrix = [_ for _ in node_matrix if _ != []]
        print(f"_rand_node.node_matrix = {node_matrix}")
        # Remove top and bottom layers
        # node_matrix.pop() # Remove bottom layer
        node_matrix.reverse()
        node_matrix.pop()  # Remove top layer
        # Debug
        print(f"_rand_node.node_matrix = {node_matrix}")
        rand_arr = rand(0, len(node_matrix) - 1)
        rand_nod = rand(0, len(node_matrix[rand_arr]) - 1)
        return node_matrix[rand_arr][rand_nod]

    def crossover(self, debug=False):
        # Select two structures, s1 and s2
        selections = [1, 1]
        while selections[0] == selections[1]:
            selections[0] = self.selection()
            selections[1] = self.selection()
        s1, s2 = self.copy(selections[0]), self.copy(selections[1])
        # s1, s2 = self.population[selections[0]], self.population[selections[1]]
        # Choose two random nodes and children n1, n2, n1l, n1r, n2l, n2r
        n1, n2 = self._rand_node(s1), self._rand_node(s2)
        n1l, n1r, n2l, n2r = n1.left, n1.right, n2.left, n2.right
        #
        print("reached end")
        pass

    def copy(self, population_member_index=0):
        """ Return an equal structure made up of copied nodes. """
        # For each node assign it an NID (NID = f'self.explore().index(node),{str(node.val)}'
        unlinked_copied_nodes = []
        nodes = list(self.population[population_member_index].explore())
        # Generate NIDs
        # Make a list of unlinked nodes with equal values
        for node in nodes:
            node.nid = f'{nodes.index(node)},{str(node.val)}'
            unlinked_copied_nodes.append(Node(node.val))
            unlinked_copied_nodes[-1].nid = node.nid
        # Store links
        #   key = node.nid, value = [node.parent.nid, node.left.nid, node.right.nid]
        #   example dict item -> ('1,X', ['0,<function div at 0x000002982BA07E20>', None, None])
        links_dict = {}
        for node in nodes:
            key = node.nid
            value = []
            for linked_node in node.get_links():
                if linked_node != None:
                    value.append(linked_node.nid)
                else:
                    value.append(None)
            links_dict.update({key: value})
        # # Debug
        # for _ in links_dict.items():
        #     print(f"dict.item={_}")
        # Debug
        # print(f"unlinked_copied_nodes = {unlinked_copied_nodes}\n")
        """ 
        # Prove original Node.nid and unlinked_copied_nodes[?].nid matches
        rand_node_index = rand(0, len(nodes) - 1)
        rand_node = nodes[rand_node_index]
        print(rand_node, rand_node.nid, links_dict[rand_node.nid]) 
        """
        # Be able to match a node.nid to an actual node in the unlinked_list
        # Therefore create a dictionary for unlinked_nodes to get an unlinked node
        #   ... by index-slicing by their
        # ---
        # Create a dictionary of unlinked node IDs to nodes (read .update(...) line)
        unlinked_nodes_dict = {}
        for node in unlinked_copied_nodes:
            unlinked_nodes_dict.update({node.nid: node})
        # Link nodes to left and right
        # Too many if-else statements :( but it works! :D
        for unlinked_node in unlinked_copied_nodes:
            parent_nid, left_nid, right_nid = links_dict[unlinked_node.nid]
            # parent
            if parent_nid is not None:
                unlinked_node.parent = unlinked_nodes_dict[parent_nid]
            else:
                unlinked_node.parent = None
            # left
            if left_nid is not None:
                unlinked_node.left = unlinked_nodes_dict[left_nid]
            else:
                unlinked_node.left = None
            # left
            if right_nid is not None:
                unlinked_node.right = unlinked_nodes_dict[right_nid]
            else:
                unlinked_node.right = None
        """
        # Prove parents are linked correctly
        rand_node_index = rand(0, len(nodes) - 1)
        rand_node = nodes[rand_node_index]
        print(
            f"rand_node, rand_node.nid, links_dict[rand_node.nid] = {rand_node, rand_node.nid, links_dict[rand_node.nid]}")
        print(f"parents = {rand_node.parent, unlinked_nodes_dict[rand_node.nid].parent}")
        print(f"left = {rand_node.left, unlinked_nodes_dict[rand_node.nid].left}")
        print(f"right = {rand_node.right, unlinked_nodes_dict[rand_node.nid].right}")
        """
        # print(f"nodes = {nodes}")
        print(f"unlinked_copied_nodes = {unlinked_copied_nodes}")
        node_structure_copy = NodeStructure(root=unlinked_copied_nodes[0], gen_struc=False)
        print(f"node_structure_copy.depth_hashmap = {node_structure_copy.depth_hashmap}")
        return node_structure_copy

    def move_popualtion(self):
        """ Moves the population from self.population into
        self.pm. i.e [x, ...] -> [[?], [?], [x, ...]]
        """
        pass

    def _mutate(self, sarr, chance_for_mutant=0.3):
        # 30% to generate a new subtree 70% to switch a value
        # Todo: create this method
        pass

    def _duplication(self, sarr):
        # Todo: review & test this method
        return self.population[sarr[rand(0, 1)]].__copy__()
        pass

    def _evolution(self, sarr=None, mutation_chance=0.2, duplication_chance=0.1, crossover_chance=0.7):
        """ Given a population of NodeStructure(s) per generation; fitness is measured,
        based on fitness, proportions and rolling percentages are generated to carry out
        random genetic opertions to produce a population of better fitted NodeStructure(s).
        This process is repeated until the fitness of a NodeStructure meets a certain range.
        """
        # Todo: create this method
        raise TypeError("._evolution() for-if failed!")

    def iterations(self, criteria=1.5):
        """ Calls ._evolution() = No. of new population member(s) """
        # Todo: review & re-create this method
        # act_crit = 99
        # iteration = 0
        # print(self.pm)
        # # for nstruc in self.population: nstruc.print_depth_hashmap()
        # while not act_crit <= criteria and iteration != 50:
        #     # Create vector for next population Todo: Fix this
        #     print(act_crit, self.pm)
        #     iteration += 1
        #     if len(self.pm) != iteration + 1: self.pm.append([])
        #     # Perform evolution
        #     try:
        #         while len(self.pm[iteration]) != self.pcount:
        #             sarr = [s1, s2] = self.selection()
        #             self.pm[iteration].append(self._evolution(sarr))
        #         for nstruc in self.pm[iteration]:
        #             # nstruc.print_depth_hashmap()
        #             if measure_fitness(nstruc) < act_crit:
        #                 nstruc.refresh_depth_hashmap()
        #                 nstruc.reset_cval_all_c()
        #                 act_crit = measure_fitness(nstruc)
        #                 print("act_crit", act_crit)
        #         self.population = None
        #         self.population = [nstruc.__copy__() for nstruc in self.pm[iteration]]
        #     except IndexError as e:
        #         print(self.pm)
        #         print("iteration:", iteration)
        #         raise e
        pass


def test_crossover():
    print("Method not written.")
    pass


if __name__ == '__main__':
    gp = genetic_program_object = GeneticProgram(count=4)
    gp.crossover()
    # gp.copy()
