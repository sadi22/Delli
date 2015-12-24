from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    return render_template('home.html');


@app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html');



@app.route('/signup')
def signup():
<<<<<<< HEAD
    return render_template('signup.html');

@app.route('/products')
def products():
    return render_template('products.html');
=======
    return render_template('signup.html');
>>>>>>> 484932b8c1b21138ed379c45cc31715ba76ebc13
