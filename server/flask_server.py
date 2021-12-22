from flask import Flask, render_template
import json
import os


def get_info(champion_name):
    data = {}
    with open("./server/static/dragontail-11.24.1/11.24.1/data/fr_FR/champion/" + champion_name + ".json",
              encoding='utf-8') \
            as f:
        data_in_file = json.load(f)
        data["name"] = data_in_file["data"][champion_name]["name"]
        data["title"] = data_in_file["data"][champion_name]["title"]
        data["lore"] = data_in_file["data"][champion_name]["lore"]
        data["skins"] = []
        for skin_info in data_in_file["data"][champion_name]["skins"]:
            data["skins"].append({
                "name": skin_info["name"],
                "file": champion_name + "_" + str(skin_info["num"]) + ".jpg"
            })
        data["spells"] = []
        for spell_info in data_in_file["data"][champion_name]["spells"]:
            tmp_struct = {
                "name": spell_info["name"],
                "description": spell_info["description"],
                "image": spell_info["image"]["full"]
            }
            data["spells"].append(tmp_struct)
        data["passive"] = {
            "name": data_in_file["data"][champion_name]["passive"]["name"],
            "description": data_in_file["data"][champion_name]["passive"]["description"],
            "image": data_in_file["data"][champion_name]["passive"]["image"]["full"]
        }
    return data


def get_champion_list():
    list_champ = []
    file_list = os.listdir("./server/static/dragontail-11.24.1/11.24.1/data/fr_FR/champion")
    for file in file_list:
        list_champ.append(file.split(".")[0])
    return list_champ


class FlaskServer:

    def __init__(self):
        self.app = Flask(__name__)

        list_champion = get_champion_list()
        data = {}
        for champion in list_champion:
            data[champion] = get_info(champion)

        @self.app.route("/champion/<champion_name>")
        def show_specific_champion(champion_name):
            return render_template("specific_champion.html",
                                   champion=champion_name,
                                   informations=data[champion_name])

        @self.app.route("/champions")
        def show_all_champions():
            return render_template("all_champions.html", list_champion=list_champion)

        @self.app.route("/")
        def home():
            return render_template("index.html")

    def run(self):
        self.app.run()

