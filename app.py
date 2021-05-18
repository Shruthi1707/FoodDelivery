from flask import Flask, redirect, url_for, request, render_template
from backend import *
app = Flask(__name__)



@app.route('/')
def main_page():
    return render_template('main_page.html')

@app.route('/orderfood', methods=["GET", "POST"])
def orderfood():
    if request.method == "POST":
        name = request.form.get("name")
        address = request.form.get("address")
        pin= int(request.form.get('pin'))
        age=int(request.form.get('age'))
        number = int(request.form.get('number'))
        option = request.form.get('option')
        if option == 'veg':
            food='veg'
        elif option == 'nonveg':
            food='nonveg'
        else:
            pass
        option = request.form.get('combo')
        if option == 'rice':
            foodtype = 'rice'
        elif option == 'roti':
            foodtype = 'roti'
        elif option == 'salad':
            foodtype = 'salad'
        else:
            pass
        suggestions = request.form.get("suggestions")

    return render_template("orderfood.html")

@app.route('/volunteer', methods=["GET", "POST"])
def volunteer():
    if request.method == "POST":
        name = request.form.get("name")
        address = request.form.get("address")
        pin= int(request.form.get('pin'))
        number = int(request.form.get('number'))
        option = request.form.get('option')
        if option == 'veg':
            food='veg'
        elif option == 'nonveg':
            food='nonveg'
        else:
            pass

    return render_template("volunteer.html")

@app.route('/signin', methods=["GET", "POST"])
def signin():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        getname(username,password)
    return render_template("signin.html")

def getname(name,password):
    print(name,password)


@app.route('/orderconfirmation', methods=["GET", "POST"])
def orderconfirmation():
    return render_template("orderconfirmation.html")

if __name__ == '__main__':
    app.run()
