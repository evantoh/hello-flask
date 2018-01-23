from flask import Flask
# initializing the app
app = Flask(__name__)

from app import views#this allows us to create views
