from flask import Flask
from flask_restful import Api, Resource
from parser_moex import moex
from parser_binance import cripta


app = Flask(__name__)
api = Api()
values = {"fiat" : moex(), "cripta" : cripta()}

class Main(Resource):
    def get(self):
        return values


api.add_resource(Main, "/api/main")
api.init_app(app)


if __name__=="__main__":
    app.run(debug=True, port=5000, host="127.0.0.1")