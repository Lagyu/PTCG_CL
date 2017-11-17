import json
import re
from . import Board
from . import Import_cards
import random

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

sets_card_pre = json.load(open('sm1.json', 'r'))["cards"]
card_test_id = "sm1-1"
card_test = ""
for cards_i in range(len(sets_card_pre)):
    if sets_card_pre[cards_i]["id"] == card_test_id:
        card_test = sets_card_pre[cards_i]
#        print(card_test)
        break
    elif cards_i == len(sets_card_pre) - 1:
        print("no such id: '"+card_test_id+"'.")


def filldeck_x60(a_card_dict: dict):
    if a_card_dict == "":  # データ存在チェック
        print("no card value in param.")
    else:
        l =0
        Board.BOARD_ELEM[Board.BOARD_DIC.index("DECK_0")] = [] # デッキを空にする
        for l in range(60):
            Board.BOARD_ELEM[Board.BOARD_DIC.index("DECK_0")].append(a_card_dict)  # 引数のカードを60枚デッキに加える

def filldeck_random_60(regulation):
    all_card_list = Import_cards.import_all_cards(regulation)
    len_all_card_list = len(all_card_list)
    if all_card_list:
        Board.BOARD_ELEM[Board.BOARD_DIC.index("DECK_0")] = [] # デッキを空にする
        for i in range(60):
            random_float = random.random() * float(len_all_card_list)
            random_int = int(random_float)
            Board.BOARD_ELEM[Board.BOARD_DIC.index("DECK_0")].append(all_card_list[random_int])  # 指定ルール内のカードをランダムに加える
    print(Board.BOARD_ELEM[Board.BOARD_DIC.index("DECK_0")])
    print(str(len(Board.BOARD_ELEM[Board.BOARD_DIC.index("DECK_0")]))+"枚")

# filldeck_x60(card_test)

Pokemon_From_HAND_To_Valid = [ "BATTLEPP_0", "BENCHP0_P_0", "BENCHP1_P_0", "BENCHP2_P_0", "BENCHP3_P_0", "BENCHP4_P_0", "BENCHP5_P_0", "BENCHP6_P_0", "BENCHP7_P_0" ]
Tool_From_HAND_To_Valid = [ "BATTLEPA_0", "BENCHP0_A_0", "BENCHP1_A_0", "BENCHP2_A_0", "BENCHP3_A_0", "BENCHP4_A_0", "BENCHP5_A_0", "BENCHP6_A_0", "BENCHP7_A_0" ]
Energy_From_HAND_To_Valid = ["BATTLEPE_0", "BENCHP0_E_0", "BENCHP1_E_0", "BENCHP2_E_0", "BENCHP3_E_0", "BENCHP4_E_0", "BENCHP5_E_0", "BENCHP6_E_0", "BENCHP7_E_0",]


def check_playable(card_issued: dict, From: str, To: str):
    if From == "HAND_0":
        if card_issued["supertype"] == "Pokémon":
            if To in Pokemon_From_HAND_To_Valid:
                if Board.BOARD_ELEM[Board.BOARD_DIC.index(To)] == []:
                    return True
                elif "evolvesFrom" in card_issued:
                    if Board.BOARD_ELEM[Board.BOARD_DIC.index(To)][-1]["name"] == card_issued["evolvesFrom"]:
                        return True
            else:
                return False

        elif card_issued["supertype"] == "Trainer":
            if To == "INPLAY_0":
                if card_issued["subtype"] == "Supporter":
                    if Board.BOARD_ELEM[Board.BOARD_DIC.index("SUPPORTER_PLAYED_0")] == []:
                        return True
                    else:
                        return False
                elif card_issued["subtype"] == "Item":
                    return True

            elif card_issued["subtype"] == "Pok\u00e9mon Tool":
                if To in Tool_From_HAND_To_Valid:
                    if Board.BOARD_ELEM[Board.BOARD_DIC.index(To)] == []:
                        Index_Attatch = Board.BOARD_DIC.index(To)
                        if Board.BOARD_ELEM[Index_Attatch - 4] != []:
                            return True
                else:
                    return False

            elif card_issued["subtype"] == "Stadium":
                if To == "STADIUM_0":
                    if Board.BOARD_ELEM[Board.BOARD_DIC.index("STADIUM_PLAYED_0")] == []:
                        if card_issued["name"] != Board.BOARD_ELEM[Board.BOARD_DIC.index("STADIUM_PLAYED_0")][0]["name"]:
                            return True
                else:
                    return False

        elif card_issued["subtype"] == "Energy":
            if To in Energy_From_HAND_To_Valid and Board.BOARD_ELEM[Board.BOARD_DIC.index(To)] == []:
                Index_Attatch = Board.BOARD_DIC.index(To)
                if Board.BOARD_ELEM[Index_Attatch - 3] != []:
                    return True
            else:
                return False
    else:
        return False
def draw():
    if Board.BOARD_ELEM[Board.BOARD_DIC.index("DECK_0")] == []:
        print("No more card in your deck!")
        return 0
    else:
        Board.BOARD_ELEM[Board.BOARD_DIC.index("HAND_0")].append(Board.BOARD_ELEM[Board.BOARD_DIC.index("DECK_0")][0])
        Board.BOARD_ELEM[Board.BOARD_DIC.index("DECK_0")].pop(0)

def check_retreatable():
    parsed_arr = parseenergy("BATTLEPE_0")
    if Board.BOARD_ELEM[Board.BOARD_DIC.index("BENCHP0_P_0")] == []:
        if Board.BOARD_ELEM[Board.BOARD_DIC.index("BENCHP1_P_0")] == []:
            if Board.BOARD_ELEM[Board.BOARD_DIC.index("BENCHP2_P_0")] == []:
                if Board.BOARD_ELEM[Board.BOARD_DIC.index("BENCHP3_P_0")] == []:
                    if Board.BOARD_ELEM[Board.BOARD_DIC.index("BENCHP4_P_0")] == []:
                        if Board.BOARD_ELEM[Board.BOARD_DIC.index("BENCHP5_P_0")] == []:
                            if Board.BOARD_ELEM[Board.BOARD_DIC.index("BENCHP6_P_0")] == []:
                                if Board.BOARD_ELEM[Board.BOARD_DIC.index("BENCHP7_P_0")] == []:
                                    return False
    elif parsed_arr[0] >= len(Board.BOARD_ELEM[Board.BOARD_DIC.index("BATTLEPP_0")][-1]["retreatCost"]):
        return True
    elif "FREE_RETREAT_FLAG" in Board.BOARD_ELEM[Board.BOARD_DIC.index("BATTLEPSC_0")]:
        return True
    else:
        return False


def check_moveusable(pokemon_issued: dict, moveno: int): # moveNo は、0,1,2...。
    if "attacks" in pokemon_issued:
        if len(pokemon_issued["attacks"]) > moveno:
            parsed_arr = parseenergy("BATTLEPE_0")
            move_issued = pokemon_issued["attacks"][moveno]
            num_energy_needed = move_issued["convertedEnergyCost"]
            if num_energy_needed < parsed_arr[0]:
                for i in range(num_energy_needed):
                    if move_issued["cost"][i] == "Colorless":
                        return True
                    elif move_issued["cost"][i] in parsed_arr[1]:
                        parsed_arr[1].pop(parsed_arr[1].index(move_issued["cost"][i]))
                    else:
                        return False
    else:
        return False


def parseenergy(object_name: str):
    Energyarray = Board.BOARD_ELEM[Board.BOARD_DIC.index(object_name)]
    length_energy = len(Energyarray)
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


