from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_scss import Scss

from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

import requests
from bs4 import BeautifulSoup

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///sqlite3.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)
Scss(app, static_dir='app/static/css', asset_dir='app/assets/scss')

class Service(db.Model):
    __tablename__ = 'services'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    created_at = db.Column(db.DateTime(timezone=True),
                           server_default=func.now())
    updated_at = db.Column(db.DateTime(timezone=True), onupdate=func.now())
    parent = relationship("Service", back_populates="services")


class StatusRecord(db.Model):
    __tablename__ = 'status_records'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)


@app.route('/')
def index():
    return render_template('intubacao_sedacao_ga.html')

@app.route('/intubacao')
def intubacao():
    return render_template('intubacao_sedacao_ga.html')

@app.route('/doses-pediatricas')
def doses_pediatricas():
    return render_template('doses_pediatricas.html')

@app.route('/5h5t')
def aesp():
    return render_template('5h5t.html')

@app.route('/trechos-exame')
def trechos():
    return render_template('trechos.html')