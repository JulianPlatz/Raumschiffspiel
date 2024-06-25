

# |-------------------------| #
# |---- Raumschiffspiel ----| #
# |---- Julian Platz -------| #
# |---- FI-A 32 ------------| #
# |-------------------------| #


class Asteroidenfeld:

    # constructor
    def __init__(self, name, posX, posY, damage):
        self._name = name
        self._posX = posX
        self._posY = posY
        self._damage = damage

    # methodes
    def Asteroidenfeld(self):
        pass

    def checkCoordinates(self, x, y):
        if self.getPosX() == x and self.getPosY() == y:
            return True
        else:
            return False

    def attack(self, starship):
        if starship.getHealthPoints() > 0:
            damage = self._damage - starship.getProtectiveShield()
            if damage > 0:
                starship._healthPoints -= damage
                if starship._healthPoints <= 0:
                    starship._isDestroyed = True

    # getter
    def getName(self):
        return self._name

    def getPosX(self):
        return self._posX

    def getPosY(self):
        return self._posY
