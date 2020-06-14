import pickle

from flask import Flask, render_template, request ,redirect, url_for
from myfunctions import*
from myfunctions import seller, customer

app= Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/seller')      #to redirect to login portal
def seller():
    return render_template('sellerlogin.html', access_granted = True)

@app.route('/sellernew') #to redirect to register portal
def sellernew():
    return render_template('sellerregister.html', is_new_user = True, password_match = True)

@app.route('/sellerlogin', methods = ["POST"])
def sellerlogin():
    username = request.form.get("username")
    password = request.form.get("password")
    access_granted = existingseller(username, password)
    if access_granted:
        return redirect(url_for('dashboard_seller'))
    else:
        return render_template('sellerlogin.html', access_granted = access_granted)

@app.route('/sellerregister', methods = ["POST"])
def sellerregister():
    username = request.form.get("username")
    password = request.form.get("password")
    confirm_password = request.form.get("confirm_password")
    if password != confirm_password:
        password_match = False
    else:
        password_match = True
    is_new_user = newseller(username, password)
    if is_new_user and password_match:
        return redirect(url_for('dashboard_seller'))
    else:
        return render_template('sellerregister.html', is_new_user = is_new_user, password_match = password_match)

@app.route('/customer')      #to redirect to login portal
def customer():
    return render_template('customerlogin.html', access_granted = True)

@app.route('/customernew') #to redirect to register portal
def customernew():
    return render_template('customerregister.html', is_new_user = True, password_match = True)

@app.route('/customerlogin', methods = ["POST"])
def customerlogin():
    username = request.form.get("username")
    password = request.form.get("password")
    access_granted = existingcustomer(username, password)
    if access_granted:
        return redirect(url_for('dashboard_customer'))
    else:
        return render_template('customerlogin.html', access_granted = access_granted)

@app.route('/customerregister', methods = ["POST"])
def customerregister():
    username = request.form.get("username")
    password = request.form.get("password")
    confirm_password = request.form.get("confirm_password")
    if password != confirm_password:
        password_match = False
    else:
        password_match = True
    is_new_user = newcustomer(username, password)
    if is_new_user and password_match:
        return redirect(url_for('dashboard_customer'))
    else:
        return render_template('customerregister.html', is_new_user = is_new_user, password_match = password_match)

@app.route('/dashboard_seller')
def dashboard_seller():
    return render_template('dashboard_seller.html')

@app.route('/dashboard_customer')
def dashboard_customer():
    return render_template('dashboard_customer.html')
