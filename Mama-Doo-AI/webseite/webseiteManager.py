from flask import Flask, render_template, request, redirect, url_for
import sys
import os


sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'AI')))
import mainAI
import Essen

app = Flask(__name__)

foods_have = []
foods_not_have = []

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/add-food-not-have', methods=['GET', 'POST'])
def add_food_not_have():
    if request.method == 'POST':
        food = request.form['food']
        if food and food not in foods_not_have:
            foods_not_have.append(food)
    return render_template('add_food_not_have.html', foods_not_have=foods_not_have)

@app.route('/add-food-have', methods=['GET', 'POST'])
def add_food_have():
    if request.method == 'POST':
        food = request.form['food']
        if food and food not in foods_have:
            foods_have.append(food)
    return render_template('add_food_have.html', foods_have=foods_have)

@app.route('/remove-food-not-have', methods=['POST'])
def remove_food_not_have():
    food_to_remove = request.form['food']
    if food_to_remove in foods_not_have:
        foods_not_have.remove(food_to_remove)
    return redirect(url_for('add_food_not_have'))

@app.route('/remove-food-have', methods=['POST'])
def remove_food_have():
    food_to_remove = request.form['food']
    if food_to_remove in foods_have:
        foods_have.remove(food_to_remove)
    return redirect(url_for('add_food_have'))

@app.route('/submit', methods=['POST'])
def submit():

    # The user has submitted their choices
    # Getting and setting all the data of the MDA
    print("Loswerden: ", foods_have)
    print("nicht Vorhanden: ", foods_not_have)
    mainAI.MDA.setUserInfo(foods_have, foods_not_have) # sending the info to the ai
    print("Setting user info to the MDA..")
    print()
    print("Getting evaluation..")
    results = mainAI.MDA.evaluate() # getting the respone
    print()
    print()
    print()
    print()
    print(f"Got {len(results)} responses from AI: ")
    print()
    print("----------------------------")

    for gericht in results:
        Essen.printGerichtStats(gericht)

    foods_have.clear()
    foods_not_have.clear()
    return redirect(url_for('confirmation'))

@app.route('/confirmation')
def confirmation():
    
    # hier müssten dann die results angezeigt werden
    # vielleicht hier steht dann so: erfolgreich 
    # und darunter zurück zur start seite und see results die dich dann auf eine neue webseite bringen
    # Evaluation muss noch gefixt werden
    # funktion dass er direkt sagt in der webseite falls er ein essen nicht findet
    # einkaufs wunschliste oben im menü als feature setzen (einfach) nur mit add und remove eigentlich genau das selbe nur dass es nicht resetet wird
    # alle Zutaten und Essen konfigurieren (schwierigkeit, zutaten, mama dabei usw)
    # komplette Ad ons, einfach vielleicht bei den Essen daten noch ein extra punkt "possible add ons" wo dann gesagt wird was das ist und wie viel es plus geben kann
    # alles umbenennen
    # filter ob mittags oder abends 
    # auf raspberry pi laufen lassen
    return render_template('submit.html')

def startApp():
    app.run(debug=True)
if __name__ == '__main__':
    app.run(debug=True)
