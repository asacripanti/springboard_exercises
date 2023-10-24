"""Blogly application."""

from flask import Flask, request, redirect, render_template, url_for
from models import db, connect_db, User, Post, Tag, PostTag
from flask_debugtoolbar import DebugToolbarExtension

# what does all this do?
app = Flask(__name__)
app.config['SECRET_KEY'] = 'myKey'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly_v2'
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
    return redirect(url_for('home_page'))


@app.route('/home')
def home_page():
    """Home page"""

    u = User
    p = Post
    t = Tag

    comments = (db.session.query(u.user_name, p.title, t.name, p.user_id, p.id, p.content)
    .join(p)
    .join(PostTag)
    .join(t)
    .all())

    return render_template('home.html', comments=comments)

    


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

    user_name = request.form['user_name']
    image_url = request.form['image_url']

    # Create a new User object and add it to the database session
    new_user = User(user_name=user_name, image_url=image_url)
    db.session.add(new_user)
    db.session.commit()

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
    user.user_name = request.form['user_name']
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

@app.route('/users/<int:user_id>/posts/<int:post_id>', methods=['GET'])
def post_view(user_id, post_id):
    """View post"""
    user = User.query.get_or_404(user_id)
    post = Post.query.get_or_404(post_id)
    return render_template('post_view.html', user=user, post=post)



@app.route('/posts/new', methods=['GET'])
def post_form():
    """View form to add post"""

    post = Post()
    return render_template('post_form.html', post=post)


@app.route('/users/<int:user_id>/posts/new', methods=['POST'])
def add_post(user_id):
    """Submit form to add post"""

    post = Post()

    post.title = request.form['title']
    post.content = request.form['content']
    post.user_id = user_id 

    user = User.query.get_or_404(user_id)

    tags = request.form['tags'].split(',')
    for tag_name in tags:
        tag_name = tag_name.strip()  # Remove leading/trailing whitespace
        if tag_name:
          # Check if the tag already exists
            existing_tag = Tag.query.filter_by(name=tag_name).first()
            if not existing_tag:
                # If the tag does not exist, create a new Tag object and add it to the tags table
                new_tag = Tag(name=tag_name)
                db.session.add(new_tag)
                existing_tag = new_tag  # Assign existing_tag to new_tag

            # Create a new PostTag relationship and add it to the session
            new_post_tag = PostTag(post=post, tag=existing_tag)
            db.session.add(new_post_tag)

    db.session.add(post)
    db.session.commit()

    return redirect("/users")

@app.route('/users/<int:user_id>/posts/<int:post_id>/edit', methods=['GET'])
def post_edit(user_id, post_id):
    """Form to edit post"""

    user = User.query.get_or_404(user_id)
    post = Post.query.get_or_404(post_id)

    return render_template('post_edit.html', user=user)


@app.route('/users/<int:user_id>/posts/<int:post_id>/edit', methods=['POST'])
def post_update(user_id, post_id):
    """Form submission of edit form"""

    user = User.query.get_or_404(user_id)
    post = Post.query.get_or_404(post_id)

    post.title = request.form['title']
    post.content = request.form['content']
    post.user_id = user_id 

    db.session.add(post)
    db.session.commit()

    return redirect("/users")

@app.route('/users/<int:user_id>/posts/<int:post_id>/delete', methods=['POST'])
def post_delete(user_id, post_id):
    """Delete post"""

    
    post = Post.query.get_or_404(post_id)

    db.session.delete(post)
    db.session.commit()

    return redirect("/users") 








    


