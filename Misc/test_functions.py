''' MAIN Program functions '''
def print_func(inp):
    # if type(inp) is list:
    #     rv = ""
    #     for e in inp:
    #         if str(type(e)).__contains__('function'):
    #             rv = rv + str(e).split(" ")[1] + " "
    #         else:
    #             rv = rv + str(e) + " "
    #     return rv
    # elif str(type(inp)).__contains__('function'):
    #     return str(inp).split(" ")[1]
    # return str(inp)
    pass

def test_population(pop_size=4, print_pop=False, out=True):
    # population = [NodeStructure() for x in range(pop_size)]
    # for i, p_ in enumerate(population):
    #     if out: print("\n<Resident:" + str(i) + ">")
    #     # p.print_all_nodes()
    #     if out: p_.print_depth_hashmap()
    #     if print_pop: p_.print_depth_hashmap()
    # return population
    pass

def test_interpreter(runs=1, out=True, outrv=True):
    # for r_ in range(runs):
    #     pop = test_population(1, print_pop=False, out=False)
    #     pop[0].interpreter(out)
    # if out: print("\nobj_func(x) -> " + str(obj_func(xt)))
    # if outrv: print("Actual output -> " + str(pop[0].root.cval))
    # return pop
    pass

def test_book_struc():
    # root = Node(add)
    # struc = NodeStructure(root=root, gen_struc=False)
    #
    # root.left = Node(1, parent=root)
    # root.right = Node(mul, parent=root)
    # struc.depth_hashmap[1] = [root.left, root.right]
    #
    # root.right.left = Node(add, parent=root.right)
    # root.right.right = Node(xt.__copy__(), parent=root.right)
    # struc.depth_hashmap[2] = [root.right.left, root.right.right]
    #
    # root.right.left.left = Node(xt, parent=root.right.left)
    # root.right.left.right = Node(1, parent=root.right.left)
    # struc.depth_hashmap[3] = [root.right.left.left, root.right.left.right]
    #
    # # struc.print_depth_hashmap()
    #
    # calc = struc.interpreter(out=False)
    #
    # return struc, calc
    pass

def test_54():
    # desired_out = obj_func(x=None, out=False)
    # popul = test_interpreter(out=False, outrv=True)
    # diff = measure_fitness(popul[0])
    #
    # target_struc, calculated = test_book_struc()
    # # print(calculated)
    #
    # plt.subplot(1, 1, 1)
    # plt.grid(True)
    # # print(type(popul[0].root.cval))
    # if type(popul[0].root.cval) is cl.List:
    #     plt.plot(desired_out, linewidth=5)
    #     plt.plot(popul[0].root.cval, linewidth=1)
    #     plt.plot(calculated, linewidth=3)
    #     plt.show()
    #
    # print("Absolute summed diff -> " + str(diff))
    pass

def test_55():
    # # Spawn population of NodeStructure object(s).
    # population = [NodeStructure() for _ in range(4)]
    #
    # # For NodeStructure in population Meas.Fitness & out structure.
    # for p__ in population:
    #     print(measure_fitness(p__))
    #     p__.print_depth_hashmap()
    #
    # # Test crossover function
    # # population[0].crossover(population[1], out=True)
    # # p1 = population[0]
    # # root1 = p1.root
    # # p2 = population[1]
    # # root2 = p2.root
    #
    # # Meas. Fitness of new structure created by crossover
    # # print(measure_fitness(population[0]))
    pass

#
# x = [1, 2, 3]
# print(x[::-1])
