import json
import re

from . import Board

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


def check_playable(card_issued: dict, _from: str, _to: str, bench_id: int):
    if _from == "HAND_0":
        if card_issued["supertype"] == "Pokémon":
            if _to == "POKEMON_P_0":
                if Board.BOARD_ELEM[Board.BOARD_DIC.index(_to)][bench_id] == []:
                    if ("evolvesFrom" in card_issued) == False:
                        return True
                elif "evolvesFrom" in card_issued:
                    if Board.BOARD_ELEM[Board.BOARD_DIC.index(_to)][bench_id][-1]["name"] == card_issued["evolvesFrom"]:
                        if Board.BOARD_ELEM[Board.BOARD_DIC.index("EVOLVED_0")][bench_id] == False:
                            return True
            else:
                return False

        elif card_issued["supertype"] == "Trainer":
            if _to == "INPLAY_0":
                if card_issued["subtype"] == "Supporter":
                    if Board.BOARD_ELEM[Board.BOARD_DIC.index("SUPPORTER_PLAYED_0")] == []:
                        return True
                    else:
                        return False
                elif card_issued["subtype"] == "Item":
                    return True

            elif card_issued["subtype"] == "Pok\u00e9mon Tool":
                if _to == "POKEMON_P_0":
                    if Board.BOARD_ELEM[Board.BOARD_DIC.index(_to)][bench_id] == []:
                        return False
                    elif Board.BOARD_ELEM[Board.BOARD_DIC.index("POKEMON_A_0")][bench_id] == []:
                        return True
                    else:
                        return False
                else:
                    return False

            elif card_issued["subtype"] == "Stadium":
                if _to == "STADIUM_0":
                    if Board.BOARD_ELEM[Board.BOARD_DIC.index("STADIUM_PLAYED_0")] == []:
                        if card_issued["name"] != Board.BOARD_ELEM[Board.BOARD_DIC.index("STADIUM_PLAYED_0")][0]["name"]:
                            return True
                else:
                    return False

        elif card_issued["subtype"] == "Energy":
            if _to == "POKEMON_P_0":
                if Board.BOARD_ELEM[Board.BOARD_DIC.index(_to)][bench_id] == []:
                    return False
                else:
                    return True
    else:
        return False


def check_basic_in_hand():
    hand_list = Board.BOARD_ELEM[Board.BOARD_DIC.index("HAND_0")]
    for i in range(len(hand_list)):
        if hand_list[i]["supertype"] == "Pok\u00E9mon":
            if hand_list[i]["subtype"] == "Basic":
                return True
    return False


def check_retreatable():
    parsed_arr = parseenergy(0)
    if check_benched_pokemon_exist():
        if parsed_arr[0] >= len(Board.BOARD_ELEM[Board.BOARD_DIC.index("POKEMON_P_0")][0][-1]["retreatCost"]):
            return True
        elif "FREE_RETREAT_FLAG" in Board.BOARD_ELEM[Board.BOARD_DIC.index("POKEMON_SC_0")][0]:
            return True
    else:
        return False


def check_moveusable(bench_id: int, move_no: int): # move_no は、0,1,2...。
    pokemon_issued = get_pokemon_on_board_dict(bench_id)
    if "attacks" in pokemon_issued:
        if len(pokemon_issued["attacks"]) > move_no:
            parsed_arr = parseenergy(0)
            move_issued = pokemon_issued["attacks"][move_no]
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


def parseenergy(bench_id: int):
    Energyarray = Board.BOARD_ELEM[Board.BOARD_DIC.index("POKEMON_A_0")][bench_id]
    length_energy = len(Energyarray)
    parsed_arr = []
    Regexp_pattern_1 = re.compile(r'\sEnergy$')
    Regexp_pattern_2 = re.compile(r'^Basic\s')
    for i in range(length_energy):
        if Energyarray[i]["subtype"] == "Basic":
            cardname = Energyarray[i]["name"]
            Type = re.sub(Regexp_pattern_1, "", cardname)
            Type = re.sub(Regexp_pattern_2, "", Type)
            parsed_arr.append(Type)
        elif length_energy != len(parsed_arr):
            print("Unknown special energy has been attached.")
    return [length_energy, parsed_arr]


def check_benched_pokemon_exist():
    exist = 0
    for i in range(1, len(Board.BOARD_ELEM[Board.BOARD_DIC.index("POKEMON_P_0")])):
        if Board.BOARD_ELEM[Board.BOARD_DIC.index("POKEMON_P_0")][i] != []:
            exist = exist +1
    if exist == 0:
        return False
    else:
        return True


def get_pokemon_on_board_dict(bench_id: int):
    pokemon_issued = Board.BOARD_ELEM[Board.BOARD_DIC.index("POKEMON_P_0")][bench_id][-1]
    return pokemon_issued


