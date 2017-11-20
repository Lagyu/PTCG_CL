

BOARD_DIC = [
    "DECK_0", "TRASHPILE_0", "LOSTPILE_0",
    "HAND_0",
    "INPLAY_0", "SUPPORTER_PLAYED_0", "ENERGY_ATTACHED_0", "HAVE_RETREATED_0",
    "POKEMON_P_0", "POKEMON_D_0", "POKEMON_SC_0", "POKEMON_E_0", "POKEMON_A_0",
    "PRIZE_0",
    "STADIUM_0", "STADIUM_PLAYED_0", "STADIUM_PLAYED_1",
    "DECK_1", "TRASHPILE_1", "LOSTPILE_1",
    "HAND_1",
    "INPLAY_1", "SUPPORTER_PLAYED_1", "ENERGY_ATTACHED_1", "HAVE_RETREATED_1",
    "POKEMON_P_0", "POKEMON_D_0", "POKEMON_SC_0", "POKEMON_E_0", "POKEMON_A_0",
    "PRIZE_1"
]
# P means Pokemon, D means damage, SC means special condition, E means Energy and A means Attachment.


'''
    "BATTLEPP_1", "BATTLEPD_1", "BATTLEPSC_1", "BATTLEPE_1", "BATTLEPA_1",
    "BENCHP0_P_1", "BENCHP0_D_1", "BENCHP0_SC_1", "BENCHP0_E_1", "BENCHP0_A_1",
    "BENCHP1_P_1", "BENCHP1_D_1", "BENCHP1_SC_1", "BENCHP1_E_1", "BENCHP1_A_1",
    "BENCHP2_P_1", "BENCHP2_D_1", "BENCHP2_SC_1", "BENCHP2_E_1", "BENCHP2_A_1",
    "BENCHP3_P_1", "BENCHP3_D_1", "BENCHP3_SC_1", "BENCHP3_E_1", "BENCHP3_A_1",
    "BENCHP4_P_1", "BENCHP4_D_1", "BENCHP4_SC_1", "BENCHP4_E_1", "BENCHP4_A_1",
    "BENCHP5_P_1", "BENCHP5_D_1", "BENCHP5_SC_1", "BENCHP5_E_1", "BENCHP5_A_1",
    "BENCHP6_P_1", "BENCHP6_D_1", "BENCHP6_SC_1", "BENCHP6_E_1", "BENCHP6_A_1",
    "BENCHP7_P_1", "BENCHP7_D_1", "BENCHP7_SC_1", "BENCHP7_E_1", "BENCHP7_A_1",
'''


BOARD_ELEM = [[]] * len(BOARD_DIC)
BOARD_ELEM[BOARD_DIC.index("POKEMON_P_0")] = [[], [], [], [], [], [], [], [], []]
BOARD_ELEM[BOARD_DIC.index("POKEMON_D_0")] = [[], [], [], [], [], [], [], [], []]
BOARD_ELEM[BOARD_DIC.index("POKEMON_SC_0")] = [[], [], [], [], [], [], [], [], []]
BOARD_ELEM[BOARD_DIC.index("POKEMON_E_0")] = [[], [], [], [], [], [], [], [], []]
BOARD_ELEM[BOARD_DIC.index("POKEMON_A_0")] = [[], [], [], [], [], [], [], [], []]

# BOARD_ELEM[BOARD_DIC.index("必要な箇所の名前")] = [] で、BOARD_ELEMの要素を取得できる。


def getelemlist(dicname: str):
    element_list = BOARD_ELEM[BOARD_DIC.index(dicname)]
    return element_list
