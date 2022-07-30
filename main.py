from Classes import NodeStructure, GeneticProgram


"""
[ ] Objective: Find program whose output matches x^2+x+1 over the range
-1 <= x <= + 1
[x] Function Set: +, -, %, *
[x] Terminal Set: x, and constants chosen randomly between -5 and +5
[x] Fitness: sum of absolute errors for x is an element of {-1.0, -0.9, ... 0.9, 1.0}
[ ] Selection: fitness proportionate (roulette wheel) non elitist
    * This should be EASY - calculate odds proportionate to their fitness
    * Sum total fitness, % = fitness / sum(fitness)
[-] Initial pop: ramped half-and-half (d = 1 to 2, 50% of terminals are constants)
[ ] Parameters: population size 4, 50% subtree crossover, 25% reproduction,
    25% subtree mutation, no tree size limits
[ ] Termination: Individual with fitness better than 0.1 found
"""

def main(debug=True):
    print(">> EXECUTING: MAIN PROGRAM")
    n1 = NodeStructure()
    if debug: n1.print_all_nodes() # Debug


if __name__ == '__main__':

    """ Global Variables """
    # global xt, func_set, term_set, whole_set

    ''' Testing section '''
    print(">> EXECUTING: TESTS <<\n")

    # for testruns in range(100):
    # gp = GeneticProgram()
    # s1, s2 = gp.selection(out=True)
    # gp.perform_crossover(s1, s2)
    # p1, p2, p3, p4 = gp.population

    gp = GeneticProgram()
    gp.test_crossover()

    print(">> EXECUTING: TESTS FINISHED SUCCESSFULLY <<\n")

    ''' Main Program Code of Genetic Programming '''
    # main(False)
    # print(">> EXECUTING: FINISHED SUCCESSFULLY <<")
