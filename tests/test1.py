import ptcgcl
import inspect



def test1():
    ptcgcl.Check.filldeck_x60(ptcgcl.Check.card_test)
    print(ptcgcl.Check.check_playable(ptcgcl.Check.card_test, "HAND_0", "POKEMON_P_0", 5))
#    print(len(ptcgcl.Board.BOARD_ELEM[ptcgcl.Board.BOARD_DIC.index("DECK_0")]))




def test_import():
    ptcgcl.Import_cards.import_all_cards("fromXY1")
    ptcgcl.Import_cards.import_all_cards("Standard")




def test_battle_starting():
    ptcgcl.Check.filldeck_random_60("fromXY1")
    for i in range(7):
        ptcgcl.Move.draw()
    print("Drawn 7 cards!")
    print("Hand is: " + str(ptcgcl.Board.BOARD_ELEM[ptcgcl.Board.BOARD_DIC.index("HAND_0")]))
    k = 0
    while ptcgcl.Check.check_basic_in_hand() == False:
        if k < 5:
            print("Mulligan!")
            print(ptcgcl.Board.BOARD_ELEM[ptcgcl.Board.BOARD_DIC.index("HAND_0")])
            ptcgcl.Move.mulligan()
            k = k + 1
        else:
            print("5 times mulligan. Died.")
            return 1
    ptcgcl.Move.put_prize()
    print("placed 6 prize cards.")
    print(len(ptcgcl.Board.BOARD_ELEM[ptcgcl.Board.BOARD_DIC.index("DECK_0")]))





