class Enemy:
    def __init__(self, x):
        self.energy = x

    def get_energy(self):
        print(self.energy)

cirkit = Enemy(5)
munabhai = Enemy(15)

cirkit.get_energy()
munabhai.get_energy()
