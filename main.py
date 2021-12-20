import os

from flask import Flask, render_template

def get_champion_list():
    list_champ = []
    file_list = os.listdir("./static/dragontail-11.24.1/11.24.1/data/fr_FR/champion")
    for file in file_list:
        list_champ.append(file.split(".")[0])
    return list_champ

def get_skin_list(champion_name):
    list_skin = []
    file_list = os.listdir("./static/dragontail-11.24.1/img/champion/splash")
    for file in file_list:
        if file.split("_")[0] == champion_name:
            list_skin.append(file)
    return list_skin


app = Flask(__name__)

list_champion = get_champion_list()


@app.route("/champion/<champion_name>")
def show_specific_champion(champion_name):
    return render_template("specific_champion.html",
                           champion=champion_name,
                           skins_list=get_skin_list(champion_name))


@app.route("/champions")
def show_all_champions():
    return render_template("all_champions.html", list_champion=list_champion)


@app.route("/")
def home():
    return render_template("index.html")


app.run()
