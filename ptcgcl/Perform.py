import json
import re
from . import Board_changer
from . import Import_cards
from . import Check
import random
import traceback


def draw(num=1):
    for i in range(num):
        if Board_changer.Board_CL().board_elem[Board_changer.Board_CL().board_dic.index("DECK_0")] == []:
            print("No more card in your deck!")
            return False
        else:
            Board_changer.Board_CL().board_elem[Board_changer.Board_CL().board_dic.index("HAND_0")].append(
                Board_changer.Board_CL().board_elem[Board_changer.Board_CL().board_dic.index("DECK_0")][0])
            Board_changer.Board_CL().board_elem[Board_changer.Board_CL().board_dic.index("DECK_0")].pop(0)
    return True


def opponent_draw(num=1):
    for i in range(num):
        if Board_changer.Board_CL().board_elem[Board_changer.Board_CL().board_dic.index("DECK_1")] == []:
            print("No more card in your deck!")
            return False
        else:
            Board_changer.Board_CL().board_elem[Board_changer.Board_CL().board_dic.index("HAND_1")].append(
                Board_changer.Board_CL().board_elem[Board_changer.Board_CL().board_dic.index("DECK_1")][0])
            Board_changer.Board_CL().board_elem[Board_changer.Board_CL().board_dic.index("DECK_1")].pop(0)
    return True


def shuffle_hand_into_deck():
    for i in range(len(Board_changer.Board_CL().board_elem[Board_changer.Board_CL().board_dic.index("HAND_0")])):
        Board_changer.Board_CL().board_elem[Board_changer.Board_CL().board_dic.index("DECK_0")].append(
            Board_changer.Board_CL().board_elem[Board_changer.Board_CL().board_dic.index("HAND_0")][i])
    Board_changer.Board_CL().board_elem[Board_changer.Board_CL().board_dic.index("HAND_0")] = []
    random.shuffle(Board_changer.Board_CL().board_elem[Board_changer.Board_CL().board_dic.index("DECK_0")])
    return 0


def opponent_shuffle_hand_into_deck():
    for i in range(len(Board_changer.Board_CL().board_elem[Board_changer.Board_CL().board_dic.index("HAND_1")])):
        Board_changer.Board_CL().board_elem[Board_changer.Board_CL().board_dic.index("DECK_1")].append(
            Board_changer.Board_CL().board_elem[Board_changer.Board_CL().board_dic.index("HAND_1")][i])
    Board_changer.Board_CL().board_elem[Board_changer.Board_CL().board_dic.index("HAND_1")] = []
    random.shuffle(Board_changer.Board_CL().board_elem[Board_changer.Board_CL().board_dic.index("DECK_1")])
    return 0


def shuffle_deck():
    random.shuffle(Board_changer.Board_CL().board_elem[Board_changer.Board_CL().board_dic.index("DECK_0")])
    return 0


def opponent_shuffle_deck():
    random.shuffle(Board_changer.Board_CL().board_elem[Board_changer.Board_CL().board_dic.index("DECK_1")])
    return 0


def mulligan():
    shuffle_hand_into_deck()
    for i in range(7):
        draw()


def put_prize():
    for i in range(6):
        Board_changer.Board_CL().board_elem[Board_changer.Board_CL().board_dic.index("PRIZE_0")].append(Board_changer.Board_CL().board_elem[Board_changer.Board_CL().board_dic.index("DECK_0")][0])
        Board_changer.Board_CL().board_elem[Board_changer.Board_CL().board_dic.index("DECK_0")].pop(0)
    return 0


def check_top(player=0, num=1):
    for i in range(num):
        print(Board_changer.Board_CL().board_elem[Board_changer.Board_CL().board_dic.index("DECK_" + str(player))][i])


def attach_energy(_from: str, card_no: int, bench_id: int):
    if Board_changer.Board_CL().board_elem[Board_changer.Board_CL().board_dic.index("POKEMON_P_0")][bench_id] != []:
        try:
            Board_changer.Board_CL().board_elem[Board_changer.Board_CL().board_dic.index("POKEMON_E_0")][bench_id].append(
                Board_changer.Board_CL().board_elem[Board_changer.Board_CL().board_dic.index(_from)][card_no])
            Board_changer.Board_CL().board_elem[Board_changer.Board_CL().board_dic.index(_from)].pop(card_no)
            return True
        except:
            traceback.print_exc()
            return False
    else:
        return False


def play_pokemon_from_hand(card_no: int, bench_id: int):
    if Check.check_playable(Board_changer.Board_CL().board_elem[Board_changer.Board_CL().board_dic.index("HAND_0")][card_no], "HAND_0",
                            "POKEMON_P_0", bench_id):
        try:
            Board_changer.Board_CL().board_elem[Board_changer.Board_CL().board_dic.index("POKEMON_P_0")][bench_id].append(
                Board_changer.Board_CL().board_elem[Board_changer.Board_CL().board_dic.index("HAND_0")][card_no])
            Board_changer.Board_CL().board_elem[Board_changer.Board_CL().board_dic.index("HAND_0")].pop(card_no)
            return True
        except:
            traceback.print_exc()
            return False
    else:
        return False


def attach_energy_from_hand(card_no: int, bench_id: int):
    if Check.check_playable(Board_changer.Board_CL().board_elem[Board_changer.Board_CL().board_dic.index("HAND_0")][card_no], "HAND_0",
                            "POKEMON_P_0", bench_id):
        if Board_changer.Board_CL().board_elem[Board_changer.Board_CL().board_dic.index("ENERGY_ATTACHED_0")] == []:
            try:
                Board_changer.Board_CL().board_elem[Board_changer.Board_CL().board_dic.index("POKEMON_E_0")][bench_id].append(
                    Board_changer.Board_CL().board_elem[Board_changer.Board_CL().board_dic.index("HAND_0")][card_no])
                Board_changer.Board_CL().board_elem[Board_changer.Board_CL().board_dic.index("HAND_0")].pop(card_no)
                Board_changer.Board_CL().board_elem[Board_changer.Board_CL().board_dic.index("ENERGY_ATTACHED_0")].append("Already Attached.")
                return True
            except:
                traceback.print_exc()
                return False
        else:
            print("You have already attached Energy this turn.")
        return True
    else:
        return False


def do_move(move_no: int):
    if Check.check_moveusable(move_no):
        if Board_changer.Board_CL().board_elem[Board_changer.Board_CL().board_dic.index("POKEMON_P_0")][0][-1]["attacks"][move_no]["text"]\
                == "":
            damage = Board_changer.Board_CL().board_elem[Board_changer.Board_CL().board_dic.index("POKEMON_P_0")][0][-1]["attacks"][move_no][
                "damage"]
            Board_changer.Board_CL().board_elem[Board_changer.Board_CL().board_dic.index("POKEMON_D_1")][0][0]\
                = Board_changer.Board_CL().board_elem[Board_changer.Board_CL().board_dic.index("POKEMON_D_1")][0][0] + damage
            return True
        else:
            # ここにテキストのある技の処理を書く
            return False
    else:
        return False


def count_hand():
    hand_count = len(Board_changer.Board_CL().board_elem[Board_changer.Board_CL().board_dic.index("HAND_0")])
    return hand_count


def count_opponents_hand():
    hand_count = len(Board_changer.Board_CL().board_elem[Board_changer.Board_CL().board_dic.index("HAND_1")])
    return hand_count


def count_my_pokemons_on_board():
    counter = 0
    for i in range(8):
        if len(Board_changer.Board_CL().board_elem[Board_changer.Board_CL().board_dic.index("POKEMON_P_0")][i]) == 0:
            pass
        else:
            counter = counter + 1
    return counter


def count_opponents_pokemons_on_board():
    counter = 0
    for i in range(8):
        if len(Board_changer.Board_CL().board_elem[Board_changer.Board_CL().board_dic.index("POKEMON_P_1")][i]) == 0:
            pass
        else:
            counter = counter + 1
    return counter


def return_pokemon_and_everything_attached(bench_id: int, _to: str):
    pokemon_count = len(Board_changer.Board_CL().board_elem[Board_changer.Board_CL().board_dic.index("POKEMON_P_0")][bench_id])
    energy_count = len(Board_changer.Board_CL().board_elem[Board_changer.Board_CL().board_dic.index("POKEMON_E_0")][bench_id])
    attachment_count = len(Board_changer.Board_CL().board_elem[Board_changer.Board_CL().board_dic.index("POKEMON_A_0")][bench_id])
    if pokemon_count == 0:
        return False
    else:
        for i in range(pokemon_count):
            Board_changer.Board_CL().board_elem[Board_changer.Board_CL().board_dic.index(_to)].append(
                Board_changer.Board_CL().board_elem[Board_changer.Board_CL().board_dic.index("POKEMON_P_0")][bench_id][i])
        for i in range(energy_count):
            Board_changer.Board_CL().board_elem[Board_changer.Board_CL().board_dic.index(_to)].append(
                Board_changer.Board_CL().board_elem[Board_changer.Board_CL().board_dic.index("POKEMON_E_0")][bench_id][i])
        for i in range(attachment_count):
            Board_changer.Board_CL().board_elem[Board_changer.Board_CL().board_dic.index(_to)].append(
                Board_changer.Board_CL().board_elem[Board_changer.Board_CL().board_dic.index("POKEMON_A_0")][bench_id][i])
        Board_changer.Board_CL().board_elem[Board_changer.Board_CL().board_dic.index("POKEMON_P_0")][bench_id] = []
        Board_changer.Board_CL().board_elem[Board_changer.Board_CL().board_dic.index("POKEMON_D_0")][bench_id] = []
        Board_changer.Board_CL().board_elem[Board_changer.Board_CL().board_dic.index("POKEMON_SC_0")][bench_id] = {}
        Board_changer.Board_CL().board_elem[Board_changer.Board_CL().board_dic.index("POKEMON_E_0")][bench_id] = []
        Board_changer.Board_CL().board_elem[Board_changer.Board_CL().board_dic.index("POKEMON_A_0")][bench_id] = []
        return True


def end_turn():
    for i in range(Board_changer.Board_CL().board_elem[Board_changer.Board_CL().board_dic.index("POKEMON_SC_0")]):
        Board_changer.Board_CL().board_elem[Board_changer.Board_CL().board_dic.index("POKEMON_SC_0")][i].pop("CANNOT_USE_MOVE_0", None)
        Board_changer.Board_CL().board_elem[Board_changer.Board_CL().board_dic.index("POKEMON_SC_0")][i].pop("CANNOT_USE_MOVE_1", None)

        # ターン変更処理
    if Board_changer.Board_CL().board_elem[Board_changer.Board_CL().board_dic.index("MY_TURN_0")] == [1]:
        Board_changer.Board_CL().board_elem[Board_changer.Board_CL().board_dic.index("MY_TURN_0")] = []
        Board_changer.Board_CL().board_elem[Board_changer.Board_CL().board_dic.index("WAS_MY_TURN_0")] = [1]
    elif Board_changer.Board_CL().board_elem[Board_changer.Board_CL().board_dic.index("MY_TURN_1")] == [1]:
        Board_changer.Board_CL().board_elem[Board_changer.Board_CL().board_dic.index("MY_TURN_1")] = []
        Board_changer.Board_CL().board_elem[Board_changer.Board_CL().board_dic.index("WAS_MY_TURN_1")] = [1]


def pokemon_check():

    # ここにポケモンチェックの内容を書く

    # どくチェック
    if "POISONED" in Board_changer.Board_CL().board_elem[Board_changer.Board_CL().board_dic.index("POKEMON_SC_0")][0]:
        Board_changer.Board_CL().board_elem[Board_changer.Board_CL().board_dic.index("POKEMON_D_0")][0][0]\
            = Board_changer.Board_CL().board_elem[Board_changer.Board_CL().board_dic.index("POKEMON_D_0")][0][0]\
              + (10 * Board_changer.Board_CL().board_elem[Board_changer.Board_CL().board_dic.index("POKEMON_SC_0")][0]["POISONED"])
        print("Your battle pokemon has taken damage for poison.")
    if "POISONED" in Board_changer.Board_CL().board_elem[Board_changer.Board_CL().board_dic.index("POKEMON_SC_1")][0]:
        Board_changer.Board_CL().board_elem[Board_changer.Board_CL().board_dic.index("POKEMON_D_1")][0][0]\
            = Board_changer.Board_CL().board_elem[Board_changer.Board_CL().board_dic.index("POKEMON_D_1")][0][0]\
              + (10 * Board_changer.Board_CL().board_elem[Board_changer.Board_CL().board_dic.index("POKEMON_SC_1")][0]["POISONED"])
        print("Opponent's battle pokemon has taken damage for poison.")
    # どくチェックおわり

    # ねむりチェック
    if "ASLEEP" in Board_changer.Board_CL().board_elem[Board_changer.Board_CL().board_dic.index("POKEMON_SC_0")][0]:
        if flip_coin():
            Board_changer.Board_CL().board_elem[Board_changer.Board_CL().board_dic.index("POKEMON_SC_0")][0].pop("ASLEEP")
            print("Now your pokemon is awake.")
    if "ASLEEP" in Board_changer.Board_CL().board_elem[Board_changer.Board_CL().board_dic.index("POKEMON_SC_1")][0]:
        if flip_coin():
            Board_changer.Board_CL().board_elem[Board_changer.Board_CL().board_dic.index("POKEMON_SC_1")][0].pop("ASLEEP")
            print("Now opponent's pokemon is awake.")
    # ねむりチェックおわり

    # まひチェック
    if "PARALYZED" in Board_changer.Board_CL().board_elem[Board_changer.Board_CL().board_dic.index("POKEMON_SC_0")][0]:
            Board_changer.Board_CL().board_elem[Board_changer.Board_CL().board_dic.index("POKEMON_SC_0")][0].pop("ASLEEP")
            print("Now your pokemon is refreshed from paralyzed..")
    # まひチェックおわり

    # BY_TURN_N のフラッグをデクリメントするコード。0のときは取り除く

    # ここから手番プレイヤー変更処理
    if Board_changer.Board_CL().board_elem[Board_changer.Board_CL().board_dic.index("WAS_MY_TURN_0")] == [1]:
        Board_changer.Board_CL().board_elem[Board_changer.Board_CL().board_dic.index("WAS_MY_TURN_0")] = []
        Board_changer.Board_CL().board_elem[Board_changer.Board_CL().board_dic.index("MY_TURN_1")] = [1]
    elif Board_changer.Board_CL().board_elem[Board_changer.Board_CL().board_dic.index("WAS_MY_TURN_1")] == [1]:
        Board_changer.Board_CL().board_elem[Board_changer.Board_CL().board_dic.index("WAS_MY_TURN_1")] = []
        Board_changer.Board_CL().board_elem[Board_changer.Board_CL().board_dic.index("MY_TURN_0")] = [1]


def ask_opp_move_id(bench_id):
    print("Opponent's move id (0, 1,.)")
    opp_move_id_input_int = int(input())
    return opp_move_id_input_int


def choose_my_pokemons_on_board(battle_bool: bool, pokemon_count: int):  # ポケモンが少ないと、戻り値がpokemon_count以下の個数の場合あり
    counter_1 = 0
    pokemon_ids_chosen_list = []
    pokemon_on_board_count = count_my_pokemons_on_board()
    if battle_bool:
        if pokemon_count > pokemon_on_board_count:
            pokemon_count = pokemon_on_board_count
    else:
        if pokemon_count > pokemon_on_board_count - 1:
            pokemon_count = pokemon_on_board_count

    while counter_1 < pokemon_count:
        bench_id = input()
        if len(Board_changer.Board_CL().board_elem[Board_changer.Board_CL().board_dic.index("POKEMON_P_0")][bench_id]) == 0:
            pass
        else:
            pokemon_ids_chosen_list.append(bench_id)
    return pokemon_ids_chosen_list


def choose_opponents_pokemons_on_board(battle_bool: bool, pokemon_count: int):  # ポケモンが少ないと、戻り値がpokemon_count以下の個数の場合あり
    counter_1 = 0
    pokemon_ids_chosen_list = []
    pokemon_on_board_count = count_opponents_pokemons_on_board()
    if battle_bool:
        if pokemon_count > pokemon_on_board_count:
            pokemon_count = pokemon_on_board_count
    else:
        if pokemon_count > pokemon_on_board_count - 1:
            pokemon_count = pokemon_on_board_count

    while counter_1 < pokemon_count:
        bench_id = input()
        if len(Board_changer.Board_CL().board_elem[Board_changer.Board_CL().board_dic.index("POKEMON_P_1")][bench_id]) == 0:
            pass
        else:
            pokemon_ids_chosen_list.append(bench_id)
    return pokemon_ids_chosen_list


def flip_coin():
    if random.random() < 0.5:
        print("Coin tails.")
        return False
    else:
        print("Coin heads.")
        return True



