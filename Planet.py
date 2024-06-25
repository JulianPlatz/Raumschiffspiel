from Ladung import Ladung


# |-------------------------| #
# |---- Raumschiffspiel ----| #
# |---- Julian Platz -------| #
# |---- FI-A 32 ------------| #
# |-------------------------| #


class Planet:

    # constructor
    def __init__(self, name, atmosphere, posX, posY):
        self._name = name
        self._atmosphere = atmosphere
        self._posX = posX
        self._posY = posY
        self._charge = None

    # methodes
    def Planet(self):
        pass

    def removeCharge(self):
        if self._charge is not None:
            charge = Ladung(self._charge.getName(), 1)
            self._charge.setUnits(self._charge.getUnits() - 1)
            return charge
        else:
            return None

    # getter
    def getName(self):
        return self._name

    def getAtmosphere(self):
        return self._atmosphere

    def getPosX(self):
        return self._posX

    def getPosY(self):
        return self._posY

    def getCharge(self):
        return self._charge

    # setter
    def setCharge(self, charge):
        self._charge = charge
