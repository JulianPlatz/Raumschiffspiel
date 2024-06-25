

# |-------------------------| #
# |---- Raumschiffspiel ----| #
# |---- Julian Platz -------| #
# |---- FI-A 32 ------------| #
# |-------------------------| #


class Raumschiff:

    # constructor
    def __init__(self, name, posX, posY, healthPoints, attackDamage, protectiveShield, kapitaen):
        self._name = name
        self._posX = posX
        self._posY = posY
        self._healthPoints = healthPoints
        self._attackDamage = attackDamage
        self._protectiveShield = protectiveShield
        self._kapitaen = kapitaen
        self._charge = None
        self._isDestroyed = False

    # methodes
    def Raumschiff(self):
        pass

    def fly(self, direction):
        if direction == 'd':
            self._posY += 1
        elif direction == 'a':
            self._posY -= 1
        elif direction == 's':
            self._posX -= 1
        elif direction == 'w':
            self._posX += 1

    def checkCoordinates(self, x, y):
        if self.getPosX() == x and self.getPosY() == y:
            return True
        else:
            return False

    def attack(self, falcon_heavy):
        if falcon_heavy.getHealthPoints() > 0:
            damage = self._attackDamage - falcon_heavy.getProtectiveShield()
            if damage > 0:
                falcon_heavy._healthPoints -= damage
                if falcon_heavy._healthPoints <= 0:
                    falcon_heavy._isDestroyed = True

    def counterAttack(self, starship):
        if starship.getHealthPoints() > 0:
            damage = self._attackDamage - starship.getProtectiveShield()
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

    def getHealthPoints(self):
        return self._healthPoints

    def getAttackDamage(self):
        return self._attackDamage

    def getProtectiveShield(self):
        return self._protectiveShield

    def getKapitaen(self):
        return self._kapitaen

    def getCharge(self):
        return self._charge

    # setter
    def addCharge(self, charge):
        if self._charge is None:
            self._charge = charge
        else:
            self._charge.setUnits(self._charge.getUnits() + charge.getUnits())
