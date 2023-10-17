
from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from upload_image import Image
from initiate import Initiate
# config

app = Flask(__name__)
CORS(app)
api = Api(app)

# routes
api.add_resource(Initiate,'/init')
api.add_resource(Image,'/upload_image')

if __name__ == "__main__":
    app.run(port=8000, debug=True)
