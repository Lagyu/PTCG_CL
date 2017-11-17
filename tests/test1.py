import ptcgcl
import inspect

def test1():
    ptcgcl.Check.filldeck_x60(ptcgcl.Check.card_test)
    print(ptcgcl.Check.check_playable(ptcgcl.Check.card_test, "HAND_0", "BENCHP5_P_0"))
    print(len(ptcgcl.Board.BOARD_ELEM[ptcgcl.Board.BOARD_DIC.index("DECK_0")]))


def test_import():
    ptcgcl.Import_cards.import_all_cards("fromXY1")
    ptcgcl.Import_cards.import_all_cards("Standard")

def test_randomdeck():
    ptcgcl.Check.filldeck_random_60("fromSM1")

'''
test_import()
print(inspect.getsource(test1))
test1()
'''

