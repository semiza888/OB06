class Game:
    def __init__(self, player_name, computer_name):
        self.player = Hero(player_name)
        self.computer = Hero(computer_name)

    def start(self):
        while True:  # Continue the game until the player decides to exit
            # Случайный выбор, кто начнет атаку первым
            attacker, defender = random.choice([(self.player, self.computer), (self.computer, self.player)])

            while attacker.is_alive() and defender.is_alive():
                if attacker == self.player:
                    # Ожидаем нажатия игрока на клавишу пробел для следующего хода
                    print("Нажмите пробел для следующего хода.")
                    keyboard.wait('space')
                    # Игрок атакует
                    attacker.attack(defender)
                else:
                    # Компьютер атакует
                    attacker.attack(defender)

                # Проверяем уровень жизни игроков
                if not defender.is_alive():
                    print(f"{attacker.name} победил!")
                    break

                # Смена ролей атакующего и обороняющегося
                attacker, defender = defender, attacker

            # Запрос на продолжение игры после завершения игры
            print("Нажмите Shift для продолжения игры или ESC для выхода.")
            key = keyboard.read_key()
            if key == 'esc':
                print("Игра завершена.")
                return  # Завершение цикла игры
            elif key == 'shift':
                # Если пользователь хочет продолжить игру, начинаем новую игру
                self.player.health = 100
                self.computer.health = 100
                continue  # Продолжение цикла игры