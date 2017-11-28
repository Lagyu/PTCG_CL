class Board(object):
    def __init__(self):
        self._BOARD_DIC = [
            "MY_TURN_0", "WAS_MY_TURN_0",
            "DECK_0", "TRASHPILE_0", "LOSTPILE_0",
            "HAND_0",
            "INPLAY_0", "SUPPORTER_PLAYED_0", "ENERGY_ATTACHED_0", "RETREATED_0", "EVOLVED_0",
            "POKEMON_P_0", "POKEMON_D_0", "POKEMON_SC_0", "POKEMON_E_0", "POKEMON_A_0",
            "PRIZE_0", "BOARD_SC_0",
            "STADIUM_0", "STADIUM_PLAYED_0", "STADIUM_PLAYED_1",
            "MY_TURN_1", "WAS_MY_TURN_1",
            "DECK_1", "TRASHPILE_1", "LOSTPILE_1",
            "HAND_1",
            "INPLAY_1", "SUPPORTER_PLAYED_1", "ENERGY_ATTACHED_1", "RETREATED_1", "EVOLVED_1",
            "POKEMON_P_1", "POKEMON_D_1", "POKEMON_SC_1", "POKEMON_E_1", "POKEMON_A_1",
            "PRIZE_1", "BOARD_SC_1"
            ]

        self._BOARD_ELEM = [[]] * len(self._BOARD_DIC)
        self._BOARD_ELEM[self._BOARD_DIC.index("POKEMON_P_0")] = [[], [], [], [], [], [], [], [], []]
        self._BOARD_ELEM[self._BOARD_DIC.index("POKEMON_D_0")] = [[0], [0], [0], [0], [0], [0], [0], [0], [0]]
        self._BOARD_ELEM[self._BOARD_DIC.index("POKEMON_SC_0")] = [{}, {}, {}, {}, {}, {}, {}, {}, {}]
        self._BOARD_ELEM[self._BOARD_DIC.index("POKEMON_E_0")] = [[], [], [], [], [], [], [], [], []]
        self._BOARD_ELEM[self._BOARD_DIC.index("POKEMON_A_0")] = [[], [], [], [], [], [], [], [], []]
        self._BOARD_ELEM[self._BOARD_DIC.index("EVOLVED_0")] = [False, False, False, False, False, False, False, False,
                                                                False]
        self._BOARD_ELEM[self._BOARD_DIC.index("BOARD_SC_0")] = [{}]

        self._BOARD_ELEM[self._BOARD_DIC.index("POKEMON_P_1")] = [[], [], [], [], [], [], [], [], []]
        self._BOARD_ELEM[self._BOARD_DIC.index("POKEMON_D_1")] = [[0], [0], [0], [0], [0], [0], [0], [0], [0]]
        self._BOARD_ELEM[self._BOARD_DIC.index("POKEMON_SC_1")] = [{}, {}, {}, {}, {}, {}, {}, {}, {}]
        self._BOARD_ELEM[self._BOARD_DIC.index("POKEMON_E_1")] = [[], [], [], [], [], [], [], [], []]
        self._BOARD_ELEM[self._BOARD_DIC.index("POKEMON_A_1")] = [[], [], [], [], [], [], [], [], []]
        self._BOARD_ELEM[self._BOARD_DIC.index("EVOLVED_1")] = [False, False, False, False, False, False, False, False,
                                                                False]
        self._BOARD_ELEM[self._BOARD_DIC.index("BOARD_SC_1")] = [{}]

    @property
    def BOARD_ELEM(self):
        return self._BOARD_ELEM

    @property
    def BOARD_DIC(self):
        return self._BOARD_DIC

    @BOARD_ELEM.setter
    def BOARD_ELEM(self, value):
        self._BOARD_ELEM = value

    @BOARD_ELEM.deleter
    def BOARD_ELEM(self):
        del self._BOARD_ELEM

    @BOARD_DIC.setter
    def BOARD_DIC(self, value):
        self._BOARD_DIC = value

    @BOARD_DIC.deleter
    def BOARD_DIC(self):
        del self._BOARD_DIC


