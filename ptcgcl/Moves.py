from . import Board_changer
from . import Perform
from . import Check



def torment():
    move_id = Perform.ask_opp_move_id(0)
    if "CANNOT_USE_MOVE_0" in Board_changer.Board_CL().board_elem[Board_changer.Board_CL().board_dic.index("POKEMON_SC_1")][0]:
        Board_changer.Board_CL().board_elem[Board_changer.Board_CL().board_dic.index("POKEMON_SC_1")][0]["CANNOT_USE_MOVE_1"] = move_id
    else:
        Board_changer.Board_CL().board_elem[Board_changer.Board_CL().board_dic.index("POKEMON_SC_1")][0]["CANNOT_USE_MOVE_0"] = move_id
    return True


def x_blast(move_id=100):
    if move_id == 100:
        move_id = Perform.ask_opp_move_id(0)
    if "CANNOT_USE_MOVE_0" in Board_changer.Board_CL().board_elem[Board_changer.Board_CL().board_dic.index("POKEMON_SC_0")][0]:
        Board_changer.Board_CL().board_elem[Board_changer.Board_CL().board_dic.index("POKEMON_SC_0")][0]["CANNOT_USE_MOVE_1"] = move_id
    else:
        Board_changer.Board_CL().board_elem[Board_changer.Board_CL().board_dic.index("POKEMON_SC_0")][0]["CANNOT_USE_MOVE_0"] = move_id
    return True


def put_damage_counter(no_str: str, damage_amount: int):
    if no_str == "all":
        for i in range(8):
            if len(Board_changer.Board_CL().board_elem[Board_changer.Board_CL().board_dic.index("POKEMON_P_1")][i]) == 0:
                pass
            else:
                Board_changer.Board_CL().board_elem[Board_changer.Board_CL().board_dic.index("POKEMON_D_1")][i][0] = \
                    Board_changer.Board_CL().board_elem[Board_changer.Board_CL().board_dic.index("POKEMON_D_1")][i][0] + damage_amount
    else:
        bench_id_list = Perform.choose_opponents_pokemons_on_board(True, int(no_str))
        for i in range(len(bench_id_list)):
            Board_changer.Board_CL().board_elem[Board_changer.Board_CL().board_dic.index("POKEMON_D_1")][bench_id_list[i]][0] = \
                Board_changer.Board_CL().board_elem[Board_changer.Board_CL().board_dic.index("POKEMON_D_1")][bench_id_list[i]][0] + damage_amount
    return True


def only_10_left(mine: bool, opponents: bool):
    if mine:
        my_max_hp_list = Check.calc_my_all_pokemons_max_hp()
        Board_changer.Board_CL().board_elem[Board_changer.Board_CL().board_dic.index("POKEMON_D_0")][0][0] = my_max_hp_list[0] - 10
    if opponents:
        opp_max_hp_list = Check.calc_opponents_all_pokemons_max_hp()
        Board_changer.Board_CL().board_elem[Board_changer.Board_CL().board_dic.index("POKEMON_D_1")][0][0] = opp_max_hp_list[0] - 10
    return True


def poisoned(nx_int=1):
    Board_changer.Board_CL().board_elem[Board_changer.Board_CL().board_dic.index("POKEMON_SC_1")][0]["POISONED"] = nx_int
    return True


def asleep(coin_int=1):
    Board_changer.Board_CL().board_elem[Board_changer.Board_CL().board_dic.index("POKEMON_SC_1")][0]["ASLEEP"] = coin_int
    return True


def paralized(coin=True):
    if coin:
        if Perform.flip_coin():
            Board_changer.Board_CL().board_elem[Board_changer.Board_CL().board_dic.index("POKEMON_SC_1")][0]["PARALYZED"] = 1
            return True
        else:
            return False



def heal_damage(bench_id: int, heal_amount: int):
    if Board_changer.Board_CL().board_elem[Board_changer.Board_CL().board_dic.index("POKEMON_D_0")][bench_id][0] < heal_amount:
        Board_changer.Board_CL().board_elem[Board_changer.Board_CL().board_dic.index("POKEMON_D_0")][bench_id][0] = 0
    else:
        Board_changer.Board_CL().board_elem[Board_changer.Board_CL().board_dic.index("POKEMON_D_0")][bench_id][0] = Board_changer.Board_CL().board_elem[Board_changer.Board_CL().board_dic.index("POKEMON_D_0")][bench_id][0] - 30
    return True


def deal_damage_to_opp_bench(no_str: str, damage_amount: int, battle_bool=False):
    if no_str == "all":
        if "BENCH_BARRIER" in Board_changer.Board_CL().board_elem[Board_changer.Board_CL().board_dic.index("BOARD_SC_1")][0]:
            Board_changer.Board_CL().board_elem[Board_changer.Board_CL().board_dic.index("POKEMON_D_1")][0][0] = \
                Board_changer.Board_CL().board_elem[Board_changer.Board_CL().board_dic.index("POKEMON_D_1")][0][0] + damage_amount
        else:
            for i in range(8):
                if len(Board_changer.Board_CL().board_elem[Board_changer.Board_CL().board_dic.index("POKEMON_P_1")][i]) == 0:
                    pass
                else:
                    Board_changer.Board_CL().board_elem[Board_changer.Board_CL().board_dic.index("POKEMON_D_1")][i][0] = \
                        Board_changer.Board_CL().board_elem[Board_changer.Board_CL().board_dic.index("POKEMON_D_1")][i][0] + damage_amount
    else:
        bench_id_list = Perform.choose_opponents_pokemons_on_board(battle_bool, int(no_str))
        if "BENCH_BARRIER" in Board_changer.Board_CL().board_elem[Board_changer.Board_CL().board_dic.index("BOARD_SC_1")][0]:
            for i in range(len(bench_id_list)):
                if bench_id_list[i] == 0:
                    Board_changer.Board_CL().board_elem[Board_changer.Board_CL().board_dic.index("POKEMON_D_1")][bench_id_list[i]][0] = \
                        Board_changer.Board_CL().board_elem[Board_changer.Board_CL().board_dic.index("POKEMON_D_1")][bench_id_list[i]][0] + damage_amount
        else:
            for i in range(len(bench_id_list)):
                Board_changer.Board_CL().board_elem[Board_changer.Board_CL().board_dic.index("POKEMON_D_1")][bench_id_list[i]][0] = \
                    Board_changer.Board_CL().board_elem[Board_changer.Board_CL().board_dic.index("POKEMON_D_1")][bench_id_list[i]][0] + damage_amount
    return True


def discard_my_battle_pokemons_energy(discard_energy_str_list: list):
    for i in len(discard_energy_str_list):
        parsed_result_list = Check.parse_energy(0)
        parsed_energy = parsed_result_list[0]
        energy_map = parsed_result_list[1]
        parsed_energy_i = parsed_energy
        energy_str_i = discard_energy_str_list[i]
        if energy_str_i in parsed_energy:
            message = "Choose from number following(" + str(i + 1) + "/" + str(len(discard_energy_str_list)) + ") :\n"
            j = 0
            while energy_str_i in parsed_energy_i:
                piyo = energy_map.pop(parsed_energy_i.index(energy_str_i))
                parsed_energy_i.pop(parsed_energy_i.index(energy_str_i))
                message = message + str(j) + ". " + piyo + "\n"
            chosen_id = input()
            name_discard = energy_map[energy_map.index(energy_str_i, chosen_id)]
            for k in range(Board_changer.Board_CL().board_elem[Board_changer.Board_CL().board_dic.index("POKEMON_E_0")][0]):
                if Board_changer.Board_CL().board_elem[Board_changer.Board_CL().board_dic.index("POKEMON_E_0")][0][k]["name"] == name_discard:
                    Board_changer.Board_CL().board_elem[Board_changer.Board_CL().board_dic.index("POKEMON_E_0")][0].pop(k)


def shuffle_opponents_hand(draw: int, as_it_was=False):
    if as_it_was:
        opp_hand_num = Perform.count_opponents_hand()
        draw = opp_hand_num
    Perform.opponent_shuffle_hand_into_deck()
    Perform.opponent_draw(draw)
    return True


def discard_my_battle_pokemons_all_energy(discard_energy_str="all"):
    if discard_energy_str == "all":
        Board_changer.Board_CL().board_elem[Board_changer.Board_CL().board_dic.index("POKEMON_E_0")][0] = []
    else:
        while (discard_energy_str in Check.parse_energy(0)[0]) or ("all" in Check.parse_energy(0)[0]):
            parsed_result_list = Check.parse_energy(0)
            parsed_energy = parsed_result_list[0]
            energy_map = parsed_result_list[1]
            parsed_energy_i = parsed_energy
            if discard_energy_str in parsed_energy:
                name_discard = energy_map[energy_map.index(parsed_energy[parsed_energy.index(discard_energy_str)])]
                for k in range(Board_changer.Board_CL().board_elem[Board_changer.Board_CL().board_dic.index("POKEMON_E_0")][0]):
                    if Board_changer.Board_CL().board_elem[Board_changer.Board_CL().board_dic.index("POKEMON_E_0")][0][k]["name"] == name_discard:
                        Board_changer.Board_CL().board_elem[Board_changer.Board_CL().board_dic.index("POKEMON_E_0")][0].pop(k)
            if "all" in parsed_energy:
                name_discard = energy_map[energy_map.index(parsed_energy[parsed_energy.index("all")])]
                for k in range(Board_changer.Board_CL().board_elem[Board_changer.Board_CL().board_dic.index("POKEMON_E_0")][0]):
                    if Board_changer.Board_CL().board_elem[Board_changer.Board_CL().board_dic.index("POKEMON_E_0")][0][k]["name"] == name_discard:
                        Board_changer.Board_CL().board_elem[Board_changer.Board_CL().board_dic.index("POKEMON_E_0")][0].pop(k)


def flip_coin_and_deal_more_damage_num(num=0):
    if Perform.flip_coin():
        Board_changer.Board_CL().board_elem[Board_changer.Board_CL().board_dic.index("POKEMON_D_1")][0][0] = \
            Board_changer.Board_CL().board_elem[Board_changer.Board_CL().board_dic.index("POKEMON_D_1")][0][0] + num


def mine():
    Perform.check_top(1, 1)
    if input("Have your opponent shuffle his or her deck?(True / False):"):
        Perform.opponent_shuffle_deck()
        return True
    else:
        return True




