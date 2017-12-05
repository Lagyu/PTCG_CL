

Board_Dic = [
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
list100 = [["test"]] * 100

Board_Elem = [[]] * len(Board_Dic)
Board_Elem[Board_Dic.index("POKEMON_P_0")] = [[], [], [], [], [], [], [], [], []]
Board_Elem[Board_Dic.index("POKEMON_D_0")] = [[0], [0], [0], [0], [0], [0], [0], [0], [0]]
Board_Elem[Board_Dic.index("POKEMON_SC_0")] = [{}, {}, {}, {}, {}, {}, {}, {}, {}]
Board_Elem[Board_Dic.index("POKEMON_E_0")] = [[], [], [], [], [], [], [], [], []]
Board_Elem[Board_Dic.index("POKEMON_A_0")] = [[], [], [], [], [], [], [], [], []]
Board_Elem[Board_Dic.index("EVOLVED_0")] = [False, False, False, False, False, False, False, False,
                                            False]
Board_Elem[Board_Dic.index("BOARD_SC_0")] = [{}]

Board_Elem[Board_Dic.index("POKEMON_P_1")] = [[], [], [], [], [], [], [], [], []]
Board_Elem[Board_Dic.index("POKEMON_D_1")] = [[0], [0], [0], [0], [0], [0], [0], [0], [0]]
Board_Elem[Board_Dic.index("POKEMON_SC_1")] = [{}, {}, {}, {}, {}, {}, {}, {}, {}]
Board_Elem[Board_Dic.index("POKEMON_E_1")] = [[], [], [], [], [], [], [], [], []]
Board_Elem[Board_Dic.index("POKEMON_A_1")] = [[], [], [], [], [], [], [], [], []]
Board_Elem[Board_Dic.index("EVOLVED_1")] = [False, False, False, False, False, False, False, False,
                                            False]
Board_Elem[Board_Dic.index("BOARD_SC_1")] = [{}]




