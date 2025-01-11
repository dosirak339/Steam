import random
import time
from helpers import *
from data import *
player = {
    "name": "mammoth",
    "armor": 0.95,
    "hp": 100,
    "attack": 30,
    "lack":50,
    "money":0,
    "inventory": []
}

enemies = [
    {
            "name": "гоблин",
            "hp": 5,
            "attack": 10,
            "skript": "ты слишком легкая добыча, я тебя одолею",
            "win": "черт, извини я был не прав",
            "loss": "я слова не бросаю на ветер",


    }
   
]

name = input("Введите свое имя путешественник ")
player["name"] = name
current_enemy = 0
while True:
    action = input("Выберите действие: 1 - в бой, 2 - тренировка")
    round = random.randint(1, 2)
    enemy = enemies [current_enemy]
    enemy_hp = enemies[current_enemy]["hp"]
    print(f"Противник {enemy['name']}: {enemy['skript']}")
    input("нажмите Enter, чтобы продолжить")
    print()

    while player["hp"] > 0 and enemy_hp > 0:
            if round % 2 == 1:
                print(f"{player['name']} атакует {enemy['name']}")
                skip = "2"
                if items["2"]["name"] in player["inventory"]:skip = input("Желаете пропустить тренировку? 1 - да, 2 - нет")
    if skip == "2":
                crit = random.randint(1, 100)
                if crit < player['lack']:
                    enemy_hp -= player['attack']
                else:
                    enemy_hp -= player['attack']
                time.sleep(1)
                print(f"{player['name']} - {player['hp']}/n{enemy['name']} - {enemy_hp}.")
                print()
                time.sleep(1)
    else:
                print(f"{enemy['name']} атакует {player['name']}")
                player['hp'] -= player['attack'] * player['armor']
                time.sleep(1)
                print(f"{player['name']} - {player['hp']}/n{enemy['name']} - {enemy_hp}.")
                print()
                time.sleep(1)
    round += 1 

    if player['hp'] > 0:
            print(f"Противник - {enemy['name']}: {enemy['win']}")
    else:
            print(f"Противник - {enemy['name']}: {enemy['loss']}")
    player['hp'] = 100
    elif action == '2':
    training_type = input('''1 - тренировать атаку
2 - тренировать оборону
''')
    for i in range(0, 101, 20):
            print(f'Тренировка завершена на {i}%')
            sleep(1.5)
    if training_type == '1':
            player['attack'] += 2
            print(f'Тренировка окончена! Теперь ваша величина атаки равна {player["attack"]}')
    elif training_type == '2':
            player['armor'] -= .09
            print(f'Тренировка окончена! Теперь броня поглощает {100 - player["armor"] * 100}% урона')
    print()

    def display_inventory():
     print("У вас есть")
     for value in player ["inventory"]:
         print(value)
    print(f"У вас {player['money']} монет")
    print()
    if "Зелье удачи" in player["inventory"]:
        potion = input("Желаете выпить зелье удачи? 1 - да, 2 - нет")
        if potion == "1":
            player["luck"] += 7
            print(f"Готово, теперь шанс нанести критический  урон равен {player['luck']}%")
            player["inventory"].remove("Зелье удачи")

def shop():
     print("Добро пожаловать, путник, что хочешь приобрести?")
     print (f"У тебя есть {player['money']}монет")
     for key, value in items.items():
        print(f"{key} - {value['name']}: {value["price"]}")
    
    item = input()
    if item in player["inventory"]:
        print(f"У тебя уже есть {items[item]['name']}")
    elif player['money'] >= items[item]['price']:
        print(f"Ты успешно приобрёл {items[item]['name']}")
        player['inventory'].append(items[item]['name'])
        player['money'] -= items[item]["price"]
    else:
        print("Не хватает монет :(")
    print()
    print("Буду ждать тебя снова, путник!")
    print()

    def shop():
     print("Добро пожаловать, путник, что хочешь приобрести?")
    print(f"У тебя есть {player['money']} монет")
    for key, value in items.items():
        print(f"{key} - {value['name']}: {value['price']}")
    
    item = input()
    if item in player["inventory"]:
        print(f"У тебя уже есть {items[item]['name']}")
    elif player['money'] >= items[item]['price']:
        print(f"Ты успешно приобрёл {items[item]['name']}")
        player['inventory'].append(items[item]['name'])
        player['money'] -= items[item]["price"]
    else:
        print("Не хватает монет :(")
    print()
    print("Буду ждать тебя снова, путник!")
    print()