from flask import Flask, render_template, request, url_for, redirect, Blueprint, current_app
from flask_login import current_user, login_required

capteur = Blueprint('capteur', __name__)


@capteur.route('/', methods=["GET", "POST"])
@login_required
def home():
    registry_id = current_app.config['REGISTER_ID']
    devices = current_app.googleHelper.getDevices(registry_id)

    return render_template('capteur.html', devices=devices)
