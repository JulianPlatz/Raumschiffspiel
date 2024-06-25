

# |-------------------------| #
# |---- Raumschiffspiel ----| #
# |---- Julian Platz -------| #
# |---- FI-A 32 ------------| #
# |-------------------------| #


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
    def setUnits(self, units):
        self._units = units
