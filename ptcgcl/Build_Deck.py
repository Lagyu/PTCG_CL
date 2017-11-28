import random
from . import Import_cards, Board
import csv


def filldeck_random_60(regulation):
    all_card_list = Import_cards.import_all_cards(regulation)
    len_all_card_list = len(all_card_list)
    if all_card_list:
        Board.Board().BOARD_ELEM[Board.Board().BOARD_DIC.index("DECK_0")] = [] # デッキを空にする
        for i in range(60):
            random_float = random.random() * float(len_all_card_list)
            random_int = int(random_float)
            Board.Board().BOARD_ELEM[Board.Board().BOARD_DIC.index("DECK_0")].append(all_card_list[random_int])  # 指定ルール内のカードをランダムに加える
    print(Board.Board().BOARD_ELEM[Board.Board().BOARD_DIC.index("DECK_0")])
    print(str(len(Board.Board().BOARD_ELEM[Board.Board().BOARD_DIC.index("DECK_0")]))+"枚")


def filldeck_random_without_basics_60(regulation):
    all_card_list = Import_cards.import_all_cards(regulation)
    len_all_card_list = len(all_card_list)
    if all_card_list:
        Board.Board().BOARD_ELEM[Board.Board().BOARD_DIC.index("DECK_0")] = [] # デッキを空にする
        for i in range(60):
            random_float = random.random() * float(len_all_card_list)
            random_int = int(random_float)
            while all_card_list[random_int]["subtype"] == "Basic":
                random_int = int(random.random() * float(len_all_card_list))
            Board.Board().BOARD_ELEM[Board.Board().BOARD_DIC.index("DECK_0")].append(all_card_list[random_int])  # 指定ルール内のカードをランダムに加える

    print(Board.Board().BOARD_ELEM[Board.Board().BOARD_DIC.index("DECK_0")])
    print(str(len(Board.Board().BOARD_ELEM[Board.Board().BOARD_DIC.index("DECK_0")]))+"枚")



def load_from_file(filename: str):
    with open(filename) as fp:
        deck_lists = list(csv.reader(fp))
    deck_list = deck_lists[0]
    if len(deck_list) == 60:
        all_card_list = Import_cards.import_all_cards("fromXY1")
        len_all_card_list = len(all_card_list)
        Board.Board().BOARD_ELEM[Board.Board().BOARD_DIC.index("DECK_0")] = []  # デッキを空にする
        for i in range(60):
            id_i = deck_list[i]
            for k in range(len_all_card_list):
                if all_card_list[k]["id"] == id_i:
                    piyo = k
            Board.Board().BOARD_ELEM[Board.Board().BOARD_DIC.index("DECK_0")].append(
                all_card_list[piyo])  # CSVファイルで指定したidのカードを加える
        print(Board.Board().BOARD_ELEM[Board.Board().BOARD_DIC.index("DECK_0")])
        print(str(len(Board.Board().BOARD_ELEM[Board.Board().BOARD_DIC.index("DECK_0")])) + "枚")


def load_from_file(filename: str):
    with open(filename) as fp:
        deck_lists = list(csv.reader(fp))
    deck_list = deck_lists[0]
    if len(deck_list) == 60:
        all_card_list = Import_cards.import_all_cards("fromXY1")
        len_all_card_list = len(all_card_list)
        Board.Board().BOARD_ELEM[Board.Board().BOARD_DIC.index("DECK_0")] = []  # デッキを空にする
        for i in range(60):
            id_i = deck_list[i]
            for k in range(len_all_card_list):
                if all_card_list[k]["id"] == id_i:
                    piyo = k
            Board.Board().BOARD_ELEM[Board.Board().BOARD_DIC.index("DECK_0")].append(
                all_card_list[piyo])  # CSVファイルで指定したidのカードを加える
        print(Board.Board().BOARD_ELEM[Board.Board().BOARD_DIC.index("DECK_0")])
        print(str(len(Board.Board().BOARD_ELEM[Board.Board().BOARD_DIC.index("DECK_0")])) + "枚")
