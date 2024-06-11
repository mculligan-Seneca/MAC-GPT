from flask import Flask,request
from flask_restful import Api, Resource


app=Flask(__name__)
api=Api(app)

#TODO: Send Application to client
@app.route("/")
def init_application():
    return "hello world"



if __name__=="__main__":
    app.run(debug=True)
