from flask import Flask
from flask_restful import Api, Resource
from parser_moex import norm
from parser_binance import cripta


app = Flask(__name__)
api = Api()


class Main(Resource):
    def get(self):
        return {"fiat" : norm(), "cripta" :  cripta()}


api.add_resource(Main, "/api/main")
api.init_app(app)


if __name__=="__main__":
    app.run(debug=True, port=5000, host="127.0.0.1")