from Robot import Robot
from Weapon import Weapon


class Fleet:
    def __init__(self):

        robot_one = Robot()
        robot_one.name = 'George'
        robot_one.power_level = 100
        robot_one.weapon = ''
        robot_one.attack_power = 30
        robot_one.health = 200

        robot_two = Robot()
        robot_two.name = 'Jimmy'
        robot_two.power_level = 90
        robot_two.weapon = ''
        robot_two.attack_power = 40
        robot_two.health = 180

        robot_three = Robot()
        robot_three.name = 'Jill'
        robot_three.power_level = 80
        robot_three.weapon = ''
        robot_three.attack_power = 50
        robot_three.health = 160

        self.robots_list = [robot_one, robot_two, robot_three]

        weapon_one = Weapon()
        weapon_one.type = 'revolver'
        weapon_one.attack_power = 10

        weapon_two = Weapon()
        weapon_two.type = 'Light Saber'
        weapon_two.attack_power = 15

        weapon_three = Weapon()
        weapon_three.type = 'Sword'
        weapon_three.attack_power = 20

        none = Weapon()
        none.type = 'none'
        none.attack_power = 0

        self.weapon_list = [weapon_one, weapon_two, weapon_three, none]