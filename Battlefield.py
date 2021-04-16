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
        for i in self.robo_list:
            self.show_robo_opponent(i)
            for j in self.dino_list:
                self.show_dino_opponent(j)
                while self.dino_turn(j, i) > 0 and self.robo_turn(j, i) > 0:
                    print(i.name + ' health is now ' + str(i.health))
                    print(i.name + ' power level is now ' + str(i.power_level))
                    print(j.type + ' health is now ' + str(j.health))
                    print(j.type + ' energy is now ' + str(j.energy))
                    self.display_winners(j, i)

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

    def show_dino_opponent(self, dino_pick):
        print('Dinosaurs choice is: ' + dino_pick.type)


    def show_robo_opponent(self, robo_pick):
        print('Robots choice is: ' + robo_pick.name)


    def display_winners(self, dino, robo):
        if dino.health > robo.health:
            print(dino.type + ' is the winner!')
        elif robo.health > dino.health:
            print(robo.name + ' is the winner!')