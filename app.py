from flask import Flask, render_template, flash, redirect, url_for
from config import DevConfig
import form2

app = Flask(__name__)
app.config.from_object(DevConfig)


@app.route('/')
@app.route('/index')
def index():
    return render_template('IndEx2_17087024.html')


@app.route('/signup', methods=['POST', 'GET'])
def signup():
    form = form2.SignupForm()
    if form.validate_on_submit():
        flash('Signup requested for {}'.format(form2.name.data))
        return redirect(url_for('index'))
    return render_template('signup.html', form=form)
