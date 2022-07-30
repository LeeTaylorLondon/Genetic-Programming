from Classes import NodeStructure
from NodeStructure import *

"""
The purpose of this program-file is to test all possible
combinations of using them together to produce errors
and fix them. 

func_set  = (sub, add, mul, div)
term_set  = (xt(), -5, -4, -3, -2, -1, 1, 2, 3, 4, 5) # Omitted 0
"""


if __name__ == '__main__':
    # log stores all computed values
    log = []
    # fterm = first_term, sterm = second_term
    for fterm in term_set:
        left = fterm
        for sterm in term_set:
            right = sterm
            for func in func_set:
                log.append([left, right, func(left, right)])
                print(log[len(log)-1][2])
