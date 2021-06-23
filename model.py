from db import db

class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    director = db.Column(db.String(80), nullable=False)
    genres = db.Column(db.Text)
    run_time = db.Column(db.Integer, nullable=False)
    poster = db.Column(db.Text, nullable=False)
    tags = db.Column(db.Text)
    link = db.Column(db.Text, nullable=False)