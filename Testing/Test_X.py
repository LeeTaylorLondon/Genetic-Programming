from Classes import NodeStructure, List
from GlobalVariables import measure_fitness


strucs = [NodeStructure() for _ in range(20)]


def outf(arr=None, out=False):
    """ Print fitness for each population member """
    if arr is None:
        arr = strucs
    rv = "|"
    for struc in arr: rv = rv + str(round(measure_fitness(struc), 3)) + "|"
    if out: print(rv)
    return rv


def struc_cval(arr=None, index=0):
    """ Debugging - can't remember :( """
    if arr is None: arr = strucs
    out_cval = False
    while not out_cval:
        try:
            print(index, strucs[index].root.cval.printv())
            out_cval = True
        except AttributeError:
            index += 1
            out_cval = False
            pass
    pass

def reset():
    """ Reset computed value """
    for struc in strucs:
        struc.reset_cval_all_c()


if __name__ == '__main__':
    outf()



