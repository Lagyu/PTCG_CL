import json
import re

from ptcgcl import Board
from . import Board
from . import Import_cards
from . import Check
import random
import traceback


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


def shuffle_deck():
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


def attach_energy(_from: str, card_no: int, bench_id: int):
    if Board.BOARD_ELEM[Board.BOARD_DIC.index("POKEMON_P_0")][bench_id] != []:
        try:
            Board.BOARD_ELEM[Board.BOARD_DIC.index("POKEMON_E_0")][bench_id].append(Board.BOARD_ELEM[Board.BOARD_DIC.index(_from)][card_no])
            Board.BOARD_ELEM[Board.BOARD_DIC.index(_from)].pop(card_no)
            return True
        except:
            traceback.print_exc()
            return False
    else:
        return False


def play_pokemon_from_hand(card_no: int, bench_id: int):
    if Check.check_playable(Board.BOARD_ELEM[Board.BOARD_DIC.index("HAND_0")][card_no], "HAND_0", "POKEMON_P_0", bench_id):
        try:
            Board.BOARD_ELEM[Board.BOARD_DIC.index("POKEMON_P_0")][bench_id].append(Board.BOARD_ELEM[Board.BOARD_DIC.index("HAND_0")][card_no])
            Board.BOARD_ELEM[Board.BOARD_DIC.index("HAND_0")].pop(card_no)
            return True
        except:
            traceback.print_exc()
            return False
    else:
        return False


def attach_energy_from_hand(card_no: int, bench_id: int):
    if Check.check_playable(Board.BOARD_ELEM[Board.BOARD_DIC.index("HAND_0")][card_no], "HAND_0", "POKEMON_P_0", bench_id):
        if Board.BOARD_ELEM[Board.BOARD_DIC.index("ENERGY_ATTACHED_0")] == []:
            try:
                Board.BOARD_ELEM[Board.BOARD_DIC.index("POKEMON_E_0")][bench_id].append(Board.BOARD_ELEM[Board.BOARD_DIC.index("HAND_0")][card_no])
                Board.BOARD_ELEM[Board.BOARD_DIC.index("HAND_0")].pop(card_no)
                Board.BOARD_ELEM[Board.BOARD_DIC.index("ENERGY_ATTACHED_0")].append("Already Attached.")
                return True
            except:
                traceback.print_exc()
                return False
        else:
            print("You have already attached Energy this turn.")
        return True
    else:
        return False


def do_move(move_no: int):
    if Check.check_moveusable(move_no):
        if Board.BOARD_ELEM[Board.BOARD_DIC.index("POKEMON_P_0")][0][-1]["attacks"][move_no]["text"] == "":
            damage = Board.BOARD_ELEM[Board.BOARD_DIC.index("POKEMON_P_0")][0][-1]["attacks"][move_no]["damage"]
            Board.BOARD_ELEM[Board.BOARD_DIC.index("POKEMON_D_1")][0][0] = Board.BOARD_ELEM[Board.BOARD_DIC.index("POKEMON_D_1")][0][0] + damage
            return True
        else:
            # ここにテキストのある技の処理を書く
            return False
    else:
        return False

def end_turn():
    pokemon_check()


def pokemon_check():

    # ここにポケモンチェックの内容を書く

    # ここから手番プレイヤー変更処理
    if Board.BOARD_ELEM[Board.BOARD_DIC.index("MY_TURN_0")] == [1]:
        Board.BOARD_ELEM[Board.BOARD_DIC.index("MY_TURN_0")] = []
        Board.BOARD_ELEM[Board.BOARD_DIC.index("MY_TURN_1")] = [1]
    elif Board.BOARD_ELEM[Board.BOARD_DIC.index("MY_TURN_1")] == [1]:
        Board.BOARD_ELEM[Board.BOARD_DIC.index("MY_TURN_1")] = []
        Board.BOARD_ELEM[Board.BOARD_DIC.index("MY_TURN_0")] = [1]

