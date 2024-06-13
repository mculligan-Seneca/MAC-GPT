from flask import Flask,send_from_directory
from flask_restful import Api, Resource
from flask_cors import CORS
from controllers.DojoController import DojoController
from controllers.ChatController import ChatController

import os
app=Flask(__name__,static_folder='./static/react/build')
api=Api(app)
CORS(app)

class RootController(Resource):
    def get(self):
             return send_from_directory(app.static_folder,'index.html')
    
class StaticController(Resource):
     def get(self,path):
             return send_from_directory(os.path.join(app.static_folder, 'static'), path)

"""
#TODO: Send Application to client
@app.route("/")
def init_application():
   
#loads json and css resources
@app.route('/static/<path:path>')
def serve_static(path):
    return send_from_directory(os.path.join(app.static_folder, 'static'), path)

"""
def main():
    controllers=[

        (DojoController,'/dojo'),
        (ChatController,'/chat'),
        (RootController,'/'),
        (StaticController,'/static/<path:path>')
        

    ]
  
    for controller,route in controllers:
        api.add_resource(controller,route)
    app.run(debug=True)


if __name__=="__main__":
    main()
