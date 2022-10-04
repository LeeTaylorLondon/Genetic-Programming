from Classes import NodeStructure
from GlobalVariables import measure_fitness, obj_func, term_set, func_set
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
        """ Check fitness of each population member """
        for i,p in enumerate(self.population):
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
        for x,y in zip(root_cval, objective):
            if x != y: return False
        return True

    def fitness_replace(self):
        """ Replace unfit population member. Unfit -> fitness(p) = 0.0 """
        while 0 < self.fitness_check() <= 3:
            print('self.fitness_check()', self.fitness_check())
            # print(self.population) # Redundant while NS.__repr__ is not fit.v.
            replace_i = self.fitness_check()
            print('replace_i', replace_i)
            self.population[replace_i] = NodeStructure()
            self.pm[0][replace_i] = NodeStructure()
            print(self.population)

    def selection(self):
        """ # ---- Variables ---- #
            fn = [28.7, 28.7, 110.5, 8.7]  # Fitness values (normal)
            fs = [20, 5, 10, 5]            # Fitness values (small)
            # ---- Calculations ---- #
            fsum = sum(fn)              # = 176.6
            pval = [f/fsum for f in fn] # = [0.16, 0.16, 0.63, 0.05]
            sump = sum(pval)            # = 1.0
            roll = [pval[0]]            # = [0.16]
            for i,v in enumerate(pval[1:]):
                roll.append(v + roll[i])
            print(fsum, pval, sump)
            print(roll)                 # = [0.16, 0.33, 0.95, 1.0]
        """
        farr = [measure_fitness(ns) for ns in self.population]
        plis = [f/sum(farr) for f in farr]
        # Roll probability values
        roll = [plis[0]]
        for i, v in enumerate(plis[1:]):
            roll.append(v + roll[i])
        roll[-1] = 1.0
        # Compare random-float and random-probability
        rfv, rv = rf(), -1
        for rp in roll[::-1]:
            if rfv < rp: rv = roll.index(rp)
        print(f"plis={plis}\nroll={roll}\nrv={rv}")
        return rv

    def crossover(self, sarr, debug=True):
        """ :param sarr: Selection Array contains index values for which
        population members are to be selected. """
        # Unpack selection array & assign values
        s1, s2 = sarr
        p1, p2 = self.population[s1].__copy__(), self.population[s2].__copy__()
        # DEBUG
        if debug:
            print("BEFORE")
            p1.print_depth_hashmap()
            p2.print_depth_hashmap()
        sn1 = selected_node1 = p1.rand_node()
        sn2 = selected_node2 = p2.rand_node(ntype=sn1.eval_type())
        # DEBUG
        if debug:
            print("^^ SN1 : SN2 ^^")
            print(sn1)
            print(sn2)
            print("================================")
        # Todo: change return condition here
        # Do not perform crossover if two of the same type do not exist
        if sn1.eval_type() != sn2.eval_type():
            return
        # Overwrite sn1.val
        if sn2.val in func_set:
            sn1.val = sn2.val
        elif sn2.val in term_set and term_set.index(sn2.val) != 0:
            sn1.val = term_set.index(sn2.val)
        else:
            sn1.val = term_set[0] # Todo: this might be wrong
        # Reset computed-value
        sn1.cval = None
        p1.reset_cval_all_c()
        # Overwrite left & right
        sn1.left  = sn2.left
        sn1.right = sn2.right
        # DEBUG
        if debug:
            print("AFTER")
            p1.print_depth_hashmap()
            p2.print_depth_hashmap()
        return p1, p2

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
