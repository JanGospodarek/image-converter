
from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from endpoints.upload_image import Image
from initiate import Initiate
from extensions import mongo
from endpoints.convert.convert_pixel_art import ConvertPixelArt
from endpoints.send_image import SendImage
app = Flask(__name__)
CORS(app)
api = Api(app)

app.config['MONGO_URI'] = "mongodb://localhost:27017/db-ascii"
mongo.init_app(app)

# routes
api.add_resource(Initiate,'/init')
api.add_resource(Image,'/upload_image')
api.add_resource(ConvertPixelArt,'/convert')
api.add_resource(SendImage,'/download_image')




if __name__ == "__main__":
    app.run(port=8000, debug=True)



