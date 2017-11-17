import json
import re

from ptcgcl import Board
from . import Board
from . import Import_cards
import random


def draw():
    if Board.BOARD_ELEM[Board.BOARD_DIC.index("DECK_0")] == []:
        print("No more card in your deck!")
        return 1
    else:
        Board.BOARD_ELEM[Board.BOARD_DIC.index("HAND_0")].append(Board.BOARD_ELEM[Board.BOARD_DIC.index("DECK_0")][0])
        Board.BOARD_ELEM[Board.BOARD_DIC.index("DECK_0")].pop(0)
        return 0

def shuffle_hand_into_deck():
    for i in range(len(Board.BOARD_ELEM[Board.BOARD_DIC.index("HAND_0")])):
        Board.BOARD_ELEM[Board.BOARD_DIC.index("DECK_0")].append(Board.BOARD_ELEM[Board.BOARD_DIC.index("HAND_0")][i])
    Board.BOARD_ELEM[Board.BOARD_DIC.index("HAND_0")] = []
    random.shuffle(Board.BOARD_ELEM[Board.BOARD_DIC.index("DECK_0")])
    return 0

def mulligan():
    shuffle_hand_into_deck()
    for i in range(7):
        draw()


def put_prize():
    for i in range(6):
        Board.BOARD_ELEM[Board.BOARD_DIC.index("PRIZE_0")].append(Board.BOARD_ELEM[Board.BOARD_DIC.index("DECK_0")][0])
        Board.BOARD_ELEM[Board.BOARD_DIC.index("DECK_0")].pop(0)
    return 0