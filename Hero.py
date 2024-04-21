class Hero:
    def __init__(self, name, health=100, attack_power=20):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def attack(self, other):
        # Реализация случайного выбора силы атаки
        attack_power = random.randint(self.attack_power - 5, self.attack_power + 5)
        # Проверка, что уровень здоровья противника не опустился ниже 0
        other.health = max(0, other.health - attack_power)
        print(f"{self.name} нанес {attack_power} урона {other.name}.")
        print(f"У {other.name} осталось {other.health} здоровья.")

    def is_alive(self):
        return self.health > 0