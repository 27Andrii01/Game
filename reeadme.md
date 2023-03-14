# Module Game_t6
This module is a text-based adventure game where the player navigates through different streets and interacts with different characters while collecting items to progress through the game.
## Usage
---
To use this module, import it into your Python code:
- import game_t6

Then, you can create street objects with descriptions and items using the Street and Item classes:
#
- peremoga = game_t6.Street("Вулиця Перемоги")
- peremoga.set_description("Одна з багатьох непримітних - вулиць міста. З невеличким магазинчиком")
- food = game_t6.Item("їжа")
- food.set_description("Не можна йти в гості з пустими руками потрібно щось придбати")
peremoga.set_item(food)
#
You can also create enemy characters with dialogue and weaknesses using the Enemy class:
#
- volodia = game_t6.Enemy("Володя", "Дивакуватий безхатько, який не дасть вам спокою поки не отримаю хоча б пару гривень.")
- volodia.set_conversation("Дай 20 гривень")
- volodia.set_weakness("готівка")
- myhailivska.set_character(volodia)
#
Finally, you can link the street objects together and start the game by setting the current_room variable to the starting street:
#
- peremoga.link_room(kiyvska, "на захід")
- kiyvska.link_room(myhailivska, "на південь")
- current_room = peremoga
#
## Gameplay
The objective of the game is to navigate through the streets and collect items while interacting with different characters. Some characters may be enemies, while others may be friendly and offer useful information. The player must also be aware of their surroundings, as some streets may be dangerous or contain obstacles.

To move to a different street, the player can use the link_room method to move to a linked street:

- current_room.linked_rooms["на захід"]

To interact with a character, the player can use the character attribute of the street object:

- current_room.character.talk()

To pick up an item, the player can use the item attribute of the street object:
- item = current_room.item
- backpack.append(item)

The game ends when the player reaches the end of the game or if they die. The player can die if they encounter an enemy without the necessary item to defeat them, or if they make a fatal mistake.

Good luck playing the game!