from flask import Flask, render_template, request, url_for, redirect, Blueprint, current_app
from flask_login import current_user, login_required

homePage = Blueprint('homePage', __name__)


@homePage.route('/', methods=["GET", "POST"])
@login_required
def home():
    print(current_user.is_authenticated)
    card = [1, 2, 3, 4, 5, 6, 7]
    return render_template('home.html', carte=card)
