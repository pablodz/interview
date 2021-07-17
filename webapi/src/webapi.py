# Imports
from flask import Flask, jsonify, url_for, redirect, request
from flask_pymongo import PyMongo
from flask_restful import Api, Resource

from _constants import HOST_WEBAPI, PORT_WEBAPI, APP_URL
from index import Index

# Configs
app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/TestDB"
mongo_flask = PyMongo(app)


# Class

class Dog(Resource):
    """
    Dog class that has attributes to register a new dog
    """

    def get(self,
            id_registration=None,
            dog_owner=None
            ):
        data = []

        if id_registration:
            studnet_info = mongo_flask.testCollection.testCollection.find_one(
                {"id_registration": id_registration},
                {"_id": 0}
            )
            if studnet_info:
                return jsonify({
                    "status": "ok",
                    "data": studnet_info,
                })
            else:
                return {"response": "no dog found for {}".format(id_registration)}

        elif dog_owner:
            cursor = mongo_flask.testCollection.testCollection.find(
                {"dog_owner": dog_owner},
                {"_id": 0}
            ).limit(5)
            for dog in cursor:
                dog['url'] = APP_URL + \
                    url_for('dogs') + \
                    "/" + \
                    dog.get('id_registration')
                data.append(dog)

            return jsonify({"dog_owner": dog_owner, "response": data})

        else:
            cursor = mongo_flask.testCollection.testCollection.find(
                {},
                {"_id": 0, "update_time": 0}
            ).limit(5)

            for dog in cursor:
                print(dog)
                dog['url'] = APP_URL + \
                    url_for('dogs') +\
                    "/" +\
                    dog.get('id_registration')
                data.append(dog)

            return jsonify({"response": data})

    def post(self):
        data = request.get_json()
        if not data:
            data = {"response": "ERROR"}
            return jsonify(data)
        else:
            id_registration = data.get('id_registration')
            if id_registration:
                if mongo_flask.testCollection.testCollection.find_one({"id_registration": id_registration}):
                    return {"response": "dog already exists."}
                else:
                    mongo_flask.testCollection.testCollection.insert(data)
            else:
                return {"response": "id_registration number missing"}

        return redirect(url_for("dogs"))

    def put(self,
            id_registration
            ):
        data = request.get_json()
        mongo_flask.testCollection.testCollection.update(
            {'id_registration': id_registration},
            {'$set': data}
        )
        return redirect(url_for("dogs"))

    def delete(self,
               id_registration
               ):
        mongo_flask.testCollection.testCollection.remove({
            'id_registration': id_registration
        })
        return redirect(url_for("dogs"))


# Endpoints
api = Api(app)
# api.add_resource(HomePage, '/') # HomePage
api.add_resource(Index,
                 "/",
                 endpoint="index")
api.add_resource(Dog(),
                 "/v1/api",
                 endpoint="dogs")
api.add_resource(Dog(),
                 "/v1/api/<string:id_registration>",
                 endpoint="id_registration")
api.add_resource(Dog(),
                 "/v1/api/dog_owner/<string:dog_owner>",
                 endpoint="dog_owner")

if __name__ == "__main__":
    # Running main app
    app.run(
        debug=True,
        host=HOST_WEBAPI,
        port=PORT_WEBAPI
    )
