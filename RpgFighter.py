import random
import time

def slow(text):
    for c in text:
        print(c, end="", flush=True)
        time.sleep(0.01)
    print()

def show_title():
    print(r"""
  _____   _____    _____       ______  _____  _____  _    _  _______  ______  _____  
 |  __ \ |  __ \  / ____|     |  ____||_   _|/ ____|| |  | ||__   __||  ____||  __ \ 
 | |__) || |__) || |  __      | |__     | | | |  __ | |__| |   | |   | |__   | |__) |
 |  _  / |  ___/ | | |_ |     |  __|    | | | | |_ ||  __  |   | |   |  __|  |  _  / 
 | | \ \ | |     | |__| |     | |      _| |_| |__| || |  | |   | |   | |____ | | \ \ 
 |_|  \_\|_|      \_____|     |_|     |_____|\_____||_|  |_|   |_|   |______||_|  \_\
                                                                                     
                                                                                          
    """)

class Character:
    def __init__(self, name, cls):
        self.name = name  # Nimi
        self.cls = cls    # Klass (Rüütel / Võlur)
        self.level = 1
        self.xp = 0
        self.defeated = 0
        self.inventory = ["Potion", "Mana Potion"]

        # Klassipõhine statistika
        if cls == "Rüütel":
            self.max_hp = 120
            self.hp = self.max_hp
            self.attack = 10
            self.mana = 30
            self.skill = "Shield Block"
        elif cls == "Võlur":
            self.max_hp = 70
            self.hp = self.max_hp
            self.attack = 6
            self.mana = 100
            self.skill = "Fireball"

def create_character():
    print("Tere tulemast RPG Fighterisse!")
    name = input("Sisesta oma nimi: ")
    print(r"""
Vali oma klass:
  1. 🛡️ Rüütel – tugev ja vastupidav
  2. 🔮 Võlur – oskuslik ja maagiline
""")
    cls_choice = input("> ")
    cls = "Rüütel" if cls_choice == "1" else "Võlur"
    return Character(name, cls)

            
def main():
    show_title()  # Näita ASCII pealkirja
    player = create_character()
    enemy_count = 0
    max_enemies = 5

    while player.is_alive() and enemy_count < max_enemies:
        show_menu()
        choice = input("> ")

        if choice == "1":
            enemy_count += 1
            enemy = Enemy(enemy_count)
            won = fight(player, enemy)
            if not won and not player.is_alive():
                break
        elif choice == "2":
            print(f"\n{player.name} | Klass: {player.cls}")
            print(f"Tase: {player.level} | XP: {player.xp} | HP: {player.hp}/{player.max_hp} | Mana: {player.mana}")
            print("Inventar:", player.inventory)
            print(f"Võidetud vaenlasi: {player.defeated}/{max_enemies}")
        elif choice == "3":
            slow("Tänan mängimast! Kohtumiseni!")
            break
        else:
            print("Tundmatu valik.")
            
if __name__ == "__main__":
    main()