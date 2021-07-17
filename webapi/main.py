# Imports
from pymongo import MongoClient
from flask import (Flask, jsonify)
from flask_restful import (Api, Resource)


app = Flask(__name__)
api = Api(app)


client = MongoClient("mongodb://db:27017")
db = client["TestDB"]
testCollection = db["testCollection"]


# Class Hello
class Hello(Resource):
    def get(self):
        """
        Returns a Hello jsonified
        """

        responseJson = {
            "status": "200",
            "message": "Hello there, this is Hello Class json response."
        }

        return jsonify(responseJson)

# Class Homepage


class HomePage(Resource):
    def get(self):
        """
        Returns a JSON with GET endpoints
        """

        responseJson = {
            "message": "HomePage: here you can check all endpoints listed on this site dockerized.",
            "status": "200",
            "hello": "/hello",
        }

        return jsonify(responseJson)


# HomePage
api.add_resource(HomePage, '/')
# HelloPage
api.add_resource(Hello, '/hello')


if __name__ == "__main__":
    # Run the main app
    app.run(
        debug=True,
        host='0.0.0.0',
        port=8501
    )
