import json
import codecs
import datetime
import re
import urllib.request
import urllib.parse
import requests
import os
import csv


def get_sets_from_web(regulation: str):
    if regulation == "Standard":  # 海外スタンダード
        params = {
            "standardLegal": "true"
        }
        p = urllib.parse.urlencode(params)
        url = "https://api.pokemontcg.io/v1/sets/?" + p
        # print(url)
        r = requests.get(url)
        sets_str = r.text
        sets_dict = json.loads(sets_str)

    elif regulation == "fromXY1":  # XY以降
        params ={
            "expandedLegal": "true"
        }
        p = urllib.parse.urlencode(params)
        url = "https://api.pokemontcg.io/v1/sets/?" + p
        # print(url)
        r = requests.get(url)
        sets_str = r.text
        sets_dict = json.loads(sets_str)
        sets_from_xy1_list = []
        for i in range(len(sets_dict["sets"])):
            datei_raw = sets_dict["sets"][i]["releaseDate"]
            datei_array = re.split("/", datei_raw)
            datei_value = datetime.date(int(datei_array[2]), int(datei_array[0]), int(datei_array[1]))
            datexy1_value = datetime.date(2014, 2, 5)
            if datei_value >= datexy1_value:
                # print("not skipped.")
                sets_from_xy1_list.append(sets_dict["sets"][i])
        # print(sets_from_xy1_list)
        sets_dict = {"sets": sets_from_xy1_list}

    elif regulation == "fromSM1":
        params ={
            "standardLegal": "true"
        }
        p = urllib.parse.urlencode(params)
        url = "https://api.pokemontcg.io/v1/sets/?" + p
        # print(url)
        r = requests.get(url)
        sets_str = r.text
        sets_dict = json.loads(sets_str)
        sets_from_sm1_list = []
        for i in range(len(sets_dict["sets"])):
            datei_raw = sets_dict["sets"][i]["releaseDate"]
            datei_array = re.split("/", datei_raw)
            datei_value = datetime.date(int(datei_array[2]), int(datei_array[0]), int(datei_array[1]))
            datexy1_value = datetime.date(2017, 1, 1)
            if datei_value >= datexy1_value:
                # print("not skipped.")
                sets_from_sm1_list.append(sets_dict["sets"][i])
        # print(sets_from_sm1_list)
        sets_dict = {"sets": sets_from_sm1_list}
    try:
        f = codecs.open("sets\u005C"+regulation+".json", "w", "utf-8")  # setsフォルダにキャッシュを保存
    except FileNotFoundError:
        os.mkdir("sets")
        f = codecs.open("sets\u005C" + regulation + ".json", "w", "utf-8")  # setsフォルダにキャッシュを保存
    json.dump(sets_dict, f, sort_keys=True, indent=4)
    return sets_dict


def save_card_jsons(regulation: str):
    sets_dic = get_sets_from_web(regulation)
    for i in range(len(sets_dic['sets'])):
        set_code = sets_dic['sets'][i]['code']
        # print("set_code=" + set_code)
        out_filename = set_code + ".json"
        params = {
            "setCode": set_code,
            "pageSize": 1000
        }
        p = urllib.parse.urlencode(params)
        url = "https://api.pokemontcg.io/v1/cards/?" + p
        # print(url)
        r = requests.get(url)
        cards_str = r.text
        # print(cards_str)
        cards_dict = json.loads(cards_str)
        try:
            f = codecs.open("cards\u005C"+out_filename, "w", "utf-8")  # cardsフォルダにキャッシュを保存
        except FileNotFoundError:
            os.mkdir("cards")
            f = codecs.open("cards\u005C"+out_filename, "w", "utf-8")  # cardsフォルダにキャッシュを保存

        json.dump(cards_dict, f, sort_keys=True, indent=4)
        # cards_all_list = cards_all_list + cards_dict["cards"]
    '''
    len_cards = len(cards_all_list)
    print(str(len_cards) + " cards imported.")
    cards_all_dict = {"cards": cards_all_list}
    # print(cards_all_dict)
    f = codecs.open("cards\u005CfromXY1all.json", "w", "utf-8")  # cardsフォルダにキャッシュを保存
    json.dump(cards_all_dict, f, sort_keys=True)
    '''


def import_all_cards(regulation: str):
    cards_all_list = []
    try:
        sets_list = json.load(open('sets\u005C' + regulation + '.json', 'r'))["sets"]
    except FileNotFoundError:
        sets_list = get_sets_from_web(regulation)["sets"]
        print("FileNotFoundError(sets)")

    for i in range(len(sets_list)):
        set_code_i = sets_list[i]["code"]
        try:
            set_cards_list = json.load(open('cards\u005C' + set_code_i + '.json', 'r'))["cards"]
        except FileNotFoundError:
            print("FileNotFoundError(cards)")
            save_card_jsons(regulation)
            set_cards_list = json.load(open('cards\u005C' + set_code_i + '.json', 'r'))["cards"]
        cards_all_list = cards_all_list + set_cards_list
#    print(cards_all_list)
    return cards_all_list


def create_moves_csv(regulation: str):
    cards_all_list = []
    try:
        sets_list = json.load(open('sets\u005C' + regulation + '.json', 'r'))["sets"]
    except FileNotFoundError:
        sets_list = get_sets_from_web(regulation)["sets"]
        print("FileNotFoundError(sets)")

    for i in range(len(sets_list)):
        set_code_i = sets_list[i]["code"]
        try:
            set_cards_list = json.load(open('cards\u005C' + set_code_i + '.json', 'r'))["cards"]
        except FileNotFoundError:
            print("FileNotFoundError(cards)")
            save_card_jsons(regulation)
            set_cards_list = json.load(open('cards\u005C' + set_code_i + '.json', 'r'))["cards"]
        cards_all_list = cards_all_list + set_cards_list
    print(len(cards_all_list))
    csv_list = [["id", "name", "attack_no", "attack_name", "damage", "text"]]
    for i in range(len(cards_all_list)):
        try:
            for j in range(len(cards_all_list[i]["attacks"])):
                if not cards_all_list[i]["attacks"][j]["text"] == "":
                    csv_list.append(
                        [cards_all_list[i]["id"], cards_all_list[i]["name"], j, cards_all_list[i]["attacks"][j]["name"],
                         cards_all_list[i]["attacks"][j]["damage"], cards_all_list[i]["attacks"][j]["text"]])
        except KeyError:
            pass
    try:
        with codecs.open("csv\u005C" + "move_sets.csv", "w", "utf-8") as f:  # cardsフォルダにキャッシュを保存
            writer = csv.writer(f, lineterminator='\n')  # 改行コード（\n）を指定しておく
            writer.writerows(csv_list)  # 2次元配列を書き込む
    except FileNotFoundError:
        os.mkdir("csv")
        with codecs.open("csv\u005C" + "move_sets.csv", "w", "utf-8") as f:  # cardsフォルダにキャッシュを保存
            writer = csv.writer(f, lineterminator='\n')  # 改行コード（\n）を指定しておく
            writer.writerows(csv_list)  # 2次元配列を書き込む


def create_sp_energy_csv(regulation: str):
    cards_all_list = []
    try:
        sets_list = json.load(open('sets\u005C' + regulation + '.json', 'r'))["sets"]
    except FileNotFoundError:
        sets_list = get_sets_from_web(regulation)["sets"]
        print("FileNotFoundError(sets)")

    for i in range(len(sets_list)):
        set_code_i = sets_list[i]["code"]
        try:
            set_cards_list = json.load(open('cards\u005C' + set_code_i + '.json', 'r'))["cards"]
        except FileNotFoundError:
            print("FileNotFoundError(cards)")
            save_card_jsons(regulation)
            set_cards_list = json.load(open('cards\u005C' + set_code_i + '.json', 'r'))["cards"]
        cards_all_list = cards_all_list + set_cards_list
    print(len(cards_all_list))
    csv_list = [["id", "name", "text"]]
    for i in range(len(cards_all_list)):
        try:
            if cards_all_list[i]["supertype"] == "Energy":
                if cards_all_list[i]["subtype"] == "Special":
                    csv_list.append(
                        [cards_all_list[i]["id"], cards_all_list[i]["name"]])
        except KeyError:
            pass
    try:
        with codecs.open("csv\u005C" + "spe_sets.csv", "w", "utf-8") as f:  # cardsフォルダにキャッシュを保存
            writer = csv.writer(f, lineterminator='\n')  # 改行コード（\n）を指定しておく
            writer.writerows(csv_list)  # 2次元配列を書き込む
    except FileNotFoundError:
        os.mkdir("csv")
        with codecs.open("csv\u005C" + "spe_sets.csv", "w", "utf-8") as f:  # cardsフォルダにキャッシュを保存
            writer = csv.writer(f, lineterminator='\n')  # 改行コード（\n）を指定しておく
            writer.writerows(csv_list)  # 2次元配列を書き込む


def get_basic_energies_json():
    out_filename = "basic_energies" + ".json"
    params = {
        "supertype": "energy",
        "subtype": "basic",
        "set": "generations"
    }
    p = urllib.parse.urlencode(params)
    url = "https://api.pokemontcg.io/v1/cards/?" + p
    # print(url)
    r = requests.get(url)
    cards_str = r.text
    # print(cards_str)
    cards_dict = json.loads(cards_str)
    try:
        f = codecs.open("cards\u005C" + out_filename, "w", "utf-8")  # cardsフォルダにキャッシュを保存
    except FileNotFoundError:
        os.mkdir("cards")
        f = codecs.open("cards\u005C" + out_filename, "w", "utf-8")  # cardsフォルダにキャッシュを保存

    json.dump(cards_dict, f, sort_keys=True, indent=4)

def save_card_jsons_sorted(regulation: str):
    sets_dic = get_sets_from_web(regulation)
    for i in range(len(sets_dic['sets'])):
        set_code = sets_dic['sets'][i]['code']
        # print("set_code=" + set_code)
        out_filename = set_code + "_sorted.json"
        params = {
            "setCode": set_code,
            "pageSize": 1000
        }
        p = urllib.parse.urlencode(params)
        url = "https://api.pokemontcg.io/v1/cards/?" + p
        # print(url)
        r = requests.get(url)
        cards_str = r.text
        # print(cards_str)
        cards_dict = json.loads(cards_str)
        cards_id_number_str_list = []
        for i in range(len(cards_dict["cards"])):
            setcode_with_minus = cards_dict["cards"][i]["setCode"] + "-"
            cards_id_number_str_list.append(cards_dict["cards"][i]["id"].replace(setcode_with_minus, ""))
        cards_dict_sorted = {"cards": []}

        for i in range(len(cards_id_number_str_list)):
            try:
                cards_id_number_str_list.index(str(i+1))
                cards_dict_sorted["cards"].append(cards_dict["cards"][cards_id_number_str_list.index(str(i+1))])
            except ValueError:
                print(setcode_with_minus+str(i+1)+" is not in list. Skipped.")
        try:
            f = codecs.open("cards\u005C"+out_filename, "w", "utf-8")  # cardsフォルダにキャッシュを保存
        except FileNotFoundError:
            os.mkdir("cards")
            f = codecs.open("cards\u005C"+out_filename, "w", "utf-8")  # cardsフォルダにキャッシュを保存

        json.dump(cards_dict_sorted, f, sort_keys=True, indent=4)
        # cards_all_list = cards_all_list + cards_dict["cards"]

