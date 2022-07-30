from Classes import NodeStructure

p1 = NodeStructure(depth_lim_lower=2, depth_lim_upper=2)
mutant = NodeStructure(depth_lim_upper=1)

print("---- P1 DEPTH HASHMAP ----")
p1.print_depth_hashmap()

print("---- MUTANT DEPTH HASHMAP ----")
mutant.print_depth_hashmap()

print("---- PERFORMING CROSSOVER ----")
p1.crossover(mutant)

print("---- P1 CROSSOVER DEPTH HASHMAP ----")
p1.refresh_depth_hashmap()
p1.print_depth_hashmap()
