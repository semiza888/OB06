class Game:
    def __init__(self, player_name, computer_name):
        self.player = Hero(player_name)
        self.computer = Hero(computer_name)

    def start(self):
        while self.player.is_alive() and self.computer.is_alive():
            if random.randint(0, 1) == 0:
                self.player.attack(self.computer)
                if not self.computer.is_alive():
                    print(f"{self.player.name} победил!")
                    break
            else:
                self.computer.attack(self.player)
                if not self.player.is_alive():
                    print(f"{self.computer.name} победил!")
                    break