import random as r

from Planet import Planet
from Ladung import Ladung
from Kapitaen import Kapitaen
from Colors import Colors as c
from Raumschiff import Raumschiff


class Sonnensystem:

    # main method
    @staticmethod
    def main():

        # |-----------------| #
        # |---- objects ----| #
        # |-----------------| #
        # captains
        captain_x     = Kapitaen("Captain X", 8, 5)
        captain_space = Kapitaen("Captain Space", 3, 9)

        # spaceships
        starship     = Raumschiff("Starship", 0, 0, 150, r.randint(10, 25), r.randint(15, 50), captain_x.getName())
        falcon_heavy = Raumschiff("Falcon Heavy", 1, 1, 100, r.randint(25, 50), r.randint(5, 15), captain_space.getName())

        # planets
        planets = [
            Planet("Erde", True, 2, 2),
            Planet("Mars", True, r.randint(-5, 5), r.randint(-5, 5)),
            Planet("Jupiter", True, r.randint(-5, 5), r.randint(-5, 5))
        ]

        # charge
        energiekern  = Ladung("Energiekerne", 1)
        energiespule = Ladung("Energiespulen", 4)
        energiezelle = Ladung("Energiezellen", 2)

        # set charge to planets
        planets[0].setCharge(energiekern)
        planets[1].setCharge(energiezelle)
        planets[2].setCharge(energiespule)

        # |--------------------| #
        # |---- game start ----| #
        # |--------------------| #
        print(c.RED + "---- Das Spiel startet ----" + c.END)
        print("Sie fliegen das Raumschiff " + c.BLUE + starship.getName() + c.END)
        print("Gesteuert von " + c.YELLOW + starship.getKapitaen() + c.END)

        # game loop
        gameOver = False
        while not gameOver:

            # spaceship coordination
            print("------------------------------")
            print("Raumschiff Koordinaten: " + c.PURPLE + str(starship.getPosX()) + ", " + str(starship.getPosY()) + c.END)
            direction = input("Bewegung (a/w/s/d): ")
            starship.fly(direction)

            # 'spaceship on spaceship' check
            if starship.checkCoordinates(falcon_heavy.getPosX(), falcon_heavy.getPosY()):
                print("------------------------------")
                if falcon_heavy._isDestroyed:
                    print("Das Raumschiff " + c.BLUE + falcon_heavy.getName() + c.END + " wurde schon zerstört")
                else:
                    print("Hier ist das Raumschiff " + c.BLUE + falcon_heavy.getName() + c.END)

                negotiationResult = captain_x.negotiation()
                print(negotiationResult)

                attackAction = input("Möchten Sie angreifen? (Y/n): ")
                if attackAction == 'Y' or attackAction == 'y':
                    while falcon_heavy.getHealthPoints() > 0 and starship.getHealthPoints() > 0:
                        starship.attack(falcon_heavy)
                        print("------------------------------")
                        if falcon_heavy.getHealthPoints() > 0:
                            print(
                                "Das Raumschiff " + c.BLUE + falcon_heavy.getName() + c.END + " hat noch " + c.BOLD + str(
                                    falcon_heavy.getHealthPoints()) + c.END + " Lebenspunkte")
                            falcon_heavy.counterAttack(starship)
                            if starship.getHealthPoints() > 0:
                                print(
                                    "Das Raumschiff " + c.BLUE + starship.getName() + c.END + " hat noch " + c.BOLD + str(
                                        starship.getHealthPoints()) + c.END + " Lebenspunkte")
                                attackAgain = input("Möchten Sie erneut angreifen? (Y/n): ")
                                if attackAgain != 'Y' and attackAgain != 'y':
                                    break
                            else:
                                print("Das Raumschiff " + c.BLUE + starship.getName() + c.END + " wurde zerstört")
                                print(c.RED + "---- Das Spiel ist beendet ----" + c.END)
                                gameOver = True
                        else:
                            print("Das Raumschiff " + c.BLUE + falcon_heavy.getName() + c.END + " wurde zerstört")

            # 'spaceship on planet' check
            for planet in planets:
                if starship.checkCoordinates(planet.getPosX(), planet.getPosY()):
                    print("------------------------------")
                    print("Das Raumschiff " + c.BLUE + starship.getName() + c.END + " ist auf dem Planeten " + c.GREEN + planet.getName() + c.END)
                    print("Die Atmosphäre des Planeten " + c.GREEN + planet.getName() + c.END + " ist " + c.CYAN + str(planet.getAtmosphere()) + c.END)
                    print("Dieser Planet hat " + c.BOLD + str(planet.getCharge().getUnits()) + " " + planet.getCharge().getName() + c.END)

                    # add charge
                    chargeAction = input("Möchten Sie Ladung " + c.PURPLE + "aufnehmen" + c.END + " ? (Y/n): ")
                    if chargeAction == 'Y' or chargeAction == 'y':
                        charge = planet.getCharge()
                        if charge:
                            starship.addCharge(charge)
                            print("------------------------------")
                            print("Eine Ladung " + c.BOLD + charge.getName() + c.END + " wurde aufgenommen")
                        else:
                            print("------------------------------")
                            print("Keine Ladung mehr auf dem Planeten vorhanden.")


if __name__ == '__main__':
    Sonnensystem.main()
