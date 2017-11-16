import json
import re
import inspect

BOARD_DIC = [
    "DECK_0", "TRASHPILE_0", "LOSTPILE_0",
    "HAND_0",
    "INPLAY_0", "SUPPORTER_PLAYED_0", "ENERGY_ATTACHED_0", "HAVE_RETREATED_0",
    "BATTLEPP_0", "BATTLEPD_0", "BATTLEPSC_0", "BATTLEPE_0", "BATTLEPA_0",
    "BENCHP0_P_0", "BENCHP0_D_0", "BENCHP0_SC_0", "BENCHP0_E_0", "BENCHP0_A_0",
    "BENCHP1_P_0", "BENCHP1_D_0", "BENCHP1_SC_0", "BENCHP1_E_0", "BENCHP1_A_0",
    "BENCHP2_P_0", "BENCHP2_D_0", "BENCHP2_SC_0", "BENCHP2_E_0", "BENCHP2_A_0",
    "BENCHP3_P_0", "BENCHP3_D_0", "BENCHP3_SC_0", "BENCHP3_E_0", "BENCHP3_A_0",
    "BENCHP4_P_0", "BENCHP4_D_0", "BENCHP4_SC_0", "BENCHP4_E_0", "BENCHP4_A_0",
    "BENCHP5_P_0", "BENCHP5_D_0", "BENCHP5_SC_0", "BENCHP5_E_0", "BENCHP5_A_0",
    "BENCHP6_P_0", "BENCHP6_D_0", "BENCHP6_SC_0", "BENCHP6_E_0", "BENCHP6_A_0",
    "BENCHP7_P_0", "BENCHP7_D_0", "BENCHP7_SC_0", "BENCHP7_E_0", "BENCHP7_A_0",
    "PRIZE0_0", "PRIZE1_0", "PRIZE2_0", "PRIZE3_0", "PRIZE4_0", "PRIZE5_0",
    "STADIUM_0", "STADIUM_PLAYED_0", "STADIUM_PLAYED_1",
    "DECK_1", "TRASHPILE_1", "LOSTPILE_1",
    "HAND_1",
    "INPLAY_1", "SUPPORTER_PLAYED_1", "ENERGY_ATTACHED_1", "HAVE_RETREATED_1",
    "BATTLEPP_1", "BATTLEPD_1", "BATTLEPSC_1", "BATTLEPE_1", "BATTLEPA_1",
    "BENCHP0_P_1", "BENCHP0_D_1", "BENCHP0_SC_1", "BENCHP0_E_1", "BENCHP0_A_1",
    "BENCHP1_P_1", "BENCHP1_D_1", "BENCHP1_SC_1", "BENCHP1_E_1", "BENCHP1_A_1",
    "BENCHP2_P_1", "BENCHP2_D_1", "BENCHP2_SC_1", "BENCHP2_E_1", "BENCHP2_A_1",
    "BENCHP3_P_1", "BENCHP3_D_1", "BENCHP3_SC_1", "BENCHP3_E_1", "BENCHP3_A_1",
    "BENCHP4_P_1", "BENCHP4_D_1", "BENCHP4_SC_1", "BENCHP4_E_1", "BENCHP4_A_1",
    "BENCHP5_P_1", "BENCHP5_D_1", "BENCHP5_SC_1", "BENCHP5_E_1", "BENCHP5_A_1",
    "BENCHP6_P_1", "BENCHP6_D_1", "BENCHP6_SC_1", "BENCHP6_E_1", "BENCHP6_A_1",
    "BENCHP7_P_1", "BENCHP7_D_1", "BENCHP7_SC_1", "BENCHP7_E_1", "BENCHP7_A_1",
    "PRIZE0_1", "PRIZE1_1", "PRIZE2_1", "PRIZE3_1", "PRIZE4_1", "PRIZE5_1"
]

BOARD_ELEM = [[]] * len(BOARD_DIC)
# BOARD_ELEM[BOARD_DIC.index("必要な箇所の名前")] = [] で、BOARD_ELEMの要素を取得できる。

'''
カードの例
        {
            "artist": "Ayaka Yoshida",
            "attacks": [
                {
                    "convertedEnergyCost": 2,
                    "cost": [
                        "Water",
                        "Colorless"
                    ],
                    "damage": "20+",
                    "name": "Second Bite",
                    "text": "This attack does 10 more damage for each damage counter on your opponent's Active Pok\u00e9mon."
                },
                {
                    "convertedEnergyCost": 3,
                    "cost": [
                        "Water",
                        "Colorless",
                        "Colorless"
                    ],
                    "damage": "70",
                    "name": "Crystal Ray",
                    "text": "During your opponent's next turn, prevent all damage done to this Pok\u00e9mon by attacks from Evolution Pok\u00e9mon."
                }
            ],
            "hp": "170",
            "id": "xy10-20",
            "imageUrl": "https://images.pokemontcg.io/xy10/20.png",
            "imageUrlHiRes": "https://images.pokemontcg.io/xy10/20_hires.png",
            "name": "Glaceon-EX",
            "nationalPokedexNumber": 471,
            "number": "20",
            "rarity": "Rare Holo EX",
            "retreatCost": [
                "Colorless",
                "Colorless"
            ],
            "series": "XY",
            "set": "Fates Collide",
            "setCode": "xy10",
            "subtype": "EX",
            "supertype": "Pok\u00e9mon",
            "text": [
                "When a Pok\u00e9mon-EX has been Knocked Out, your opponent takes 2 Prize cards."
            ],
            "types": [
                "Water"
            ],
            "weaknesses": [
                {
                    "type": "Metal",
                    "value": "\u00d72"
                }
            ]
        }

'''

sets_card_pre = json.load(open('sm1.json','r'))["cards"]
card_test_id = "sm1-1"
card_test = ""
for cards_i in range(len(sets_card_pre)):
    if sets_card_pre[cards_i]["id"] == card_test_id:
        card_test = sets_card_pre[cards_i]
#        print(card_test)
        break
    elif cards_i == len(sets_card_pre) -1 :
        print("no such id: '"+card_test_id+"'.")


def filldeck_x60(a_card_dict):
    if a_card_dict == "": # データ存在チェック
        print("no card value in param.")
    else:
        l =0
        BOARD_ELEM[BOARD_DIC.index("DECK_0")] = [] # デッキを空にする
        for l in range(60):
            BOARD_ELEM[BOARD_DIC.index("DECK_0")].append(a_card_dict) # 引数のカードを60枚デッキに加える



Pokemon_From_HAND_To_Valid = [ "BATTLEPP_0", "BENCHP0_P_0", "BENCHP1_P_0", "BENCHP2_P_0", "BENCHP3_P_0", "BENCHP4_P_0", "BENCHP5_P_0", "BENCHP6_P_0", "BENCHP7_P_0" ]
Tool_From_HAND_To_Valid = [ "BATTLEPA_0", "BENCHP0_A_0", "BENCHP1_A_0", "BENCHP2_A_0", "BENCHP3_A_0", "BENCHP4_A_0", "BENCHP5_A_0", "BENCHP6_A_0", "BENCHP7_A_0" ]
Energy_From_HAND_To_Valid = ["BATTLEPE_0", "BENCHP0_E_0", "BENCHP1_E_0", "BENCHP2_E_0", "BENCHP3_E_0", "BENCHP4_E_0", "BENCHP5_E_0", "BENCHP6_E_0", "BENCHP7_E_0",]

def check_playable(card_issued, From, To):
    if From == "HAND_0":
        if card_issued["supertype"] == "Pokémon":
            if To in Pokemon_From_HAND_To_Valid:
                if BOARD_ELEM[BOARD_DIC.index(To)] == []:
                    return True
                elif "evolvesFrom" in card_issued:
                    if BOARD_ELEM[BOARD_DIC.index(To)][-1]["name"] == card_issued["evolvesFrom"]:
                        return True
            else:
                return False

        elif card_issued["supertype"] == "Trainer":
            if To == "INPLAY_0":
                if card_issued["subtype"] == "Supporter":
                    if BOARD_ELEM[BOARD_DIC.index("SUPPORTER_PLAYED_0")] == []:
                        return True
                    else:
                        return False
                elif card_issued["subtype"] == "Item":
                    return True

            elif card_issued["subtype"] == "Pok\u00e9mon Tool":
                if To in Tool_From_HAND_To_Valid:
                    if BOARD_ELEM[BOARD_DIC.index(To)] == []:
                        Index_Attatch = BOARD_DIC.index(To)
                        if BOARD_ELEM[Index_Attatch - 4] != []:
                            return True
                else:
                    return False

            elif card_issued["subtype"] == "Stadium":
                if To == "STADIUM_0":
                    if BOARD_ELEM[BOARD_DIC.index("STADIUM_PLAYED_0")] == []:
                        if card_issued["name"] != BOARD_ELEM[BOARD_DIC.index("STADIUM_PLAYED_0")][0]["name"]:
                            return True
                else:
                    return False

        elif card_issued["subtype"] == "Energy":
            if To in Energy_From_HAND_To_Valid and BOARD_ELEM[BOARD_DIC.index(To)] == []:
                Index_Attatch = BOARD_DIC.index(To)
                if BOARD_ELEM[Index_Attatch - 3] != []:
                    return True
            else:
                return False
    else:
        return False
def draw():
    if BOARD_ELEM[BOARD_DIC.index("DECK_0")] == []:
        print("No more card in your deck!")
        return 0
    else:
        BOARD_ELEM[BOARD_DIC.index("HAND_0")].append(BOARD_ELEM[BOARD_DIC.index("DECK_0")][0])
        BOARD_ELEM[BOARD_DIC.index("DECK_0")].pop(0)

def check_retreatable():
    parsed_arr = parseenergy("BATTLEPE_0")
    if BOARD_ELEM[BOARD_DIC.index("BENCHP0_P_0")] == []:
        if BOARD_ELEM[BOARD_DIC.index("BENCHP1_P_0")] == []:
            if BOARD_ELEM[BOARD_DIC.index("BENCHP2_P_0")] == []:
                if BOARD_ELEM[BOARD_DIC.index("BENCHP3_P_0")] == []:
                    if BOARD_ELEM[BOARD_DIC.index("BENCHP4_P_0")] == []:
                        if BOARD_ELEM[BOARD_DIC.index("BENCHP5_P_0")] == []:
                            if BOARD_ELEM[BOARD_DIC.index("BENCHP6_P_0")] == []:
                                if BOARD_ELEM[BOARD_DIC.index("BENCHP7_P_0")] == []:
                                    return False
    elif parsed_arr[0] >= len(BOARD_ELEM[BOARD_DIC.index("BATTLEPP_0")][-1]["retreatCost"]):
        return True
    elif "FREE_RETREAT_FLAG" in BOARD_ELEM[BOARD_DIC.index("BATTLEPSC_0")]:
        return True
    else:
        return False


def check_moveusable(pokemon_issued, moveno): # moveNo は、0,1,2...。
    if "attacks" in pokemon_issued:
        if len(pokemon_issued["attacks"]) > moveno:
            parsed_arr = parseenergy("BATTLEPE_0")
            move_issued = pokemon_issued["attacks"][moveno]
            num_energy_needed = move_issued["convertedEnergyCost"]
            if num_energy_needed < parsed_arr[0]:
                i = 0
                for i in range(num_energy_needed):
                    if move_issued["cost"][i] == "Colorless":
                        return True
                    elif move_issued["cost"][i] in parsed_arr[1]:
                        parsed_arr[1].pop(parsed_arr[1].index(move_issued["cost"][i]))
                    else:
                        return False
    else:
        return False


def parseenergy(object_name):
    Energyarray = BOARD_ELEM[BOARD_DIC.index(object_name)]
    length_energy = len(Energyarray)
    i = 0
    parsed_arr = []
    Regexp_pattern = re.compile(r'\sEnergy$')
    for i in range(length_energy):
        if Energyarray[i]["subtype"] == "Basic":
            cardname = Energyarray[i]["name"]
            Type = re.sub(Regexp_pattern, "", cardname)
            parsed_arr.append(Type)
        elif length_energy != len(parsed_arr):
            print("Unknown special energy has been attached.")
    return [length_energy, parsed_arr]

def test1():
    filldeck_x60(card_test)
    print(check_playable(card_test, "HAND_0", "BENCHP5_P_0"))
    print(len(BOARD_ELEM[BOARD_DIC.index("DECK_0")]))


print(inspect.getsource(test1))
test1()


