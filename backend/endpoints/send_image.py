import base64

from flask_restful import Resource, reqparse,fields,marshal_with
from flask import request,jsonify
class SendImage(Resource):
    def post(self):
        try:
            parse = reqparse.RequestParser()
            parse.add_argument('image')
            args = parse.parse_args()

            file_name = args["image"]

            # url=''
            # if fileName.count('pixel')!=0:
            url=f'./data/stored/{file_name}.png'
            print(url)
            with open(url, "rb") as image_file:
                encoded = base64.b64encode(image_file.read()).decode('utf-8')
            enc_str = str(encoded)
            response = jsonify({"imageData": encoded})
        except:
            return {"message": "Wystąpił problem z plikiem"}, 400
        else:
            return response
