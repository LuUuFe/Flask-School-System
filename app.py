from flask import Flask, render_template, redirect, url_for, flash, request
from flask_sqlalchemy import SQLAlchemy
from forms import StudentForm

app = Flask(__name__)

app.config.from_pyfile('config.py')

@app.route('/', methods=['GET', 'POST'])
def index():
  return render_template('index.html')

if __name__ == '__main__':
  app.run(debug=True)