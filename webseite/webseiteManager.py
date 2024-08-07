import os

from flask import Flask, flash, redirect, render_template, request, url_for

from AI import Essen, mainAI

global foods_have, foods_not_have, mamaBenötigt, sortiereNachSchwierigkeit, sortedByRating, sortedByGesund, sortedBySatt

app = Flask(__name__, static_folder="static")
app.secret_key = "dsfjdsgjdfgsderfgeshe23425234563465345"
foods_have = []
foods_not_have = []
shopping_list = []

selected_gericht = None

file = open("webseite/einkaufsliste.txt")
lines = file.readlines()
for line in lines:
    shopping_list.append(line.strip())
file.close()

results = []


@app.route("/reset-foods-einkaufsliste", methods=["POST"])
def reset_foods_einkaufsliste():
    global shopping_list
    shopping_list = []
    file = open("webseite/einkaufsliste.txt", "w")
    file.write("")
    file.close()
    return render_template("Einkaufsliste.html", shopping_list=shopping_list)


@app.route("/reset-foods-not-have", methods=["POST"])
def reset_foods_not_have():
    global foods_not_have
    foods_not_have = []
    return redirect(url_for("add_food_not_have"))


@app.route("/reset-foods-have", methods=["POST"])
def reset_foods_have():
    global foods_have
    foods_have = []
    return redirect(url_for("add_food_have"))


@app.route("/reset-selected-gericht", methods=["POST"])
def reset_selected_gericht():
    global selected_gericht
    selected_gericht = None
    return redirect(url_for("home"))


@app.route("/", methods=["GET", "POST"])
def home():
    global selected_gericht

    print("selected Gericht: ", selected_gericht)
    return render_template("index.html", selected_gericht=selected_gericht)


@app.route("/add-food-not-have", methods=["GET", "POST"])
def add_food_not_have():
    global foods_not_have
    if request.method == "POST":
        food = request.form["food"]
        if food and food not in foods_not_have:
            if mainAI.MDA.checkIfZutatExists(food):
                foods_not_have.append(food)
            else:
                flash(f"Das Lebensmittel '{food}' existiert nicht.", "danger")
    return render_template("add_food_not_have.html", foods_not_have=foods_not_have)


@app.route("/add-food-have", methods=["GET", "POST"])
def add_food_have():
    global foods_have
    if request.method == "POST":
        food = request.form["food"]
        if food and food not in foods_have:
            if mainAI.MDA.checkIfZutatExists(food):
                foods_have.append(food)
            else:
                flash(f"Das Lebensmittel '{food}' existiert nicht.", "danger")
    return render_template("add_food_have.html", foods_have=foods_have)


@app.route("/remove-food-not-have", methods=["POST"])
def remove_food_not_have():
    food_to_remove = request.form["food"]
    if food_to_remove in foods_not_have:
        foods_not_have.remove(food_to_remove)
    return redirect(url_for("add_food_not_have"))


@app.route("/remove-food-have", methods=["POST"])
def remove_food_have():
    food_to_remove = request.form["food"]
    if food_to_remove in foods_have:
        foods_have.remove(food_to_remove)
    return redirect(url_for("add_food_have"))


@app.route("/submit", methods=["POST"])
def submit():
    global results, numOfLoswerdeGerichte

    # Erfasse die Checkbox-Werte
    mamaBenötigt = request.form.get("mamaBenötigt") == "true"
    sortiereNachSchwierigkeit = request.form.get("sortiereNachSchwierigkeit") == "true"
    sortedByRating = request.form.get("sortiereNachRating") == "true"
    sortedBySatt = request.form.get("sortiereNachSatt") == "true"
    sortedByGesund = request.form.get("sortiereNachGesund") == "true"
    mainAI.MDA.reinit()
    print("setting user info: ", foods_have, foods_not_have)
    mainAI.MDA.setUserInfo(foods_have, foods_not_have)  # sending the info to the ai

    # Hier werden die Parameter an die evaluate-Funktion übergeben
    results, numOfLoswerdeGerichte = mainAI.MDA.evaluate(sortiereNachSchwierigkeit, mamaBenötigt, sortedByRating, sortedByGesund, sortedBySatt)

    # Speichere die Back-URL, um zur vorherigen Seite zurückzukehren
    back_url = request.referrer
    return redirect(url_for("confirmation", back_url=back_url))


@app.route("/confirmation")
def confirmation():
    back_url = request.args.get("back_url", url_for("home"))
    return render_template("submit.html", results=results, numOfLoswerdeGerichte=numOfLoswerdeGerichte, back_url=back_url)


@app.route("/reset-and-home", methods=["GET", "POST"])
def reset_and_home():
    print()
    print()
    print("reset and home")
    global foods_have, foods_not_have, mamaBenötigt, sortiereNachSchwierigkeit, sortedByRating, sortedByGesund, sortedBySatt
    global selected_gericht

    foods_have = []
    foods_not_have = []
    mainAI.MDA.reinit()

    # Reset all filters
    mamaBenötigt = "false"
    sortiereNachSchwierigkeit = "false"
    sortedByRating = "false"
    sortedBySatt = "false"
    sortedByGesund = "false"

    if request.method == "POST":
        selected_gericht = request.form.get("selected_gericht", None)

    return redirect(url_for("home"))


@app.route("/shopping-list", methods=["GET", "POST"])
def show_shopping_list():
    if request.method == "POST":
        food = request.form["food"]
        if food and food not in shopping_list:
            shopping_list.append(food)
    return render_template("Einkaufsliste.html", shopping_list=shopping_list)


@app.route("/add-food-shopping-list", methods=["POST"])
def add_food_shopping_list():
    food = request.form["food"]
    if food and food not in shopping_list:
        with open("webseite/einkaufsliste.txt", "a") as file:
            file.write(food + "\n")
        shopping_list.append(food)
    return redirect(url_for("show_shopping_list"))


@app.route("/remove-food-shopping-list", methods=["POST"])
def remove_food_shopping_list():
    food_to_remove = request.form["food"]
    if food_to_remove in shopping_list:
        shopping_list.remove(food_to_remove)
        with open("webseite/einkaufsliste.txt", "w") as file:
            for food in shopping_list:
                file.write(food + "\n")
    return redirect(url_for("show_shopping_list"))


@app.route("/gericht/<string:name>")
def gericht_detail(name):
    gericht = Essen.get_gericht_by_name(name)
    return render_template("gericht_detail.html", gericht=gericht)


def start():
    app.run(debug=False, host="0.0.0.0")
