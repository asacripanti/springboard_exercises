from flask import Flask, request

app = Flask(__name__)

@app.route('/welcome')
def say_welcome():
    ''''Return Welcome'''
    return 'welcome'

@app.route('/welcome/home')
def say_welcome_home():
    """Return Welcome Home"""
    return 'welcome home'

@app.route('/welcome/back')
def say_welcome_back():
    """Return welcome back"""
    return 'welcome back'