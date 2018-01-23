from flask import Flask
from .config import DevConfig
# initializing the app
app = Flask(__name__,instance_relative_config = True)
#instance_relative_config allows us to connect to the instance  folder when app instance is created
#setting up configurations
app.config.from_object(DevConfig)
app.config.from_pyfile('config.py')#connects to the config.py file and all its content are appended to the app.config
#method for setting up configurations
# and pass Devconfig subclass

from app import views#this allows us to create views
