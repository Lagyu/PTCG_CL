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
        Board.Board().BOARD_ELEM[Board.Board().BOARD_DIC.index("DECK_0")] = [] # デッキを空にする
        for l in range(60):
            Board.Board().BOARD_ELEM[Board.Board().BOARD_DIC.index("DECK_0")].append(a_card_dict)  # 引数のカードを60枚デッキに加える


def check_playable(card_issued: dict, _from: str, _to: str, bench_id: int):
    if _from == "HAND_0":
        if card_issued["supertype"] == "Pokémon":
            if _to == "POKEMON_P_0":
                if Board.Board().BOARD_ELEM[Board.Board().BOARD_DIC.index(_to)][bench_id] == []:
                    if ("evolvesFrom" in card_issued) == False:
                        return True
                elif "evolvesFrom" in card_issued:
                    if Board.Board().BOARD_ELEM[Board.Board().BOARD_DIC.index(_to)][bench_id][-1]["name"] == card_issued["evolvesFrom"]:
                        if Board.Board().BOARD_ELEM[Board.Board().BOARD_DIC.index("EVOLVED_0")][bench_id] == False:
                            return True
            else:
                return False

        elif card_issued["supertype"] == "Trainer":
            if _to == "INPLAY_0":
                if card_issued["subtype"] == "Supporter":
                    if Board.Board().BOARD_ELEM[Board.Board().BOARD_DIC.index("SUPPORTER_PLAYED_0")] == []:
                        return True
                    else:
                        return False
                elif card_issued["subtype"] == "Item":
                    return True

            elif card_issued["subtype"] == "Pok\u00e9mon Tool":
                if _to == "POKEMON_P_0":
                    if Board.Board().BOARD_ELEM[Board.Board().BOARD_DIC.index(_to)][bench_id] == []:
                        return False
                    elif Board.Board().BOARD_ELEM[Board.Board().BOARD_DIC.index("POKEMON_A_0")][bench_id] == []:
                        return True
                    else:
                        return False
                else:
                    return False

            elif card_issued["subtype"] == "Stadium":
                if _to == "STADIUM_0":
                    if Board.Board().BOARD_ELEM[Board.Board().BOARD_DIC.index("STADIUM_PLAYED_0")] == []:
                        if card_issued["name"] != Board.Board().BOARD_ELEM[Board.Board().BOARD_DIC.index("STADIUM_PLAYED_0")][0]["name"]:
                            return True
                else:
                    return False

        elif card_issued["subtype"] == "Energy":
            if _to == "POKEMON_P_0":
                if Board.Board().BOARD_ELEM[Board.Board().BOARD_DIC.index(_to)][bench_id] == []:
                    return False
                else:
                    return True
    else:
        return False


def check_basic_in_hand():
    hand_list = Board.Board().BOARD_ELEM[Board.Board().BOARD_DIC.index("HAND_0")]
    for i in range(len(hand_list)):
        if hand_list[i]["supertype"] == "Pok\u00E9mon":
            if hand_list[i]["subtype"] == "Basic":
                return True
    return False


def check_retreatable():
    parsed_arr = parse_energy(0)
    if check_benched_pokemon_exist():
        if parsed_arr[0] >= len(Board.Board().BOARD_ELEM[Board.Board().BOARD_DIC.index("POKEMON_P_0")][0][-1]["retreatCost"]):
            return True
        elif "FREE_RETREAT_FLAG" in Board.Board().BOARD_ELEM[Board.Board().BOARD_DIC.index("POKEMON_SC_0")][0]:
            return True
    else:
        return False


def check_moveusable(bench_id: int, move_no: int): # move_no は、0,1,2...。
    pokemon_issued = get_pokemon_on_board_dict(bench_id)
    if "CANNOT_USE_MOVE_1" in Board.Board().BOARD_ELEM[Board.Board().BOARD_DIC.index("POKEMON_SC_0")][bench_id]:
        if move_no == Board.Board().BOARD_ELEM[Board.Board().BOARD_DIC.index("POKEMON_SC_0")][bench_id]["CANNOT_USE_MOVE_1"]:
            return False
    if "CANNOT_USE_MOVE_0" in Board.Board().BOARD_ELEM[Board.Board().BOARD_DIC.index("POKEMON_SC_0")][bench_id]:
        if move_no == Board.Board().BOARD_ELEM[Board.Board().BOARD_DIC.index("POKEMON_SC_0")][bench_id]["CANNOT_USE_MOVE_0"]:
            return False
    if "attacks" in pokemon_issued:
        if len(pokemon_issued["attacks"]) > move_no:
            parsed_arr = parse_energy(0)
            move_issued = pokemon_issued["attacks"][move_no]
            num_energy_needed = move_issued["convertedEnergyCost"]
            if num_energy_needed <= sum(parsed_arr[1]):
                for i in range(num_energy_needed):
                    if move_issued["cost"][i] == "Colorless":
                        return True
                    elif move_issued["cost"][i] in parsed_arr[0]:
                        parsed_arr[0].pop(parsed_arr[0].index(move_issued["cost"][i]))
                    elif "all" in parsed_arr[0]:
                        parsed_arr[0].pop(parsed_arr[0].index("all"))
                    else:
                        return False
    else:
        return False


def parse_energy(bench_id: int):
    energy_array = Board.Board().BOARD_ELEM[Board.Board().BOARD_DIC.index("POKEMON_E_0")][bench_id]
    energy_elem_name_list = []
    parsed_arr = []
    regexp_pattern_1 = re.compile(r'\sEnergy$')
    regexp_pattern_2 = re.compile(r'^Basic\s')
    for i in range(len(energy_array)):
        if energy_array[i]["subtype"] == "Basic":
            cardname = energy_array[i]["name"]
            type = re.sub(regexp_pattern_1, "", cardname)
            type = re.sub(regexp_pattern_2, "", type)
            parsed_arr.append(type)
            energy_elem_name_list.append(energy_array[i]["name"])
        elif energy_array[i]["subtype"] == "Special":
            if energy_array[i]["name"] == "Double Colorless Energy":
                energy_elem_name_list.append(energy_array[i]["name"])
                energy_elem_name_list.append(energy_array[i]["name"])
                parsed_arr.append("Colorless")
                parsed_arr.append("Colorless")
            if energy_array[i]["name"] == "Rainbow Energy":
                energy_elem_name_list.append(energy_array[i]["name"])
                parsed_arr.append("all")
            if energy_array[i]["name"] == "Herbal Energy":
                energy_elem_name_list.append(energy_array[i]["name"])
                parsed_arr.append("Grass")
            if energy_array[i]["name"] == "Strong Energy":
                energy_elem_name_list.append(energy_array[i]["name"])
                parsed_arr.append("Fighting")
            if energy_array[i]["name"] == "Mystery Energy":
                energy_elem_name_list.append(energy_array[i]["name"])
                parsed_arr.append("Psychic")
            if energy_array[i]["name"] == "Shield Energy":
                energy_elem_name_list.append(energy_array[i]["name"])
                parsed_arr.append("Metal")
            if energy_array[i]["name"] == "Wonder Energy":
                energy_elem_name_list.append(energy_array[i]["name"])
                parsed_arr.append("Fairy")
            if energy_array[i]["name"] == "Double Aqua Energy":
                energy_elem_name_list.append(energy_array[i]["name"])
                energy_elem_name_list.append(energy_array[i]["name"])
                parsed_arr.append("Water")
                parsed_arr.append("Water")
            if energy_array[i]["name"] == "Double Magma Energy":
                energy_elem_name_list.append(energy_array[i]["name"])
                energy_elem_name_list.append(energy_array[i]["name"])
                parsed_arr.append("Fighting")
                parsed_arr.append("Fighting")
            if energy_array[i]["name"] == "Double Dragon Energy":
                energy_elem_name_list.append(energy_array[i]["name"])
                energy_elem_name_list.append(energy_array[i]["name"])
                parsed_arr.append("all")
                parsed_arr.append("all")
            if energy_array[i]["name"] == "Flash Energy":
                energy_elem_name_list.append(energy_array[i]["name"])
                parsed_arr.append("Lightning")
            if energy_array[i]["name"] == "Dangerous Energy":
                energy_elem_name_list.append(energy_array[i]["name"])
                parsed_arr.append("Darkness")
            if energy_array[i]["name"] == "Burning Energy":
                energy_elem_name_list.append(energy_array[i]["name"])
                parsed_arr.append("Fire")
            if energy_array[i]["name"] == "Splash Energy":
                energy_elem_name_list.append(energy_array[i]["name"])
                parsed_arr.append("Water")
            if energy_array[i]["name"] == "Warp Energy":
                energy_elem_name_list.append(energy_array[i]["name"])
                parsed_arr.append("Colorless")
            if energy_array[i]["name"] == "Counter Energy":
                if len(Board.Board().BOARD_ELEM[Board.Board().BOARD_DIC.index("PRIZE_0")]) > len(Board.Board().BOARD_ELEM[Board.Board().BOARD_DIC.index("PRIZE_0")]):
                    energy_elem_name_list.append(energy_array[i]["name"])
                    energy_elem_name_list.append(energy_array[i]["name"])
                    parsed_arr.append("all")
                    parsed_arr.append("all")
                else:
                    energy_elem_name_list.append(energy_array[i]["name"])
                    parsed_arr.append("Colorless")
        elif energy_array[i]["name"] == "Electrode":
            energy_elem_name_list.append(energy_array[i]["name"])
            energy_elem_name_list.append(energy_array[i]["name"])
            parsed_arr.append("Lightning")
            parsed_arr.append("Lightning")

    return [parsed_arr, energy_elem_name_list]


def parse_basic_energy(bench_id: int):
    energy_array = Board.Board().BOARD_ELEM[Board.Board().BOARD_DIC.index("POKEMON_E_0")][bench_id]
    energy_elem_name_list = []
    parsed_arr = []
    regexp_pattern_1 = re.compile(r'\sEnergy$')
    regexp_pattern_2 = re.compile(r'^Basic\s')
    for i in range(len(energy_array)):
        if energy_array[i]["subtype"] == "Basic":
            cardname = energy_array[i]["name"]
            type = re.sub(regexp_pattern_1, "", cardname)
            type = re.sub(regexp_pattern_2, "", type)
            parsed_arr.append(type)
            energy_elem_name_list.append(energy_array[i]["name"])
        else:
            pass
    return [parsed_arr, energy_elem_name_list]

def check_benched_pokemon_exist():
    exist = 0
    for i in range(1, len(Board.Board().BOARD_ELEM[Board.Board().BOARD_DIC.index("POKEMON_P_0")])):
        if Board.Board().BOARD_ELEM[Board.Board().BOARD_DIC.index("POKEMON_P_0")][i] != []:
            exist = exist +1
    if exist == 0:
        return False
    else:
        return True


def get_pokemon_on_board_dict(bench_id: int):
    pokemon_issued = Board.Board().BOARD_ELEM[Board.Board().BOARD_DIC.index("POKEMON_P_0")][bench_id][-1]
    return pokemon_issued


def calc_my_all_pokemons_max_hp():
    max_hp_list = []
    for i in range(8):
        if len(Board.Board().BOARD_ELEM[Board.Board().BOARD_DIC.index("POKEMON_P_0")][i]) == 0:
            max_hp_list.append(0)
        else:
            if "MAX_HP_CHANGED" in Board.Board().BOARD_ELEM[Board.Board().BOARD_DIC.index("POKEMON_SC_0")][i]:
                max_hp = int(Board.Board().BOARD_ELEM[Board.Board().BOARD_DIC.index("POKEMON_P_0")][i][-1]["hp"]) + Board.Board().BOARD_ELEM[Board.Board().BOARD_DIC.index("POKEMON_SC_0")][i]["MAX_HP_CHANGED"]
                max_hp_list.append(max_hp)
            else:
                max_hp_list.append(int(Board.Board().BOARD_ELEM[Board.Board().BOARD_DIC.index("POKEMON_P_0")][i][-1]["hp"]))
    return max_hp_list


def calc_opponents_all_pokemons_max_hp():
    max_hp_list = []
    for i in range(8):
        if len(Board.Board().BOARD_ELEM[Board.Board().BOARD_DIC.index("POKEMON_P_1")][i]) == 0:
            max_hp_list.append(0)
        else:
            if "MAX_HP_CHANGED" in Board.Board().BOARD_ELEM[Board.Board().BOARD_DIC.index("POKEMON_SC_1")][i]:
                max_hp = int(Board.Board().BOARD_ELEM[Board.Board().BOARD_DIC.index("POKEMON_P_1")][i][-1]["hp"]) + Board.Board().BOARD_ELEM[Board.Board().BOARD_DIC.index("POKEMON_SC_1")][i]["MAX_HP_CHANGED"]
                max_hp_list.append(max_hp)
            else:
                max_hp_list.append(int(Board.Board().BOARD_ELEM[Board.Board().BOARD_DIC.index("POKEMON_P_1")][i][-1]["hp"]))
    return max_hp_list







