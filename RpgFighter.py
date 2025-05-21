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
        self.name = name  
        self.cls = cls 
        self.level = 1
        self.xp = 0
        self.defeated = 0
        self.inventory = ["Health Potion", "Mana Potion"]

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

    def is_alive(self):
        return self.hp > 0

    def take_damage(self, dmg):
        self.hp = max(0, self.hp - dmg)

    def heal(self):
        if "Health Potion" in self.inventory:
            self.hp = min(self.max_hp, self.hp + 40)
            self.inventory.remove("Health Potion")
            slow(f"{self.name} kasutas Health Potionit ja paranes!")
        else:
            slow("Pole health potionit!")

    def restore_mana(self):
        if "Mana Potion" in self.inventory:
            self.mana += 40
            self.inventory.remove("Mana Potion")
            slow(f"{self.name} jõi Mana Potionit!")
        else:
            slow("Pole mana potionit!")

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
        slow(f"Statistika paranes!")

    def special_attack(self, enemy):
        if self.cls == "Rüütel":
            self.hp = min(self.max_hp, self.hp + 20)
            slow(f"{self.name} kasutab {self.skill}it ja taastab 20 HP!")
        elif self.cls == "Võlur":
            if self.mana >= 30:
                self.mana -= 30
                dmg = random.randint(25, 35)
                enemy.take_damage(dmg)
                slow(f"{self.name} viskab TULEPALLI 🔥 ja teeb {dmg} kahju!")
            else:
                slow("Pole piisavalt mana!")

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

def fight(player, enemy):
    print(r"""
╔══════════════════════════╗
║     LAHING ALGAB! ⚔️    ║
╚══════════════════════════╝
""")
    while player.is_alive() and enemy.is_alive():
        print(f"\n{player.name} | HP: {player.hp}/{player.max_hp} | Mana: {player.mana} | Tase: {player.level} | XP: {player.xp}")
        print(f"{enemy.name} | HP: {enemy.hp}")
        print("\n1. Ründa\n2. Erirünnak\n3. Kasuta potionit\n4. Põgene")
        choice = input("> ")

        if choice == "1":
            dmg = random.randint(5, player.attack)
            enemy.take_damage(dmg)
            slow(f"{player.name} ründab ja teeb {dmg} kahju!")
        elif choice == "2":
            player.special_attack(enemy)
        elif choice == "3":
            print("a) Health Potion\nb) Mana Potion")
            sub = input("> ").lower()
            if sub == "a":
                player.heal()
            elif sub == "b":
                player.restore_mana()
        elif choice == "4":
            if random.random() < 0.4:
                slow("Põgenemine õnnestus!")
                return False
            else:
                slow("Põgenemine ebaõnnestus!")
        else:
            slow("Tundmatu käik.")
            continue

        if enemy.is_alive():
            dmg = random.randint(4, enemy.attack)
            player.take_damage(dmg)
            slow(f"{enemy.name} ründab ja teeb {dmg} kahju!")

    if player.is_alive():
        print(r"""
╔════════════════════════╗
║ 🎉 SA VÕITSID LAHINGU! ║
╚════════════════════════╝
""")
        player.gain_xp(50)
        player.defeated += 1
        if random.random() < 0.5:
            player.inventory.append("Health Potion")
            slow("Sa leidsid potioni!")
        return True
    else:
        print(r"""
╔══════════════════╗
║    💀 MÄNG LÄBI  ║
╚══════════════════╝
""")
        return False

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

def show_menu():
    print("\n--- PEAMENÜÜ ---")
    print("1. Alusta lahingut")
    print("2. Näita tegelast")
    print("3. Välju mängust")

def main():
    show_title()
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

    if player.is_alive() and player.defeated >= max_enemies:
        slow("\n🎉 Palju õnne! Võitsid kõik vastased ja lõpetasid mängu edukalt!")
    elif not player.is_alive():
        slow("\n😢 Mäng läbi. Proovi uuesti!")

if __name__ == "__main__":
    main()
