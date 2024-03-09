from flask import Flask
from datetime import datetime
from main import app
from flask import request, redirect, render_template, session
from models.user import User
from models.prayer import Prayer

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/prayers')
def prayers():
    list_of_prayers = Prayer.get_all_prayers()
    return render_template('all_prayers.html', prayers=list_of_prayers)

@app.route('/process_form', methods=['POST'])
### REMEMBER TO AUTO ASSIGN AN ID NUMBER TO THE USER###
def process_form():
    user_check = {
        'user_name': request.form['user_name'],
        'phone_number': request.form['phone_number'],
        'email': request.form['email']
    }
    prayer_add = {
        'content': request.form['content'],
        'user_name': request.form['user_name'],
        'pastor_name': '',
        'created_at': datetime.now(),
        'answered': ''
    }
    if not User.validate_user(request.form):
        return redirect('/')
    if not User.check_users_exists(user_check):
        session['user_name'] = User.add_user(user_check).user_name
        Prayer.add_prayer(prayer_add)
        return redirect('/prayers')
    session['user_name'] = User.get_user_by_name(user_check['user_name'])
    Prayer.add_prayer(prayer_add)
    return redirect('/prayers')

@app.route('/clear_session')
def clear():
    session.clear()
    return redirect('/')


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)

'''
this line is for testing purposes, not production

would need to be changed to os.environ.get('SECRET_KEY')
or something of the like to grab the environments secret
key
'''
# app.config['SECRET_KEY'] = generate_cipher()