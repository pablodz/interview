# Imports
from flask import Flask, jsonify, url_for, redirect, request
from flask_pymongo import PyMongo
from flask_restful import Api, Resource

from _constants import HOST_WEBAPI, PORT_WEBAPI, APP_URL, MONGO_URI, LIMIT_QUERY
from index import Index

# Configs
app = Flask(__name__)
app.config["MONGO_URI"] = MONGO_URI
mongo = PyMongo(app)


# Class


class Dog(Resource):
    """
    Dog class that has attributes to register a new dog
    """

    def get(self, idregistration=None, dogowner=None):
        """
        GET Method
        """
        data = []

        if idregistration:
            idregistration_info = mongo.db.dogs.find_one(
                {"idregistration": idregistration}, {"_id": 0}
            )
            if idregistration_info:
                return jsonify(
                    {
                        "status": "ok",
                        "data": idregistration_info,
                    }
                )
            else:
                return {"response": "no dog found for {}".format(idregistration)}

        elif dogowner:
            cursor = mongo.db.dogs.find({"dogowner": dogowner}, {"_id": 0}).limit(
                LIMIT_QUERY
            )
            for dog in cursor:
                dog["url"] = APP_URL + url_for("dogs") + "/" + dog.get("idregistration")
                data.append(dog)

            return jsonify({"dogowner": dogowner, "response": data})

        else:
            cursor = mongo.db.dogs.find({}, {"_id": 0, "update_time": 0}).limit(
                LIMIT_QUERY
            )

            for dog in cursor:
                print(dog)
                dog["url"] = APP_URL + url_for("dogs") + "/" + dog.get("idregistration")
                data.append(dog)

            return jsonify({"response": data})

    def post(self):
        """
        POST Method
        """
        data = request.get_json()
        if not data:
            data = {"response": "ERROR"}
            return jsonify(data)
        else:
            idregistration = data.get("idregistration")
            if idregistration:
                if mongo.db.dogs.find_one({"idregistration": idregistration}):
                    return {"response": "dog already exists."}
                else:
                    mongo.db.dogs.insert(data)
            else:
                return {"response": "idregistration number missing"}

        return redirect(url_for("dogs"))

    def put(self, idregistration):
        """
        PUT Method
        """
        data = request.get_json()
        mongo.db.dogs.update({"idregistration": idregistration}, {"$set": data})
        return redirect(url_for("dogs"))

    def delete(self, idregistration):
        """
        DELETE Method
        """
        mongo.db.dogs.remove({"idregistration": idregistration})
        return redirect(url_for("dogs"))


# Endpoints
api = Api(app)
# api.add_resource(HomePage, '/') # HomePage
api.add_resource(Index, "/", endpoint="index")
api.add_resource(Dog(), "/v1/api", endpoint="dogs")
api.add_resource(Dog(), "/v1/api/<string:idregistration>", endpoint="idregistration")
api.add_resource(Dog(), "/v1/api/dogowner/<string:dogowner>", endpoint="dogowner")

if __name__ == "__main__":
    # Running main app
    app.run(debug=True, host=HOST_WEBAPI, port=PORT_WEBAPI)
