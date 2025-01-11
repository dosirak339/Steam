import random
import time
from data import *
def display_player():
    print(f'Игрок - {["name"]}')
    print(f'Величина атаки - {player["attack"]}. Шанс критического урона ({player["attack"]}ед.) равен {player["luck"]}')
    print(f'Броня поглощает {(1 - player["armor"]) * 100}% урона')


def display_enemy(current_enemy):
    enemy = enemies[current_enemy]
    print(f'Противник - {enemy["name"]}')
    print(f'Веилична атаки - {enemy["attack"]}')
    print(f'Здоровье - {enemy["hp"]}')
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

items = {
 "1" : {"name": "Зелье удачи", "price": 1500},
    "2" : {"name": "Пропуск тренировки", "price": 1000},

}