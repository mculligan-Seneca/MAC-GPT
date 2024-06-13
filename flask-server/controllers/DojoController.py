from flask_restful import Resource
from flask import request




#web controller for the DOJO screen
class DojoController(Resource):


    def post(self):
        
        f=request.files['file']
        file_path=f"../input_data/{f.filename}"
        f.save(file_path)
        return {'response':'ok'}
        
