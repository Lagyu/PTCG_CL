import json
import codecs
import datetime
import re
import urllib.request, urllib.parse
import requests
import numpy


def get_sets_from_web(regulation: str):
    if regulation == "Standard":  # 海外スタンダード
        params = {
            "standardLegal": "true"
        }
        p = urllib.parse.urlencode(params)
        url = "https://api.pokemontcg.io/v1/sets/?" + p
        print(url)
        r = requests.get(url)
        sets_str = r.text
        sets_dict = json.loads(sets_str)

    elif regulation == "fromXY1":  # XY以降
        params ={
            "expandedLegal": "true"
        }
        p = urllib.parse.urlencode(params)
        url = "https://api.pokemontcg.io/v1/sets/?" + p
        print(url)
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
        print(url)
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
    f = codecs.open("sets\u005C"+regulation+".json", "w", "utf-8")
    json.dump(sets_dict, f, sort_keys=True, indent=4)
    return sets_dict


def import_cards(regulation: str):
    sets_dic = get_sets_from_web(regulation)
    for i in range(len(sets_dic['sets'])):
        set_code = sets_dic['sets'][i]['code']
        print("set_code=" + set_code)
        out_filename = set_code + ".json"
        params = {
            "setCode": set_code,
            "pageSize": 1000
        }
        p = urllib.parse.urlencode(params)
        url = "https://api.pokemontcg.io/v1/cards/?" + p
        print(url)
        r = requests.get(url)
        cards_str = r.text
        print(cards_str)
        cards_dict = json.loads(cards_str)
        f = codecs.open("cards\u005C"+out_filename, "w", "utf-8")
        json.dump(cards_dict, f, sort_keys=True, indent=4)


import_cards("fromXY1")


def construct_cardlist():
    print("test")
