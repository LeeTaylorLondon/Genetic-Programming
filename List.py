class List(list):
    def __init__(self, x=None):
        if x is not None: self.append(x)
        super(List, self).__init__(x)

    def __add__(self, other):
        rv = self.__copy__()
        if type(other) is List:
            for i in range(len(other)):
                rv.__setitem__(i, self.__getitem__(i) + other[i])
            return rv
        for i in range(0, len(self)):
            rv.__setitem__(i, self.__getitem__(i) + other)
        return rv

    def __sub__(self, other):
        rv = self.__copy__()
        if type(other) is List:
            for i in range(len(other)):
                rv.__setitem__(i, self.__getitem__(i) - other[i])
            return rv
        for i in range(0, len(self)):
            rv.__setitem__(i, self.__getitem__(i) - other)
        return rv

    def __mul__(self, other):
        rv = self.__copy__()
        if type(other) is List:
            for i in range(len(other)):
                rv.__setitem__(i, self.__getitem__(i) * other[i])
            return rv
        for i in range(0, len(self)):
            rv.__setitem__(i, self.__getitem__(i) * other)
        return rv

    def __truediv__(self, other):
        rv = self.__copy__()
        if type(other) is List:
            for i in range(len(other)):
                try:
                    rv.__setitem__(i, self.__getitem__(i) / other[i])
                except ZeroDivisionError:
                    rv.__setitem__(i, self.__getitem__(i))
            return rv
        for i in range(0, len(self)):
            try:
                rv.__setitem__(i, self.__getitem__(i) / other)
            except ZeroDivisionError:
                rv.__setitem__(i, self.__getitem__(i))
        return rv

    def __copy__(self):
        return List([float(x) for x in self])

    def __str__(self):
        if len(self) ==  0:
            return 'Empty List'
        rv = '['
        for i in range(len(self) - 1):
            rv = rv + str(self.__getitem__(i)) + ', '
        rv = rv + str(self.__getitem__(len(self) - 1))
        rv = rv + ']'
        return rv
        # return "X" # Old way of representing a List

    def __repr__(self):
        return self.__str__()

    def printv(self):
        rv = "["
        for i in range(len(self)):
            # print(self.__getitem__(i))
            rv = rv + str(self.__getitem__(i))
            if i != len(self) - 1:
                rv = rv + ", "
        rv = rv + "]"
        return rv


