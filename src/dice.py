from random import choice, randint
from abc import ABC, abstractmethod
from typing import List, Dict, Tuple


class AbstractDice(ABC):
    @abstractmethod
    def roll(self, roll_times: int) -> None:
        pass


class Coin(AbstractDice):
    __sides: List[str] = ["Head", "Tails"]

    def roll(self, roll_times: int) -> str:
        for i in range(roll_times):
            face = choice(self.__sides)
            yield face


class FourFacedDice(AbstractDice):
    __sides: int = 4

    def roll(self, roll_times: int) -> int:
        for i in range(roll_times):
            face = randint(1, self.__sides+1)
            yield face


class SixFacedDice(AbstractDice):
    __sides: int = 6

    def roll(self, roll_times: int) -> int:
        for i in range(roll_times):
            face = randint(1, self.__sides+1)
            yield face


class EightFacedDice(AbstractDice):
    __sides: int = 8

    def roll(self, roll_times: int) -> int:
        for i in range(roll_times):
            face = randint(1, self.__sides+1)
            yield face


class TwelveFacedDice(AbstractDice):
    __sides: int = 12

    def roll(self, roll_times: int) -> int:
        for i in range(roll_times):
            face = randint(1, self.__sides+1)
            yield face


class TwentyFacedDice(AbstractDice):
    __sides: int = 20

    def roll(self, roll_times: int) -> int:
        for i in range(roll_times):
            face = randint(1, self.__sides+1)
            yield face


class DiceManager:
    def __init__(self):
        self.__dices_dict: Dict = {2: Coin, 4: FourFacedDice, 6: SixFacedDice,
                                   8: EightFacedDice, 12: TwelveFacedDice, 20: TwentyFacedDice}

    def manage(self, dice_number: int, roll_times: int) -> List:
        dice = self.__dices_dict[dice_number]()
        return dice.roll(roll_times)
