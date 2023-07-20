from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension
from stories import story

app = Flask(__name__)
app.debug = True
app.config['SECRET_KEY'] = 'secret_key'
debug = DebugToolbarExtension(app)

@app.route('/')
def ask_questions():
    '''Generate form'''
    prompts = story.prompts
    return render_template('questions.html', prompts=prompts)

@app.route('/story')
def show_story():
    """Show story result"""
    print(request.args)
    text = story.generate(request.args)
    return render_template('story.html', text=text)