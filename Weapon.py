class Weapon

    def __init__(self, name, attack_power):
        self.name = ''
        self.attack_power = []

    def name(self):
        self.name = input('Weapon name:')
        print(self.name)