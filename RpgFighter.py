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

    def gain_xp(self, amount):
        self.xp += amount
        if self.xp >= self.level * 100:
            self.level_up()

    def level_up(self):
        self.level += 1
        self.max_hp += 20
        self.hp = self.max_hp
        self.attack += 3
        self.mana += 20
        print(r"""
    ╔════════════════════════╗
    ║ 🔼 UUS TASE SAAVUTATUD!║
    ╚════════════════════════╝
""")

    # def is_alive(self):
    #     return self.hp > 0
    
    def take_damage(self, dmg):
        self.hp = max(0, self.hp - dmg)

def create_character():
    print("Tere tulemast RPG Fighterisse!")
    name = input("Sisesta oma nimi: ")
    print(r"""
Vali oma klass:
  1. 🛡️  Rüütel – tugev ja vastupidav
  2. 🔮 Võlur – oskuslik ja maagiline
""")
    cls_choice = input("> ")
    cls = "Rüütel" if cls_choice == "1" else "Võlur"
    return Character(name, cls)

# 📋 Mängu menüü
def show_menu():
    print("\n--- PEAMENÜÜ ---")
    print("1. Alusta lahingut")
    # print("2. Näita tegelast")
    print("3. Välju mängust")

# 💀 Vastase klass
class Enemy:
    def __init__(self, number):
        names = ["Zombi", "Ork", "Luukere", "Madu", "Tume Rüütel"]
        self.name = random.choice(names) + f" #{number}"
        self.hp = random.randint(50, 100)
        self.attack = random.randint(6, 14)

    def is_alive(self):
        return self.hp > 0
    
    def take_damage(self, dmg):
        self.hp = max(0, self.hp - dmg)

# ⚔️ Lahingu funktsioon
def fight(player, enemy):
    print(r"""
╔══════════════════════════╗
║     LAHING ALGAB! ⚔️    ║
╚══════════════════════════╝
""")
    while enemy.is_alive(): #and player.is_alive()
        # Kuvatakse statistika
        print(f"\n{player.name} | HP: {player.hp}/{player.max_hp} | Mana: {player.mana} | Tase: {player.level} | XP: {player.xp}")
        print(f"{enemy.name} | HP: {enemy.hp} | Strength: {enemy.attack}")
        print("\n1. Ründa\n4. Põgene")
        choice = input("> ")

        if choice == "1":
            dmg = random.randint(5, player.attack)
            enemy.take_damage(dmg)
            slow(f"{player.name} ründab ja teeb {dmg} kahju!")
        # elif choice == "2":
        #     player.special_attack(enemy)
        # elif choice == "3":
        #     print("a) Potion\nb) Mana Potion")
        #     sub = input("> ").lower()
        #     if sub == "a":
        #         player.heal()
        #     elif sub == "b":
        #         player.restore_mana()
        elif choice == "4":
            if random.random() < 0.4:
                slow("Põgenemine õnnestus!")
                return False
            else:
                slow("Põgenemine ebaõnnestus!")
        else:
            slow("Tundmatu käik.")
            continue

        # Vaenlase vasturünnak
        if enemy.is_alive():
            dmg = random.randint(4, enemy.attack)
            player.take_damage(dmg)
            slow(f"{enemy.name} ründab ja teeb {dmg} kahju!")
    # Lahingu tulemus
    # if player.is_alive():
    print(r"""
╔════════════════════════╗
║ 🎉 SA VÕITSID LAHINGU! ║
╚════════════════════════╝
""")
    player.gain_xp(50)
        # player.defeated += 1
        # if random.random() < 0.5:
        #     player.inventory.append("Potion")
        #     slow("Sa leidsid potioni!")
#         return True
# #     else:
# #         print(r"""
# # ╔══════════════════╗
# # ║    💀 MÄNG LÄBI  ║
# # ╚══════════════════╝
# # """)
#         return False

            
def main():
    show_title()  # Näita ASCII pealkirja
    player = create_character()
    enemy_count = 0
    max_enemies = 5

    while True: #player.is_alive() enemy_count < max_enemies:
        show_menu()
        choice = input("> ")

        if choice == "1":
            enemy_count += 11
            enemy = Enemy(enemy_count)
            won = fight(player, enemy)
            # if not won and not player.is_alive():
            #     break
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