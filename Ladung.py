class Ladung:

    # constructor
    def __init__(self, name="Leerladung", units=0):
        self._name = name
        self._units = units

    # methodes
    def Ladung(self):
        pass

    # getter
    def getName(self):
        return self._name

    def getUnits(self):
        return self._units

    # setter
    def setName(self, name):
        self._name = name

    def setUnits(self, units):
        self._units = units
