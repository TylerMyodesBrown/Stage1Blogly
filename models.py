"""Models for Blogly."""

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

    @classmethod
    def get_by_species(cls, species):
        """Get all pets matching that species."""

        return cls.query.filter_by(species=species).all()

    @classmethod
    def get_all_hungry(cls):
        return cls.query.filter(Pet.hunger >= 20).all();