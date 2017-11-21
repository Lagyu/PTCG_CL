import ptcgcl

import ptcgcl.Build_Deck


def test1():
    ptcgcl.Check.filldeck_x60(ptcgcl.Check.card_test)
    print(ptcgcl.Check.check_playable(ptcgcl.Check.card_test, "HAND_0", "POKEMON_P_0", 5))
#    print(len(ptcgcl.Board.BOARD_ELEM[ptcgcl.Board.BOARD_DIC.index("DECK_0")]))


def test_import():
    ptcgcl.Import_cards.import_all_cards("fromXY1")
    ptcgcl.Import_cards.import_all_cards("Standard")
    ptcgcl.Import_cards.get_basic_energies_json()
# 現状、"fromXY1"、"Standard"、"fromSM1"を実装済み


def test_battle_starting():
    ptcgcl.Build_Deck.load_from_file("test.csv")
    ptcgcl.Perform.shuffle_deck()
    for i in range(7):
        ptcgcl.Perform.draw()
    print("Drawn 7 cards!")
    print("Hand is: " + str(ptcgcl.Board.BOARD_ELEM[ptcgcl.Board.BOARD_DIC.index("HAND_0")]))
    k = 0
    while not ptcgcl.Check.check_basic_in_hand():
        if k < 100:
            print("Mulligan!")
            print(ptcgcl.Board.BOARD_ELEM[ptcgcl.Board.BOARD_DIC.index("HAND_0")])
            ptcgcl.Perform.mulligan()
            print("New hand is: " + str(ptcgcl.Board.BOARD_ELEM[ptcgcl.Board.BOARD_DIC.index("HAND_0")]))
            k = k + 1
        else:
            print("100 times mulligan. There should be no basics.")  # たねポケモン入ってないデッキで無限マリガンするのを防ぐ
            return 1

    hand_name_str = ""
    for i in range(len(ptcgcl.Board.BOARD_ELEM[ptcgcl.Board.BOARD_DIC.index("HAND_0")])):
        hand_name_str = hand_name_str + ", " + ptcgcl.Board.BOARD_ELEM[ptcgcl.Board.BOARD_DIC.index("HAND_0")][i]["name"]
    print("Hand(Name only) is" + hand_name_str)

    ptcgcl.Perform.put_prize()
    print("placed 6 prize cards.")
    print("Deck count: "+str(len(ptcgcl.Board.BOARD_ELEM[ptcgcl.Board.BOARD_DIC.index("DECK_0")])))





