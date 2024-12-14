import time

class Character:
    def __init__(self, name, health, attack):
        self.name = name
        self.health = health
        self.attack = attack

    def take_damage(self, damage):
        self.health = max(self.health - damage, 0)

    def is_alive(self):
        return self.health > 0

    def __str__(self):
        return f"{self.name} (Health: {self.health}, Attack: {self.attack})"

class Boss(Character):
    def __init__(self, name, health, attack):
        super().__init__(name, health, attack)

class Hero(Character):
    def __init__(self, name, health, attack):
        super().__init__(name, health, attack)
        self.alive = True

    def special_ability(self, boss, heroes, round_number):
        pass

class Witcher(Hero):
    def __init__(self, name, health):
        super().__init__(name, health, 0)  # Witcher does not deal damage
        self.revived = False

    def special_ability(self, boss, heroes, round_number):
        if not self.revived:
            for hero in heroes:
                if not hero.is_alive() and hero != self:
                    hero.health = self.health
                    self.health = 0
                    self.revived = True
                    print(f"{self.name} sacrifices himself to revive {hero.name}!")
                    break

class Magic(Hero):
    def __init__(self, name, health, attack, boost_amount):
        super().__init__(name, health, attack)
        self.boost_amount = boost_amount

    def special_ability(self, boss, heroes, round_number):
        if round_number <= 4:
            for hero in heroes:
                if hero != self and hero.is_alive():
                    hero.attack += self.boost_amount
            print(f"{self.name} boosts attack of all heroes by {self.boost_amount} for round {round_number}! Waiting 10 seconds.")
            time.sleep(10)

class Hacker(Hero):
    def __init__(self, name, health, attack, steal_amount):
        super().__init__(name, health, attack)
        self.steal_amount = steal_amount

    def special_ability(self, boss, heroes, round_number):
        if round_number % 2 == 0 and boss.health > 0:
            boss.health -= self.steal_amount
            weakest_hero = min([hero for hero in heroes if hero.is_alive()], key=lambda h: h.health)
            weakest_hero.health += self.steal_amount
            print(f"{self.name} steals {self.steal_amount} health from {boss.name} and gives it to {weakest_hero.name}!")

# Example setup
boss = Boss("Dark Lord", 1000, 50)
heroes = [
    Witcher("Geralt", 300),
    Magic("Gandalf", 250, 30, 10),
    Hacker("Neo", 200, 25, 12)
]

# Simulating rounds
round_number = 1
while boss.is_alive() and any(hero.is_alive() for hero in heroes):
    print(f"\n--- Round {round_number} ---")
    for hero in heroes:
        if hero.is_alive():
            hero.special_ability(boss, heroes, round_number)
            boss.take_damage(hero.attack)
            print(f"{hero.name} attacks {boss.name}, dealing {hero.attack} damage!")

    if boss.is_alive():
        for hero in heroes:
            if hero.is_alive():
                hero.take_damage(boss.attack)
                print(f"{boss.name} attacks {hero.name}, dealing {boss.attack} damage!")

    round_number += 1

print("\n--- Battle Over ---")
if boss.is_alive():
    print(f"{boss.name} wins!")
else:
    print("Heroes win!")

for hero in heroes:
    print(hero)
