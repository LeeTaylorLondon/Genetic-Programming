from Classes import NodeStructure
from GlobalVariables import measure_fitness

class NodeStructureGUI(NodeStructure):
    def __init__(self):
        super(NodeStructureGUI, self).__init__()

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return f"<NSGUI {round(float(measure_fitness(self)), 2)}>"


if __name__ == '__main__':
    nsgui = NodeStructureGUI()
    print(nsgui)