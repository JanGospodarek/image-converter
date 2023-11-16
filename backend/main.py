
from flask import Flask,g
from flask_restful import Api
from flask_cors import CORS
from upload_image import Image
from initiate import Initiate

from flask_pymongo import PyMongo


app = Flask(__name__)
CORS(app)
api = Api(app)

app.config['MONGO_URI'] = "mongodb://localhost:27017/db-ascii"

db = PyMongo(app).db

api.add_resource(Initiate,'/init')
api.add_resource(Image,'/upload_image')



if __name__ == "__main__":
    app.run(port=8000, debug=True)



