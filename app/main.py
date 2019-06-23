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
from flask import Flask, render_template, request, url_for, redirect, Blueprint
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


login_manager = LoginManager()


app = Flask(__name__)
app.config.from_object('environnement.DevelopmentConfig')
login_manager.init_app(app)

#on met le googlehelper dans le contexte de l'app pour l'avoir dans les blueprints
app.googleHelper = GoogleHelper(
    app.config['PROJET_ID'], app.config['IOT_REGION'], app.config['GOOGLE_JSON'])



@login_manager.user_loader
def load_user(user_id):
    print(user_id)
    u = UserHelper(Users).getUserById(user_id)
    print(u.nom)
    return u


# Blueprint Import
#import des vues après le contexte
from views.login import login
from views.home import homePage
from views.sensor import capteur

app.register_blueprint(login, url_prefix='/')
app.register_blueprint(login, url_prefix='/login')
app.register_blueprint(homePage, url_prefix='/home')
app.register_blueprint(capteur, url_prefix='/capteur')


if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    app.run(host='0.0.0.0', port=8080, debug=True)
