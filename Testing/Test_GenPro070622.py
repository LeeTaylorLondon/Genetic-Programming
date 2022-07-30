from Classes import GeneticProgram


"""
< Class : GeneticProgram >
        self.pcount     = count
        self.population = [NodeStructure() for _ in range(count)]
        self.pm         = [ns.__copy__() for ns in self.population]
"""


gp = GeneticProgram()
print("gp.count, gp.population, gp.pm")
print(gp.pcount)
print(gp.population)
print(gp.pm)

gp.pm.append([gp._crossover(gp.selection())])
gp.pm[1].append(gp._crossover(gp.selection()))
gp.pm[1].append(gp._crossover(gp.selection()))
gp.pm[1].append(gp._crossover(gp.selection()))

print(gp.pm[0])
print(gp.pm[1])
