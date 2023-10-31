
from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from upload_image import Image
from initiate import Initiate
from model import db
# config
app = Flask(__name__)
CORS(app)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///database.db'
db.init_app(app)
#
# with app.app_context():
#     db.create_all()

# routes
api.add_resource(Initiate,'/init')
api.add_resource(Image,'/upload_image')

if __name__ == "__main__":
    app.run(port=8000, debug=True)
