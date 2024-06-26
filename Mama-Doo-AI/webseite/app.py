from flask import Flask, render_template, request, redirect, url_for

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

@app.route('/submit', methods=['POST'])
def submit():
    # Hier könntest du die eingegebenen Daten verarbeiten oder speichern
    return redirect(url_for('confirmation'))

@app.route('/confirmation')
def confirmation():
    return render_template('submit.html')

if __name__ == '__main__':
    app.run(debug=True)
