from Dinosaur import Dinosaur
from Weapon import Weapon

class Herd:
    def __init__(self):
        dinosaur_one = Dinosaur()
        dinosaur_one.type = 'T-Rex'
        dinosaur_one.energy = 100
        dinosaur_one.attack_power = 20
        dinosaur_one.health = 190
        dinosaur_one.attack_type = ''

        dinosaur_two = Dinosaur()
        dinosaur_two.type = 'Brontosaurus'
        dinosaur_two.energy = 90
        dinosaur_two.attack_power = 30
        dinosaur_two.health = 200
        dinosaur_two.attack_type = ''

        dinosaur_three = Dinosaur()
        dinosaur_three.type = 'Pterodactyl'
        dinosaur_three.energy = 80
        dinosaur_three.attack_power = 40
        dinosaur_three.health = 170
        dinosaur_three.attack_type = ''

        dino_attack_one = Weapon()
        dino_attack_one.type = 'Tail Whip'
        dino_attack_one.attack_power = 15

        # dino attacks
        dino_attack_two = Weapon()
        dino_attack_two.type = 'Bite'
        dino_attack_two.attack_power = 20

        dino_attack_three = Weapon()
        dino_attack_three.type = 'Roar'
        dino_attack_three.attack_power = 25

        none = Weapon()
        none.type = 'none'
        none.attack_power = 0

        self.dinosaur_list = [dinosaur_one, dinosaur_two, dinosaur_three]
        self.dino_attack_type_list = (dino_attack_one, dino_attack_two, dino_attack_three, none)