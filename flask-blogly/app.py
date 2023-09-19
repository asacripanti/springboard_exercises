"""Blogly application."""

from flask import Flask, request, redirect, render_template, url_for
from models import db, connect_db, User
from flask_debugtoolbar import DebugToolbarExtension

# what does all this do?
app = Flask(__name__)
app.config['SECRET_KEY'] = 'myKey'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

toolbar = DebugToolbarExtension(app)

connect_db(app)
# db.create_all()

with app.app_context():
    # Create the database tables
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)

@app.route('/')
def redirect_to_users():
    """Redirects to list of users."""
    return redirect(url_for('show_all_users'))
    


@app.route('/users')
def show_all_users():
    """Page with user info"""
    users = User.query.all()
    return render_template('users.html', users=users)


@app.route('/users/new', methods=['GET'])
def show_add_user_form():
    """New user form"""
    return render_template('add_user.html')


@app.route('/users/new', methods=['POST'])
def add_user():
    """Add new user"""
    return render_template('new_user.html')


@app.route('/users/<int:user_id>')
def users_show(user_id):
    """Specific user info"""

    user = User.query.get_or_404(user_id)
    return render_template('user_info.html', user=user)


@app.route('/users/<int:user_id>/edit', methods=['GET'])
def show_edit_user_form(user_id):
    """Form to edit user"""
    user = User.query.get_or_404(user_id)
    return render_template('edit_user.html', user=user)    


@app.route('/users/<int:user_id>/edit', methods=["POST"])
def users_update(user_id):
    """Handle form submission for updating an existing user"""

    user = User.query.get_or_404(user_id)
    user.first_name = request.form['first_name']
    user.last_name = request.form['last_name']
    user.image_url = request.form['image_url']

    db.session.add(user)
    db.session.commit()

    return redirect("/users")


@app.route('/users/<int:user_id>/delete', methods=["POST"])
def users_destroy(user_id):
    """Handle form submission for deleting an existing user"""

    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()

    return redirect("/users")


    


