
    
from flask import Flask, jsonify, request, render_template, session
from boggle import Boggle

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'

boggle_game = Boggle()

@app.route('/', methods=['GET', 'POST'])
def new_game():
    """Generate board"""
    if request.method == 'POST':
        # Handle the form submission here
        guess = request.form.get('word')
        board = session.get('board')

        if not board:
            return jsonify(result='error')

        result = boggle_game.check_valid_word(board, guess)
        return jsonify(result=result)

    else:
        board = boggle_game.make_board()
        session['board'] = board
        return render_template('base.html', board=board)


@app.route('/check_guess', methods=['GET', 'POST'])
def check_guess():
    """Check if guessed word is valid on board"""
    guess = request.json.get('word')
    board = session.get('board')

    if not board:
        return jsonify(result='error')

    # Implement the logic to check if the guess is a valid word on the board
    result = boggle_game.check_valid_word(board, guess)

    return jsonify(result=result)

@app.route('/update_score', methods=['POST'])
def update_score():
    """update high score and times played"""
    score = request.json.get('score')

    # Increment the number of times played and update highest score if needed
    times_played = session.get('times_played', 0) + 1
    highest_score = session.get('highest_score', 0)
    if score > highest_score:
        highest_score = score

    session['times_played'] = times_played
    session['highest_score'] = highest_score

    return jsonify(result='success')

@app.route('/get_times_played')
def get_times_played():
    """Retrieves number of times played"""
    times_played = session.get('times_played', 0)
    return jsonify(times_played=times_played)

@app.route('/get_highest_score')
def get_highest_score():
    """Retrieves highest score"""
    highest_score = session.get('highest_score', 0)
    return jsonify(highest_score=highest_score)



