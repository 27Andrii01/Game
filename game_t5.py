"""
Module...
"""

class  Room:
    """
    Class describe certain room where he is etc
    """
    def __init__(self, name) -> None:
        """
        Method is constructor of class
        """
        self.name = name
        self.description = None
        self.way = {}
        self.character = None
        self.item = None

    def set_description(self, decription):
        """
        Method get description of room
        """
        self.description = decription

    def link_room(self, room, way):
        """
        Method get direction where the room is located
        """
        self.way[way] = room

    def set_character(self, character):
        """
        Method get name of character who is located in certain room 
        """
        self.character = character

    def set_item(self, item):
        """
        Method get name of item which is located in certain room 
        """
        self.item = item

    def get_details(self):
        """
        Method print name and description about certain room
        """
        print(f"{self.name}\n--------------------")
        print(self.description)
        for key, values in self.way.items():
            print(f"{values.name} is {key}")

    def get_character(self):
        """
        Method return name of character who is located in certain room 
        """
        return self.character

    def get_item(self):
        """
        Method return name of item which is located in certain room 
        """
        return self.item

    def move(self, comand):
        """
        Method return direction where main charactern want to go
        """
        return self.way[comand]


class Enemy:
    """
    Class describe characters which will faced with main character
    """
    def __init__(self, name, description):
        """
        Method is constructor of class
        """
        self.name = name
        self.description = description
        self.phrase = None
        self.weapon = None
        self.corps = 0

    def set_conversation(self, phrase):
        """
        Method get discription about conversation
        """
        self.phrase = phrase

    def set_weakness(self, weapon):
        """
        Method get name of thing that can kill enemy 
        """
        self.weapon = weapon

    def describe(self):
        """
        Method print name and description of enemy
        """
        print(f"{self.name} is here!\n{self.description}")

    def talk(self):
        """
        Method print phrase of enemy
        """
        print(f"[{self.name} says]: {self.phrase}")

    def fight(self, fight_with):
        """
        Method check ability of certain item to kill enemy
        """
        if self.weapon == fight_with:
            self.corps += 1
            return True

    def get_defeated(self):
        """
        Method count number of killed enemies
        """
        return self.corps



class Item:
    """
    Class describe items which located in certain room
    """
    def __init__(self, item) -> None:
        """
        Method is constructor of class
        """
        self.item = item
        self.description = None

    def set_description(self, description):
        """
        Method get description of certain item
        """
        self.description = description

    def describe(self):
        """
        Method print description of certain item
        """
        print(f"The [{self.item}] is here - {self.description}")

    def get_name(self):
        """
        Method  return name of item with which you do somethind
        """
        return self.item
