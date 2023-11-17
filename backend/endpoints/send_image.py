import base64

from flask_restful import Resource, reqparse,fields,marshal_with
from flask import request,jsonify
class SendImage(Resource):
    def get(self):
        try:
            file_name = request.args.get("file_name")


            # url=''
            # if fileName.count('pixel')!=0:
            url=f'./data/temp/{file_name}-pixel.png'
            encoded=''
            with open(url, "rb") as image_file:
                encoded = base64.b64encode(image_file.read())
        except:
            return {"message": "Wystąpił problem z plikiem"}, 400
        else:
            return jsonify({"imageData":str(encoded)})
