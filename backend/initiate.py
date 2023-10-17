from flask_restful import Resource
import uuid
class Initiate(Resource):
    def get(self):
        id=uuid.uuid4()
        return {"id":str(id)},200
