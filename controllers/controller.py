from flask import render_template
from app import app
from modules.calulator import *


@app.route('/add/<number1>/<number2>')
def add(number1, number2):
    return render_template('index.html', title='Add', add_numbers=add)

@app.route('/orders/<index>')
def order(index):
    customer_order = orders[int(index)]
    return render_template('order.html', title='Your', order=customer_order)