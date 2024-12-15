"""Blogly application."""

from flask import Flask, render_template, redirect, request, url_for
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, User

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = 'secretkey'
toolbar = DebugToolbarExtension(app)

db.init_app(app)

with app.app_context():
    db.create_all()


@app.route('/')
def root():
    """Redirect to /users."""
    return redirect('/users')

@app.route('/users')
def list_users():
    """Show a list of all users."""
    users = User.query.order_by(User.last_name, User.first_name).all()
    return render_template('user_list.html', users=users)

@app.route('/users/<int:user_id>')
def show_user(user_id):
    """Show details about a single user."""
    user = User.query.get_or_404(user_id)
    return render_template('user_detail.html', user=user)

@app.route('/users/new', methods=['GET', 'POST'])
def add_user():
    """Add a new user."""
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        image_url = request.form['image_url'] or None

        new_user = User(first_name=first_name, last_name=last_name, image_url=image_url)
        db.session.add(new_user)
        db.session.commit()
        return redirect('/users')
    return render_template('user_new.html')

@app.route('/users/<int:user_id>/edit', methods=['GET', 'POST'])
def edit_user(user_id):
    """Edit an existing user."""
    user = User.query.get_or_404(user_id)

    if request.method == 'POST':
        user.first_name = request.form['first_name']
        user.last_name = request.form['last_name']
        user.image_url = request.form['image_url']
        db.session.commit()
        return redirect('/users')
    return render_template('user_edit.html', user=user)

@app.route('/users/<int:user_id>/delete', methods=['POST'])
def delete_user(user_id):
    """Delete a user."""
    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()
    return redirect('/users')
