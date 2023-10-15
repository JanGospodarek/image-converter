from flask_restful import Resource, reqparse
import base64

class Image(Resource):
    def post(self):
        try:
            parse = reqparse.RequestParser()
            parse.add_argument('image64')
            args = parse.parse_args()
            image_base64 = args['image64']
            starter = image_base64.find(',')
            image_data = image_base64[starter + 1:]

            image_data = bytes(image_data, encoding="ascii")
            with open('./images/image.png', 'wb') as fh:
                fh.write(base64.decodebytes(image_data))
        except:
            return {"message": "Wystąpił problem z plikiem"}, 401
        else:
            return {"message": "Plik wysłany na serwer!"}, 200
