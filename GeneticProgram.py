from Classes import NodeStructure
from GlobalVariables import measure_fitness, term_set, func_set
from random import random as rf
from random import randint as rand


class GeneticProgram:
    def __init__(self, count=4):
        self.pcount     = count
        self.population = [NodeStructure() for _ in range(count)]
        self.pm         = [[ns.__copy__() for ns in self.population]]

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return str(self.population)

    def fitness_check(self):
        for i,p in enumerate(self.population):
            if measure_fitness(p, False) == 0.0:
                return i
        return -1

    def fitness_replace(self):
        while 0 < self.fitness_check() <= 3:
            print('self.fitness_check()', self.fitness_check())
            # print(self.population) # Redundant while NS.__repr__ is not fit.v.
            replace_i = self.fitness_check()
            print('replace_i', replace_i)
            self.population[replace_i] = NodeStructure()
            self.pm[0][replace_i] = NodeStructure()
            print(self.population)

    def selection(self, out=False):
        self.fitness_replace()
        """ Creates values fitness, proportions, and rolling percentages
        to select (in a roulette fashion) two random NodeStructures from
        the self.population. 
        
        value 'matrix' stores vectors of 4 values for each pop. member
        vec[0] -> value fitness  
        vec[1] -> value proportion
        vec[2] -> value percentage 
        vec[3] -> value rolling sum of %
        """
        # Init. matrix
        matrix = [[1.0, 0.0, 0.0, 0.0] for _ in self.population]
        # vec[0]
        for vec, p in zip(matrix, self.population): vec[0] = max(1.0, measure_fitness(p))
        fitness_summed = sum([vec[0] for vec in matrix])
        if fitness_summed == 0: raise TypeError('How is the fitness_summed zero?')
        # vec[1]
        for vec in matrix:
            if float(vec[0]/fitness_summed) == 0.0:
                print('fitness_summed ->', fitness_summed)
                for p in self.population:
                    mfp = measure_fitness(p)
                    print('measure_fitness(p) ->', mfp)
                    if mfp == 0:
                        print('vec[0] ->', vec[0])
                        print('p.root.cval ->', p.root.cval)
                raise TypeError('vec[0]/fitness_summed == 0')
            vec[1] = 1/(float(vec[0]/fitness_summed))
        proportion_summed = sum(vec[1] for vec in matrix)
        matrix[0][2] = matrix[0][1]/proportion_summed # vec[2]
        matrix[0][3] = matrix[0][1]/proportion_summed # vec[3]
        for i,vec in enumerate(matrix[1:]):
            vec[2] = vec[1]/proportion_summed
            vec[3] = matrix[i][3] + vec[2]
        # Roulette selection ~ rf = randomfloat, s = selection
        rf1, rf2, s1, s2 = rf(), rf(), None, None
        while s1 is None or s2 is None or s1 == s2:
            # Generate random float for selection boundry
            if rf1 < matrix[0][3]: s1 = 0
            if rf2 < matrix[0][3]: s2 = 0
            # if rfx within boundary and current selection is None
            for i,vec in enumerate(matrix):
                if matrix[i][3] < rf1 <= matrix[i+1][3] and s1 is None: s1 = i + 1
                if matrix[i][3] < rf2 <= matrix[i+1][3] and s2 is None: s2 = i + 1
            if s1 is None:
                rf1, s1 = rf(), None
                print('rf1, rf2, s1, s2')
                print(rf1, rf2, s1, s2)
                print(matrix[0][3], matrix[1][3], matrix[2][3], matrix[3][3])
                raise TypeError ('Why is this none?')
            if s2 is None:
                rf2, s2 = rf(), None
                print('rf1, rf2, s1, s2')
                print(rf1, rf2, s1, s2)
                print(matrix[0][3], matrix[1][3], matrix[2][3], matrix[3][3])
                raise TypeError ('Why is this none?')
            # Todo: optional - prevent selecting itself
            if s1 == s2:
                break
        # Debug information
        if out:
            print([vec[3] for vec in matrix])
            print(str(rf1) + " " + str(rf2) + " " + str(s1) + " " + str(s2) + '\n')
        return s1, s2

    def move_popualtion(self):
        """ Moves the population from self.population into
        self.pm. i.e [x, ...] -> [[?], [?], [x, ...]]
        """
        pass

    def _crossover(self, sarr):
        """ :param sarr: Selection Array contains index values for which
        population members are to be selected. """
        # Unpack selection array & assign values
        s1, s2 = sarr
        p1, p2 = self.population[s1], self.population[s2]
        sn1 = selected_node1 = p1.rand_node()
        sn2 = selected_node2 = p2.rand_node(ntype=sn1.eval_type())
        # Do not perform crossover if two of the same type do not exist
        # Todo: change this so that it is compatible to do so without error
        if sn1.eval_type() != sn2.eval_type(): return
        # Overwrite sn1.val
        if sn2.val in func_set: sn1.val = sn2.val
        elif sn2.val in term_set and term_set.index(sn2.val) != 0:
            sn1.val = term_set.index(sn2.val)
        else: sn1.val = term_set[0]
        # Reset computed-value
        sn1.cval = None
        p1.reset_cval_all_c()
        # Overwrite left & right
        sn1.left  = sn2.left
        sn1.right = sn2.right

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
        act_crit = 99
        iteration = 0
        print(self.pm)
        # for nstruc in self.population: nstruc.print_depth_hashmap()
        while not act_crit <= criteria and iteration != 50:
            # Create vector for next population Todo: Fix this
            print(act_crit, self.pm)
            iteration += 1
            if len(self.pm) != iteration + 1: self.pm.append([])
            # Perform evolution
            try:
                while len(self.pm[iteration]) != self.pcount:
                    sarr = [s1, s2] = self.selection()
                    self.pm[iteration].append(self._evolution(sarr))
                for nstruc in self.pm[iteration]:
                    # nstruc.print_depth_hashmap()
                    if measure_fitness(nstruc) < act_crit:
                        nstruc.refresh_depth_hashmap()
                        nstruc.reset_cval_all_c()
                        act_crit = measure_fitness(nstruc)
                        print("act_crit", act_crit)
                self.population = None
                self.population = [nstruc.__copy__() for nstruc in self.pm[iteration]]
            except IndexError as e:
                print(self.pm)
                print("iteration:", iteration)
                raise e
        pass

def test_crossover():
    print("Method not written.")
    pass