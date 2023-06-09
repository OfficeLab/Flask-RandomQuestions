# Library Import
from flask import Flask, render_template, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func

app = Flask(__name__)

# Database Declaration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sqlite.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


# Database Models
class ASKDB(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String(250))
    category = db.Column(db.String(100))


# Routing
@app.route('/')
def index():
    questionList = ASKDB.query.order_by(func.random()).limit(5)
    return render_template('index.html', **locals())

@app.route('/about')
def about():
    questiontable = ASKDB.query.all()
    return render_template('about.html', **locals())


# Start Server with python file
if __name__ == '__main__':
    app.run(debug=True)