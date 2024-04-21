class Hero:
    def __init__(self, name, health=100, attack_power=20):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def attack(self, other):
        other.health -= self.attack_power
        print(f"{self.name} нанес {self.attack_power} урона {other.name}.")
        print(f"У {other.name} осталось {other.health} здоровья.")

    def is_alive(self):
        return self.health > 0