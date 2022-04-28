"""Models for Blogly."""
import datetime
from email.policy import default
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)


class User(db.Model):
    """User"""

    __tablename__ = "Users"

    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)
    first_name = db.Column(db.String(25),
                     nullable=False,)
    last_name = db.Column(db.String(25),
                     nullable=False,)
    img_url - db.Column(
                    db.Text,
                    default = 'https://media.istockphoto.com/photos/barbary-macaque-picture-id824860820?k=20&m=824860820&s=612x612&w=0&h=W8783ZGcqMfDMJoXvBAyDFcSjnOWdKqKhgLGvf-VIuU='
    )
    
    posts = db.relationship('Post')
    
    
    def greet(self):
        """Greet using name."""

        return f"Hello {self.first_name}, how are you?"
    
    def full_name(self, units=10):
        """Nom nom nom."""

        return f"{self.first_name} {self.last_name}"

    def __repr__(self):
        """Show info about user."""

        p = self
        return f"<User id={p.id} | Name={p.first_name} {p.last_name} | Hunger Level={p.hunger}>"
    
    
    
    
class Post(db.Model):
    
    __tablename__ = "Posts"
    
    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)
    title = db.Column(db.String(25),
                     nullable=False,
                     UNIQUE = True)
    content = db.Column(db.Text,
                     nullable=False)
    time_created - db.Column(
                    db.TIMESTAMP, default = datetime.datetime.now())
    user_id = db.Column(
        db.Integer,
        db.ForeignKey('User.id'),
        nullable=False)
    
    def __repr__(self):
        """Show info about user."""

        p = self
        return f"<post id={p.id} | title={p.title} | User id = {p.user_id}>"
    
    