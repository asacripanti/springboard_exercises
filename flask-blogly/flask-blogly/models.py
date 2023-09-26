"""Models for Blogly."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    """User model for SQLAlchemy."""


    __tablename__ = 'users'


    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    image_url = db.Column(db.String(200), default='https://www.thehappycatsite.com/wp-content/uploads/2020/09/Orange-and-Black-Cat-long.jpg')  

    @property
    def full_name(self):
        """Return full name of user."""

        return f"{self.first_name} {self.last_name}"


def connect_db(app):
    """Connect database to provided Flask app"""

    db.app = app
    db.init_app(app)