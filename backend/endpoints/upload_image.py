from flask_restful import Resource, reqparse,fields,marshal_with
import base64
from extensions import mongo
class Image(Resource):

    def post(self):
        try:
            parse = reqparse.RequestParser()
            parse.add_argument('image64')
            parse.add_argument('id')
            args = parse.parse_args()

            image_base64 = args['image64']
            starter = image_base64.find(',')
            image_data = image_base64[starter + 1:]

            fileName=args["id"]
            imagesCollection=mongo.db['images']

            if imagesCollection.count_documents({"name":fileName})==0:
                imagesCollection.insert_one({"name":fileName,"tags":[]})
            image_data = bytes(image_data, encoding="ascii")

            with open(f'./data/stored/{fileName}.png', 'wb') as fh:
                fh.write(base64.decodebytes(image_data))
        except:
            return {"message": "Wystąpił problem z plikiem"}, 400
        else:
            return {"message": "Plik wysłany na serwer!" }, 200