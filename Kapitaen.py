import random
from Colors import Colors as c


class Kapitaen:

    # constructor
    def __init__(self, name, charisma, experience):
        self._name = name
        self._charisma = charisma
        self._experience = experience

    # methodes
    def Kapitaen(self):
        pass

    def negotiation(self):
        randomInt = random.randint(1, 10)
        success = (self._charisma + self._experience) / randomInt

        if success > 3:
            return "Die Verhandlung war erfolgreich."
        else:
            return "Die Verhandlung war " + c.RED + "nicht" + c.END + " erfolgreich."

    # getter
    def getName(self):
        return self._name

    def getCharisma(self):
        return self._charisma

    def getExperience(self):
        return self._experience

    # setter
    def setName(self, name):
        self._name = name

    def setCharisma(self, charisma):
        self._charisma = charisma

    def setExperience(self, experience):
        self._experience = experience
