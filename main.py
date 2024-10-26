from abc import ABC, abstractmethod

class Weapon(ABC):
    @abstractmethod
    def attack(self):
        pass

    @abstractmethod
    def __str__(self):
        pass

class Sword(Weapon):
    def attack(self):
        print("Боец наносит удар мечом.")

    def __str__(self):
        return "меч"

class Bow(Weapon):
    def attack(self):
        print("Боец наносит удар из лука.")

    def __str__(self):
        return "лук"

class Fighter:
    def __init__(self, weapon: Weapon):
        self.weapon = weapon
        print(f"Боец выбирает {weapon}.")

    def change_weapon(self, new_weapon: Weapon):
        self.weapon = new_weapon
        print(f"Боец выбирает {new_weapon}.")

    def attack(self):
        self.weapon.attack()

class Monster:
    def defeat(self):
        print("Монстр побежден!")

def battle(fighter: Fighter, monster: Monster):
    fighter.attack()
    monster.defeat()


sword = Sword()
bow = Bow()

fighter = Fighter(weapon=sword)

monster = Monster()

battle(fighter, monster)
print()

fighter.change_weapon(bow)

battle(fighter, monster)
