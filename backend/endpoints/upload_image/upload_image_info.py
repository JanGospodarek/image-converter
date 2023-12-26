from flask_restful import Resource, reqparse,fields,marshal_with
import base64
from extensions import mongo
from PIL import Image as Img
from endpoints.upload_image.upload_image import image_id
class ImageInfoUpload(Resource):

    def post(self):
        print('hej')
        parse = reqparse.RequestParser()
        parse.add_argument('imageTitle')
        parse.add_argument('tags',action='append',type=str)
        parse.add_argument('id')
        args = parse.parse_args()
        imagesCollection = mongo.db['images']

        post = imagesCollection.find_one({"name": args['id']})
        post['title']=args['imageTitle']
        post['tags']=args['tags']
        imagesCollection.update_one({"name": args['id']}, {"$set": post},upsert=False)

        print(args)
