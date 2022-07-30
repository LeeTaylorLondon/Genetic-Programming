from Classes import NodeStructure, List
from GeneticProgram import *

""" 
 Class: < Genetic Program >
 Attrs: .pcount .population .pm
 Meths: ... 
"""

# gp = GeneticProgram()
#
# print("gp.count ->", gp.pcount)          # Population Count
# print("gp.popualtion ->", gp.population) # Population Array (members)
# print("gp.population_matrix ->", gp.pm)  # Population Matrix

# print("Original************")
# gp.population[0].print_depth_hashmap()
# print("Copy*********")
# gp.pm[0].print_depth_hashmap()

# for i in range(0, 4):
#     gp.pm[0][i].print_depth_hashmap()
#     gp.population[i].print_depth_hashmap()
#     print("***")

# gp.selection()


strucs = [NodeStructure() for x in range(50)]

def mfloop():
    for loops in range(20):
        measure_fitness(strucs[rand(0, len(strucs) - 1)])

