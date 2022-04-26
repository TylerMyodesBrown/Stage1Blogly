"""Seed file to make sample data for pets db."""

from models import User, db
from app import app

# Create all tables
db.drop_all()
db.create_all()

# If table isn't empty, empty it
User.query.delete()

# Add pets
whiskey = User(first_name='Whiskey', last_name='Barrel')
bowser = User(first_name='Bowser', last_name='Mario', img_url='https://www.rd.com/wp-content/uploads/2019/09/GettyImages-621924830-scaled.jpg')
spike = User(first_name='Spike', last_name='Lash')

# Add new objects to session, so they'll persist
db.session.add(whiskey)
db.session.add(bowser)
db.session.add(spike)

# Commit--otherwise, this never gets saved!
db.session.commit()
