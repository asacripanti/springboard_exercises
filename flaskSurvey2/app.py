from flask import Flask, render_template, redirect, url_for, session, request, flash
from flask_debugtoolbar import DebugToolbarExtension
from surveys import satisfaction_survey as survey

app = Flask(__name__)
app.config['SECRET_KEY'] = 'key'
toolbar = DebugToolbarExtension(app)

responses = []

@app.route("/")
def survey_start():
    """Select a survey."""
    return render_template("base.html", survey=survey)

@app.route("/begin", methods=["POST"])
def start_survey():
    """Clear the session of responses."""

    session['responses'] = []

    return redirect("/questions/0")

@app.route("/questions/<int:question_num>", methods=["GET", "POST"])
def question(question_num):
    """Display and handle the questions of the survey."""

    if "responses" not in session:
        session["responses"] = []

    if len(session["responses"]) == len(survey.questions):
        # If all questions are answered, redirect to thank you page
        return redirect(url_for("thank_you"))

    if len(session["responses"]) != question_num:
        # If user tries to access a question out of order, redirect to the correct URL
        flash("You're trying to access an invalid question.")
        return redirect(url_for("question", question_num=len(session["responses"])))

    current_question = survey.questions[question_num]

    if request.method == "POST":
        choice = request.form.get("choice")
        responses = session.get('responses', [])
        responses.append(choice)
        session['responses'] = responses

        # Redirect to the next question if available, otherwise, thank you page
        if question_num + 1 < len(survey.questions):
            return redirect(url_for("question", question_num=question_num + 1))
        else:
            return redirect(url_for("thank_you"))

    return render_template("questions.html", survey=survey, question_num=question_num, current_question=current_question)

@app.route("/thank-you")
def thank_you():
    """Show a thank you page after completing the survey."""
    return "Thank you for completing the survey!"
    
   