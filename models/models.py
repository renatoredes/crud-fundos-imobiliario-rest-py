# models/models.py
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Ticker(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
