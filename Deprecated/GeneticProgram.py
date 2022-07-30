from Classes import NodeStructure
from GlobalVariables import measure_fitness, term_set, func_set
from random import random as rf
from random import randint as rand


class GeneticProgram:
    def __init__(self, count=4):
        self.pcount            = count
        self.population        = [NodeStructure() for _ in range(count)]
        self.pm                = [[ns.__copy__() for ns in self.population]]
        # self.pm                = self.population_matrix

    def selection(self, out=False):
        """ Creates values fitness, proportions, and rolling percentages
        to select (in a roulette fashion) two random NodeStructures from
        the self.population. """
        # Init. matrix to store vector(s), vec, for each NodeStructure
        matrix = [[0, 0, 0, 0] for _ in self.population]
        # vec[0] stores 'fitness value'
        for vec, p in zip(matrix, self.population): vec[0] = measure_fitness(p)
        fitness_summed = sum([vec[0] for vec in matrix])
        # vec[1] stores 'proportion value'
        for vec in matrix: vec[1] = 1/(vec[0]/fitness_summed)
        proportion_summed = sum(vec[1] for vec in matrix)
        # vec[2] stores 'percentage value'
        matrix[0][2] = matrix[0][1]/proportion_summed
        # vec[3] stores 'rolling sum of % value (from vec[2])'
        matrix[0][3] = matrix[0][1]/proportion_summed
        for i,vec in enumerate(matrix[1:]):
            vec[2] = vec[1]/proportion_summed
            vec[3] = matrix[i][3] + vec[2]
        # Roulette selection ~ rf = randomfloat, s = selection
        rf1, rf2, s1, s2 = rf(), rf(), None, None
        while s1 is None or s2 is None or s1 == s2:
            if rf1 < matrix[0][3]: s1 = 0
            if rf2 < matrix[0][3]: s2 = 0
            for i,vec in enumerate(matrix):
                if matrix[i][3] < rf1 <= matrix[i+1][3] and s1 is None: s1 = i + 1
                if matrix[i][3] < rf2 <= matrix[i+1][3] and s2 is None: s2 = i + 1
            if s1 is None: rf1, s1 = rf(), None
            if s2 is None: rf2, s2 = rf(), None
            if s1 == s2: rf1, rf2, s1, s2 = rf(), rf(), None, None
        # Debug information
        if out:
            print([vec[3] for vec in matrix])
            print(str(rf1) + " " + str(rf2) + " " + str(s1) + " " + str(s2) + '\n')
        return s1, s2

    def _crossover(self, sarr):
        nstruc_copy = self.population[sarr[0]].__copy__()
        nstruc_copy.crossover(self.population[sarr[1]].__copy__(), out=False)
        nstruc_copy.refresh_depth_hashmap()
        nstruc_copy.find_max_depth()
        return nstruc_copy

    def _mutate(self, sarr, chance_for_mutant=0.3):
        # 30% to generate a new subtree 70% to switch a value
        if rf() < chance_for_mutant:
            # sarr = self.selection() # = selection_array
            mutant       = NodeStructure(depth_lim_upper=1)
            nstruc_index = sarr[rand(0, len(sarr)-1)]
            nstruc_copy  = self.population[nstruc_index].__copy__()
            nstruc_copy.crossover(mutant)
            return nstruc_copy.__copy__()
        else:
            # snode = self.selection()[rand(0, 1)]._rand_node()
            nstruc_copy  = self.population[sarr[rand(0, 1)]].__copy__()
            if nstruc_copy is None: raise TypeError("blank nstruc_copy")
            snode        = nstruc_copy.rand_node(nstruc=nstruc_copy, debug=True)
            if snode.eval_type() is "term":
                snode.val = term_set[rand(0, len(term_set) - 1)]
            else:
                snode.val = func_set[rand(0, len(func_set) - 1)]
            return nstruc_copy

    def _duplication(self, sarr):
        return self.population[sarr[rand(0, 1)]].__copy__()

    def _evolution(self, sarr=None, mutation_chance=0.2, duplication_chance=0.1, crossover_chance=0.7):
        """ Given a population of NodeStructure(s) per generation; fitness is measured,
        based on fitness, proportions and rolling percentages are generated to carry out
        random genetic opertions to produce a population of better fitted NodeStructure(s).
        This process is repeated until the fitness of a NodeStructure meets a certain range.
        """
        if sarr is None: sarr = [s1, s2] = self.selection()
        # List(s) -> chances, rolled_percentages, methods
        chances = [mutation_chance, duplication_chance, crossover_chance]
        ''' rolledp = [chances[0]]
        rolledp.extend([rolledp[i - 1] + c for i, c in enumerate(chances[1:])])
        print("var arr rolledp = " + str(rolledp)) '''
        rolledp = [0.2, 0.3, 1.0]
        methods = [self._mutate, self._duplication, self._crossover]
        for _ in self.population:
            rfval = rf()
            if rfval <= rolledp[0]:
                print(".mutate()")
                return methods[0](sarr)
            elif rolledp[0] < rfval <= rolledp[1]:
                print("._dupe()")
                return methods[1](sarr)
            elif rolledp[1] < rfval <= rolledp[2]:
                print("._cross()")
                return methods[2](sarr)
        print(rfval, chances, rolledp)
        raise TypeError("._evolution() for-if failed!")

    def evolution_loop(self, criteria=1.5):
        """ Calls ._evolution() = No. of new population member(s) """
        act_crit, iteration = 99, 0
        # for nstruc in self.population: nstruc.print_depth_hashmap()
        while not act_crit <= criteria and iteration != 50:
            # Create vector for next population
            print(act_crit, self.pm[iteration]) # Debug
            iteration += 1
            if len(self.pm) != iteration + 1: self.pm.append([])
            # Perform evolution
            try:
                # While-loop appends new_struc to pop._matrix
                while len(self.pm[iteration]) != self.pcount:
                    sarr = [s1, s2] = self.selection()
                    self.pm[iteration].append(self._evolution(sarr))
                    new_fit = measure_fitness(self.pm[iteration][len(self.pm[iteration]) - 1])
                    if new_fit < act_crit: act_crit = new_fit
                self.population = None
                self.population = [nstruc.__copy__() for nstruc in self.pm[iteration]]
            except IndexError as e:
                print(self.pm)
                print("iteration:", iteration)
                raise e
        pass

