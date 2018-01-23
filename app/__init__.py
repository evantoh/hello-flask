from flask import Flask
from .config import DevConfig
# initializing the app
app = Flask(__name__)

#setting up configurations
app.config.from_object(DevConfig)#method for setting up configurations
# and pass Devconfig subclass

from app import views#this allows us to create views
