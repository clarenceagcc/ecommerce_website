from flask import render_template, request, redirect, url_for
from app import app, db
from app.models import User, Product, Order

@app.route('/')
def home():
    products = Product.query.all()
    return render_template('home.html', products=products)

@app.route('/product/<int:product_id>')
def product_detail(product_id):
    product = Product.query.get_or_404(product_id)
    return render_template('product_detail.html', product=product)

# Add more routes for login, signup, cart, etc.