#import générique
import os
from datetime import datetime

#import flask
from flask import Flask, render_template, request, url_for, redirect, Blueprint, current_app
from flask_login import LoginManager, current_user, login_user, login_required

# import des api google
from google.auth.transport import requests
from google.cloud import datastore
from google.oauth2 import service_account
from googleapiclient import discovery
from googleapiclient.errors import HttpError
import google.oauth2.id_token

# import du modèle de donnée & helper
from model.user import User, UserHelper, Users

login = Blueprint('login', __name__)


# TODO a déplacer dans le google helper
""" datastore_client = datastore.Client.from_service_account_json(
    current_app.config['GOOGLE_JSON'])

def store_time(dt):
    entity = datastore.Entity(key=datastore_client.key('visit'))
    entity.update({
        'timestamp': dt
    })

    datastore_client.put(entity)


def fetch_times(limit):
    query = datastore_client.query(kind='visit')
    #query.order = ['-timestamp']

    times = query.fetch(limit=limit)

    return times """

@login.route('/', methods=["GET", "POST"])
def home():
  # Verify Firebase auth.
    id_token = request.cookies.get("token")
    error_message = None
    claims = None
    times = None
    with current_app.app_context():
        firebase_request_adapter = requests.Request()

    if id_token:
        try:
            # Verify the token against the Firebase Auth API. This example
            # verifies the token on each page load. For improved performance,
            # some applications may wish to cache results in an encrypted
            # session store (see for instance
            # http://flask.pocoo.org/docs/1.0/quickstart/#sessions).
            claims = google.oauth2.id_token.verify_firebase_token(
                id_token, firebase_request_adapter)
        except ValueError as exc:
            # This will be raised if the token is expired or any other
            # verification checks fail.
            error_message = str(exc)

        # Record and fetch the recent times a logged-in user has accessed
        # the site. This is currently shared amongst all users, but will be
        # individualized in a following step.
        print(claims)
        if claims:
            u = UserHelper(Users).getUserByEmail(claims['email'])
            if u:
                login_user(u)
                #store_time(datetime.now())
                return redirect(url_for('homePage.home'))
            else:
                error_message = "user not register in the application"

        #times = fetch_times(10)
        times = {}

    return render_template(
        'index.html',
        user_data=claims, error_message=error_message, times=times)
