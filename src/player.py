from src.dice import DiceManager, choice, List, Dict, Tuple
from random import choice
import re
from src.utils import sepate_uppercase

class Player():
    def __init__(self,name) -> None:
        self.r_name: str = name
        self.r_race: str = ""
        self.r_class: str = ""
        self.r_old_money: float = 0.0
        self.r_digi_money: float = 0.0
        self.r_status: Dict = {"Strenght": 0, "Dexterity": 0, "Creativity": 0,
                               "Cleverness": 0, "Charm": 0, "Insight": 0, "Resistence": 0, "NuclearResistence": 0}
        self.r_languages: List[str] = []
        self.r_armament: List[str] = []
        self.data_dict: Dict = {}
    def print_player(self) -> Dict:
        self.data_dict["Player"] = sepate_uppercase(self.r_name)
        self.data_dict["Race"] = self.r_race
        self.data_dict["Class"] = self.r_class
        self.data_dict["Old Coin"] = str(self.r_old_money)
        self.data_dict["Digital Coin"] = str(self.r_digi_money)
        for k,v in self.r_status.items():
            self.data_dict[k] = str(v)
        for l in range(len(self.r_languages)):
            self.data_dict[f"Lanaguage {l+1}º"] = self.r_languages[l]
        self.data_dict["Armament"] = ", ".join(self.r_armament)



    def __str__(self) -> str:
        string = ""
        string += f"Player: {self.r_name}:\n"
        string += f"\tRace: {self.r_race}\n"
        string += f"\tClass: {self.r_class}\n"
        string += f"\tOld Money: {self.r_old_money}\n"
        string += f"\tDigi Money: {self.r_digi_money}\n"
        for k, v in self.r_status.items():
            string += f"\t{k}{v}\n"
        string += f"\tLanguages: {self.r_languages}\n"
        string += f"\tArmament: {self.r_armament}\n\n"
        return string


class PlayerManager:
    __players: Dict = {}
    @property
    def players(self):
        return self.__players

    @players.setter
    def players(self, name: str) -> None:
        self.__players[name] = Player(name)

    def set_race(self, name: str, r_race: str):
        self.__players.get(name).r_race = r_race

    def set_class(self, name: str, r_class: str) -> None:
        self.__players.get(name).r_class = r_class

    def set_name(self, name: str):
        self.__players.get(name).r_name = name

    def set_coin(self, name: str, r_old: Tuple = (0, 0), r_digi: Tuple = (0, 0)) -> None:
        self.__players.get(name).r_old_money += choice(r_old)
        self.__players.get(name).r_digi_money += choice(r_digi)

    def set_armament(self, name: str, armament: str) -> None:
        self.__players.get(name).r_armament.append(armament)

    def set_languages(self, name: str, language: str) -> None:
        if language not in self.__players.get(name).r_languages:
            self.__players.get(name).r_languages.append(language)

    def set_status(self, name: str, status_list: List = [""], bonus_list: List = [0]) -> None:
        dice = DiceManager()
        for item in range(len(status_list)):
            dice_list = [i for i in dice.manage(4,6)]
            dice_list.remove(min(dice_list))
            status = sum(dice_list)
            status += bonus_list[item]
            self.__players.get(name).r_status[status_list[item]] = status

