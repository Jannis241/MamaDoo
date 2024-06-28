
try:
    from flask import Flask, render_template, request, redirect, url_for, flash
except:
    print("Required module 'Flask' is missing..")
    exit(-1)

try:
    import sys
    import os

    sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'AI')))
    import mainAI
except:
    print("Import error..")
    exit(-1)

app = Flask(__name__, static_folder='static')
app.secret_key = "secret"
foods_have = []
foods_not_have = []
results = []

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
    global results
    
    # Erfasse die Checkbox-Werte
    mamaBenötigt = request.form.get('mamaBenötigt') == 'true'
    sortiereNachSchwierigkeit = request.form.get('sortiereNachSchwierigkeit') == 'true'
    print("-------")
    print()
    print(f"Set User Info of MDA --- essen was verbraucht werden soll: {foods_have} -- essen welches nicht vorhanden ist: {foods_not_have}")
    print()
    print("MDA FILTER: ")
    print("Mama benötigt: ", mamaBenötigt)
    print("Nach schwierigkeit sortiert: ", sortiereNachSchwierigkeit)
    print("-------")
    mainAI.MDA.setUserInfo(foods_have, foods_not_have)  # sending the info to the ai
    
    # Hier werden die Parameter an die evaluate-Funktion übergeben
    results = mainAI.MDA.evaluate(sortiereNachSchwierigkeit, mamaBenötigt)
    
    # Clear the lists after submission

    return redirect(url_for('confirmation'))

@app.route('/confirmation')
def confirmation():
    return render_template('submit.html', results=results)

@app.route('/reset-and-home')
def reset_and_home():
    print("RE-INITIALIZE EVERYTHING.....")
    global foods_have, foods_not_have
    foods_have = []
    foods_not_have = []
    mainAI.MDA.reinit()
    return redirect(url_for('home'))

def start():
    app.run(debug=True, host='0.0.0.0')

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
