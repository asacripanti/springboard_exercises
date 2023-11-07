"""Auth app"""

from flask import Flask, render_template, request, redirect, session
from flask_sqlalchemy import SQLAlchemy
from models import User, connect_db, db, Feedback
from forms import RegisterForm, LoginForm, FeedbackForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///reviews'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

connect_db(app)

with app.app_context():
    db.create_all()



@app.route('/')
def home():
    """Home page for register"""

    return redirect("/register")

@app.route('/register', methods=['GET', 'POST'])
def register():
    """Register a user"""

    if "username" in session:
        return redirect(f"/users/{session['username']}")

    form =  RegisterForm()

    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        email = form.email.data
        first_name = form.first_name.data
        last_name = form.last_name.data

        user = User.register(username, password, email, first_name, last_name)

        db.session.commit()
        session['username'] = user.username

        return redirect(f"/users/{user.username}")

    else:
        return render_template("register.html", form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    """User login"""

    form = LoginForm()     

    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data

        user = User.authenticate(username, password)   
        if user:
            session['username'] = user.username
            return redirect(f"/users/{user.username}")

        else:
            form.username.errors = ["Invalid login info"]
            return render_template("register.html", form=form)    

    return render_template("login.html", form=form)        


@app.route('/users/<username>')
def secrets_route(username):
    """The secret route"""

    user = User.query.get(username)

    return render_template("secrets.html", user=user)


@app.route("/logout")
def logout():
    """Logout user"""

    session.pop("username")
    return redirect("/login")

@app.route("/users/<username>/delete", methods=['POST']) 
def delete_user(username):
    """Delete User"""

    # PRINT USERNAME

    user = User.query.get(username)
    db.session.delete(user)
    db.session.commit()
    session.pop("username")

    return redirect("/login")   


@app.route("/users/<username>/feedback/add", methods=['GET', 'POST'])   
def feedback_new(username):
    """Add feedback form"""

    print(f"Username: {username}")

    form = FeedbackForm()

    if form.validate_on_submit():
        title = form.title.data
        content = form.content.data

        feedback = Feedback(
            title=title,
            content=content,
            username=username
        )

        print(feedback) 

        db.session.add(feedback)
        db.session.commit()

        print(feedback.username)

        return redirect(f"/users/{feedback.username}")

    else:
        return render_template("feedback_new.html", form=form)

if __name__ == '__main__':
    app.run(debug=True)







