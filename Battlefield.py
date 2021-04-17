from Fleet import Fleet
from Herd import Herd
import random

class Battlefield:
    def __init__(self):
        self.fleet = Fleet()
        self.herd = Herd()
        self.dino_list = Herd().dinosaur_list
        self.robo_list = Fleet().robots_list
        self.weapon_list = Fleet().weapon_list
        self.dino_attacks = Herd().dino_attack_type_list
        self.pick_dino = self.dino_list
        self.pick_robo = self.robo_list

    def run_game(self):
        i = 1
        while i > 0:
            print('Enter Start to begin and Cancel to end')
            start = input()
            if start == 'Start':
                self.display_welcome()
                self.battle()
            elif start == 'Cancel':
                break
            i += 1

    def display_welcome(self):
        print('Welcome to the battlefield of Fleet vs Herd.')

    def battle(self):
        print('Battle will commence.')
        robo_wins = []
        dino_wins = []
        limit = range(len(self.robo_list))
        for i in limit:
            robo_opponent = self.show_robo_opponent(self.robo_list, i)
            dino_opponent = self.show_dino_opponent(self.dino_list, i)
            while self.dino_turn(dino_opponent, robo_opponent) > 0 and self.robo_turn(dino_opponent, robo_opponent) > 0:
                print(robo_opponent.name + ' health is now ' + str(robo_opponent.health))
                print(robo_opponent.name + ' power level is now ' + str(robo_opponent.power_level))
                print(dino_opponent.type + ' health is now ' + str(dino_opponent.health))
                print(dino_opponent.type + ' energy is now ' + str(dino_opponent.energy))
            if dino_opponent.health > robo_opponent.health:
                print(dino_opponent.type + ' is the winner!')
                robo_wins.append(dino_opponent)
            elif robo_opponent.health > dino_opponent.health:
                print(robo_opponent.name + ' is the winner!')
                dino_wins.append(robo_opponent)
        self.display_winners(robo_wins, dino_wins)

    def dino_turn(self, dino, robo):
        robo.weapon = random.choice(self.weapon_list)
        print(robo.name + ' weapon of choice: ' + robo.weapon.type)
        strike_dino = robo.health
        strike_dino = strike_dino - (random.randint(0, dino.attack_power) + robo.weapon.attack_power)
        robo.health = strike_dino
        dino.energy = dino.energy - 10
        return strike_dino

    def robo_turn(self, dino, robo):
        dino.attack_type = random.choice(self.dino_attacks)
        print(dino.type + ' attack of choice: ' + dino.attack_type.type)
        strike_robo = dino.health
        strike_robo = strike_robo - (random.randint(0, robo.attack_power) + robo.weapon.attack_power)
        dino.health = strike_robo
        robo.power_level = robo.power_level - 10
        return strike_robo

    def show_dino_opponent(self, dino_list, i):
        dino_pick = dino_list[i]
        print('Dinosaurs choice is: ' + dino_pick.type)
        return dino_pick

    def show_robo_opponent(self, robo_list, i):
        robo_pick = robo_list[i]
        print('Robots choice is: ' + robo_pick.name)
        return robo_pick

    def display_winners(self, robo, dino):
        robo_count = len(robo)
        dino_count = len(dino)
        if robo_count > dino_count:
            print("The Fleet wins the battle!")
        elif dino_count > robo_count:
            print("The Herd wins the battle!")