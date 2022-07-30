from Classes import NodeStructure, List
from GeneticProgram import *


RUNS = 1


for runs in range(RUNS):

    """ Proof measure_fitness() & .interpreter() works """
    strucs = [NodeStructure() for count in range(10)]
    strucs2 = []
    out_str1 = ""
    for struc in strucs:
        out_str1 = out_str1 + " | " + str(measure_fitness(struc))
    """ ### End End End ### """
    print(out_str1 + '\n')

    """ Proof selection returns two indexes """
    gp = GeneticProgram()
    gp.population = strucs
    gp.pm = [[ns.__copy__() for ns in gp.population]]
    selection_return = gp.selection()
    """ ### End End End ### """
    print(str(selection_return) + "\n")

    """ Proving each genetic method functions correctly """
    new_ns = gp._crossover(selection_return)

    for selection in selection_return:
        print("----Selection----")
        gp.pm[0][selection].print_depth_hashmap()

    print("----Crossover Result----")

    gp.pm.append([new_ns])
    gp.pm[1][0].print_depth_hashmap()
    # Cross Over Interpreter Return
    coir = gp.pm[1][0].interpreter()
    print("----COIR Out----")
    print(coir)
    if type(coir) == List: coir.printv()

    # Proof .find_max_depth() works
    # for struc in strucs:
    #     print(struc.find_max_depth())
    #     struc.print_depth_hashmap()
