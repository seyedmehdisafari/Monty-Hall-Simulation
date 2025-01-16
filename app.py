from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

# Monty Hall Game Logic
def monty_hall_game(switch_doors: bool):
    doors = ['car'] + ['goat'] * 2
    random.shuffle(doors)
    initial_choice = random.choice([0, 1, 2])
    doors_revealed = [i for i in range(3) if i != initial_choice and doors[i] == 'goat']
    door_revealed = random.choice(doors_revealed)
    if switch_doors:
        final_choice = [i for i in range(3) if i != initial_choice and i != door_revealed][0]
    else:
        final_choice = initial_choice
    return {'final_choice': final_choice, 'result': doors[final_choice], 'door_revealed': door_revealed}

# Route for the main page
@app.route('/')
def index():
    return render_template('template.html')

# Route for playing the game
@app.route('/play', methods=['POST'])
def play():
    data = request.get_json()
    switch = data.get('switch', False)
    result = monty_hall_game(switch)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)