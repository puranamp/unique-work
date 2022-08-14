import os
import random
from dotenv import load_dotenv
from flask import Flask, render_template, redirect, request, url_for
from flask_sqlalchemy import SQLAlchemy
from models import Routine, db
from config import Config
from forms import RoutineForm
from flask_bootstrap import Bootstrap

load_dotenv()

app = Flask(__name__)
app.config.from_object(Config)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
Bootstrap(app)

db.init_app(app)
with app.app_context():
    db.create_all()

@app.route('/', methods=['GET', 'POST'])
def index():
    form = RoutineForm()
    message = ""

    if form.validate_on_submit():
        content = request.form['routine']
        name = request.form['name']

        routine = Routine(name=name, content=content)
        routine_lst = Routine.query.all()

        if len(routine_lst) > 0:
            message = random.choice(Routine.query.all()).content
            routine.add()
            return render_template('view.html', message=message)
        
        routine.add()
        return redirect(url_for('index'))

    return render_template('index.html', form=form)
    # The routine gets added on submit with example.html


@app.route('/testing')
def hello():
    try:
        db.session.commit()
        # Test the DB
        rout = Routine(name="Pranav", content="This is test content")
        db.session.add(rout)
        db.session.commit()

        me = Routine.query.all()

        return "<h1>" + str(random.choice(me).content) + "</h1>"

    except Exception as e:
        return "<h1>" + str(e) + "</h1>"

if __name__ == "__main__":
    app.run(port=os.environ.get('PORT'))
