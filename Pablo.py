#Mygame
print("Welcome to the Monster Encounter Simulator!")  

class Character:
    def __init__(self, name, stamina, attack_power, defense):
        self.name = name
        self.stamina = stamina
        self.attack_power = attack_power
        self.defense = defense

    def attack(self, other):
        # Calculate damage dealt to another character based on attack power and defense
        damage = max(0, self.attack_power - other.defense)
        other.take_damage(damage)
        print(f"{self.name} attacks {other.name} for {damage} damage.")

    def take_damage(self, damage):
        # Reduce health by the damage taken, but don't go below 0
        self.health = max(0, self.health - damage)
        print(f"{self.name} takes {damage} damage. Health is now {self.health}.")

    def is_alive(self):
        # Return whether the character is still alive
        return self.health > 0

    def display_info(self):
        # Display character's details
        print(f"{self.name}: Health = {self.health}, Attack = {self.attack_power}, Defense = {self.defense}")

# Example characters
mainCharacter = Character("You", 100, 30, 10)
character_2 = Character("Dragon", 150, 40, 20)

# Display character information
mainCharacter.display_info()
character_2.display_info()

# Example battle between the two characters
mainCharacter.attack(character_2)
character_2.attack(mainCharacter)

# Check if the characters are still alive
if not mainCharacter.is_alive():
    print(f"{mainCharacter.name} has been defeated!")
if not character_2.is_alive():
    print(f"{character_2.name} has been defeated!")
