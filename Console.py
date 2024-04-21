if __name__ == "__main__":
    player_name = input("Введите имя игрока: ")
    computer_name = "Компьютер"
    game = Game(player_name, computer_name)
    game.start()