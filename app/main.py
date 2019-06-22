# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

#import générique
import os
from datetime import datetime

#import flask
from flask import Flask, render_template, request, url_for, redirect
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
from helper.googleCloud import GoogleHelper

firebase_request_adapter = requests.Request()
login_manager = LoginManager()


app = Flask(__name__)
app.config.from_object('environnement.DevelopmentConfig')
login_manager.init_app(app)


googleHelper = GoogleHelper(
    app.config['PROJET_ID'], app.config['IOT_REGION'], app.config['GOOGLE_JSON'])
# TODO a déplacer dans le google helper
datastore_client = datastore.Client.from_service_account_json(
    app.config['GOOGLE_JSON'])


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

    return times


@login_manager.user_loader
def load_user(user_id):
    print(user_id)
    u = UserHelper(Users).getUserById(user_id)
    print(u.nom)
    return u


@app.route('/')
@app.route('/login')
def root():
    # Verify Firebase auth.
    id_token = request.cookies.get("token")
    error_message = None
    claims = None
    times = None

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
                store_time(datetime.now())
                return redirect(url_for('home'))
            else:
                error_message = "user not register in the application"

        times = fetch_times(10)

    return render_template(
        'index.html',
        user_data=claims, error_message=error_message, times=times)


@app.route('/home')
@login_required
def home():
    print(current_user.is_authenticated)
    card = [1, 2, 3, 4, 5, 6, 7]
    return render_template('home.html', carte=card)


@app.route('/capteur')
@login_required
def capteur():
    # TODO A déplacer dans la config
    registry_id = app.config['REGISTER_ID']
    devices = googleHelper.getDevices(registry_id)

    return render_template('capteur.html', devices=devices)


if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    app.run(host='0.0.0.0', port=8080, debug=True)
