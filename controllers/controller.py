from flask import render_template
from app import app
from models.orders import orders

@app.route('/orders')
def index():
    return render_template('index.html', title='Home', orders=orders)

@app.route('/orders/<index>')
def order_by_index(index):
    order = orders[int(index)]
    return render_template('order.html', order=order)