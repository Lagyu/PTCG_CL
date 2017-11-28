from . import Board_Elements


class Board(object):
    def __init__(self):
        self._BOARD_DIC = Board_Elements.Board_Dic
        self._BOARD_ELEM = Board_Elements.Board_Elem

    @property
    def board_elem(self):
        return self._BOARD_ELEM

    @board_elem.setter
    def board_elem(self, value):
        self._BOARD_ELEM = value
        Board.Board_Elem = self._BOARD_ELEM

    @board_elem.deleter
    def board_elem(self):
        del self._BOARD_ELEM

    def append(self, value):
        self.board_elem = self.board_elem + [value]
        return self.board_elem

    @property
    def board_dic(self):
        return self._BOARD_DIC

    @board_dic.setter
    def board_dic(self, value):
        self._BOARD_DIC = value

    @board_dic.deleter
    def board_dic(self):
        del self._BOARD_DIC


