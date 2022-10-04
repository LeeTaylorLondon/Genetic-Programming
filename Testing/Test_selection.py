# Author: Lee Taylor

"""          20 + 5 + 10 + 5 = 40
             100 / 40 = 2.5 
Therefore -> 1 : 2.5% 
             1 / 20 = 0.05
             1 / 5  = 0.20
             [0.05, 0.20, 0.10, 0.20]
             [0.05, 0.25, 0.35, 0.55]
             
            import numpy.random as npr
            def selectOne(self, population):
                max = sum([c.fitness for c in population])
                selection_probs = [c.fitness/max for c in population]
                return population[npr.choice(len(population), p=selection_probs)]
"""


if __name__ == '__main__':
    fn = [28.7, 28.7, 110.5, 8.7]  # Fitness values (normal)
    fs = [20, 5, 10, 5]            # Fitness values (small)
    fsum = sum(fn)              # = 176.6
    pval = [f/fsum for f in fn] # = [0.16, 0.16, 0.63, 0.05]
    sump = sum(pval)            # = 1.0
    roll = [pval[0]]            # = [0.16]
    for i,v in enumerate(pval[1:]):
        roll.append(v + roll[i])
    print(fsum, pval, sump)
    print(roll)                 # = [0.16, 0.33, 0.95, 1.0]
    print(roll[::-1])           # = [1.0, 0.95, 0.33, 0.16]
    # Compare in reverse order and then locate index of value
    print(roll.index(0.95))