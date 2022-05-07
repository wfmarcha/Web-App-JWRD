from flask import Flask
#from flask_pymongo import PyMongo
from dotenv import load_dotenv
from flask_sock import Sock
import os

import json


load_dotenv(".flaskenv")
USERNAME = 'devUser'
PASSWORD = os.getenv("PASSWORD")
DATABASE = os.getenv("DATABASE")

print("U " ,USERNAME)
print("P "  ,PASSWORD)
print("D ", DATABASE) 

sock = Sock()

def create_app():
    # __name__ is the name of the current Python module. 
    # The app needs to know where it’s located to set up some paths, and __name__ is a convenient way to tell it that.
    app = Flask(__name__) 
    # SECRET_KEY is used by Flask and extensions to keep data safe. It’s set to 'dev' to provide a convenient value during 
    # development, but it should be overridden with a random value when deploying.
    app.config['SECRET_KEY'] = 'dev'
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.config["MONGO_URI"] = f"mongodb+srv://{USERNAME}:{PASSWORD}@clusterjwrd.49opx.mongodb.net/{DATABASE}?retryWrites=true&w=majority"
    from .database import mongo_client
    mongo_client.init_app(app)
   # from .models import login_manager
    # login_manager.init_app(app)
  
    sock.init_app(app)
    return app


@sock.route("/ws")
def socker(ws):
  while True:
      data = ws.receive()
      print("this is annoying", data)
      print('this is the ws , ',ws)
      ws.send(data)