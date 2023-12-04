from flask_restful import Resource, reqparse,fields,marshal_with
from extensions import mongo
from flask import jsonify,make_response
import base64
from PIL import Image
class ConvertPixelArt(Resource):
    def post(self):
        try:
            parse = reqparse.RequestParser()
            parse.add_argument('name')
            parse.add_argument('pixels')
            args = parse.parse_args()
            print(args)

            file_name = args["name"]
            pixel_amount=int(args["pixels"])
            url=f'./data/temp/{file_name}-pixel.png'

            pixelate(file_name,f'./data/stored/{file_name}.png',url,pixel_amount)
            encoded = ''
            with open(url, "rb") as image_file:
                encoded = base64.b64encode(image_file.read()).decode('utf-8')
            response = jsonify({"imageData":encoded})
        except:
            return {"message": "Wystąpił problem z plikiem"}, 400
        else:
            return response



def pixelate(file_name,input_file_path,url_to_save, pixel_size):
    print(input_file_path,pixel_size)
    image = Image.open(input_file_path)
    image = image.resize(
        (image.size[0] // pixel_size, image.size[1] // pixel_size),
        Image.NEAREST
    )
    image = image.resize(
        (image.size[0] * pixel_size, image.size[1] * pixel_size),
        Image.NEAREST
    )
    # image.show()
    image.save(url_to_save)


