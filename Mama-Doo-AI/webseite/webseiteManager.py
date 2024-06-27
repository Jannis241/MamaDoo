from flask import Flask, render_template, request, redirect, url_for, flash
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'AI')))
import mainAI
import Essen

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Für Flash-Messages erforderlich

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
            if mainAI.MDA.checkIfZutatExists(food):
                foods_not_have.append(food)
            else:
                flash(f"Das Lebensmittel '{food}' existiert nicht.", 'danger')
    return render_template('add_food_not_have.html', foods_not_have=foods_not_have)

@app.route('/add-food-have', methods=['GET', 'POST'])
def add_food_have():
    if request.method == 'POST':
        food = request.form['food']
        if food and food not in foods_have:
            if mainAI.MDA.checkIfZutatExists(food):
                foods_have.append(food)
            else:
                flash(f"Das Lebensmittel '{food}' existiert nicht.", 'danger')
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
    global foods_have, foods_not_have, results
    mainAI.MDA.setUserInfo(foods_have, foods_not_have)  # sending the info to the ai
    results = mainAI.MDA.evaluate()  # getting the response

    # Clear the lists after submission
    foods_have = []
    foods_not_have = []

    # Store results in session for access on the confirmation page
    # session['results'] = results

    return redirect(url_for('confirmation'))

@app.route('/confirmation')
def confirmation():
    for gericht in results:
        name = gericht.name
        bewertung = gericht.rating
        sättigung = gericht.satt
        schwierigkeit = gericht.difficulty
        zutatenString = ""
        for zutat in gericht.zutaten:
            zutatenString += zutat.name +", "
        zutaten = zutatenString
        wann = gericht.wann
        thermomix = gericht.thermomix
        mama = gericht.mamaBenötigt
        extraInfo = gericht.extraInfo


    return render_template('submit.html')

def startApp():
    app.run(debug=True)

if __name__ == '__main__':
    app.run(debug=True)
