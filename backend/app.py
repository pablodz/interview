import os
from datetime import datetime

from flask import Flask, jsonify, redirect, request, url_for
from flask.templating import render_template
from flask_mongoengine import MongoEngine
from flask_restful import Api, Resource

from _constants import (API_URL, COLLECTION_DEFAULT, DATABASE_DEFAULT,
                        HOST_WEB, LIMIT_QUERY, MONGO_URI, PORT_WEB)
from _index import Index

# Configs
app = Flask(__name__)
mydict = {
    'db': os.environ['MONGO_INITDB_DATABASE'],
    'username': os.environ['MONGODB_USERNAME'],
    'password': os.environ['MONGODB_PASSWORD'],
    'host': os.environ['MONGODB_HOST'],
}
uri = f"mongodb://{mydict['username']}:{mydict['password']}@{mydict['host']}:27017"#/{mydict['db']}
print(uri)
app.config['MONGODB_SETTINGS'] = mydict

db = MongoEngine()
db.init_app(app)


class Cat(db.Document):
    name = db.StringField()
    ownername = db.StringField()
    age = db.StringField()
    creation_date = db.DateTimeField(default=datetime.now)


class CatResource(Resource):
    """
    Dog class that has attributes to register a new dog
    """

    def get(self, dogage=None, dogowner=None):
        """
        GET Method
        """
        print('DOG GET')
        data = []

        # if dogage:
        #     dogage_info = mongo.db.dogs.find_one({"dogage": dogage}, {"_id": 0})
        #     if dogage_info:
        #         return jsonify(
        #             {
        #                 "status": "200",
        #                 "data": dogage_info,
        #             }
        #         )
        #     else:
        #         return {"response": "no dog found for {}".format(dogage)}

        # elif dogowner:
        #     cursor = mongo.db.dogs.find({"dogowner": dogowner}, {"_id": 0}).limit(
        #         LIMIT_QUERY
        #     )
        #     for dog in cursor:
        #         dog["url"] = API_URL + url_for("dogs") + "/" + dog.get("dogage")
        #         data.append(dog)

        #     return jsonify({"dogowner": dogowner, "response": data})

        # else:
        #     cursor = mongo.db.dogs.find({}, {"_id": 0, "update_time": 0}).limit(
        #         LIMIT_QUERY
        #     )

        #     for dog in cursor:
        #         print(dog)
        #         dog["url"] = API_URL + url_for("dogs") + "/" + dog.get("dogage")
        #         data.append(dog)

        #     return jsonify({"response": data})

        data = request.get_json()
        # mongo.db.dogs.insert_one(data)
        return jsonify({"response": str(data)})

    def post(self):
        """
        POST Method
        """
        print('DOG POST')
        # data = request.get_json()
        # if not data:
        #     data = {"response": "ERROR"}
        #     return jsonify(data)
        # else:
        #     dogage = data.get("dogage")
        #     if dogage:
        #         if mongo.db.dogs.find_one({"dogage": dogage}):
        #             return {"response": "dog already exists."}
        #         else:
        #             mongo.db.dogs.insert(data)
        #     else:
        #         return {"response": "dogage number missing"}

        # return redirect(url_for("dogs"))

        data = request.get_json()

        if data:
            if data.get("insert"):
                Cat(name="Cat1", ownername="Owner1", age="14yo").save()
                Cat(name="Cat1", ownername="Owner1", age="14yo").save()

                return jsonify({"response":"200"})

            if data.get("list"):
                _items = client.api_dev_db.dogs.find()
                items = [item for item in _items]

                return jsonify({"items": items})
            else:
                pass

        return jsonify(data)

    def put(self, dogage):
        """
        PUT Method
        """
        data = request.get_json()
        mongo.db.dogs.update({"dogage": dogage}, {"$set": data})
        return redirect(url_for("dogs"))

    def delete(self, dogage):
        """
        DELETE Method
        """
        mongo.db.dogs.remove({"dogage": dogage})
        return redirect(url_for("dogs"))


# Endpoints
api = Api(app)
# api.add_resource(HomePage, '/') # HomePage
api.add_resource(Index, "/", endpoint="index")
api.add_resource(CatResource, "/v1/api", endpoint="cats")
api.add_resource(CatResource, "/v1/api/<string:catage>", endpoint="catage")
api.add_resource(CatResource, "/v1/api/catowner/<string:catowner>",
                 endpoint="catowner")

if __name__ == "__main__":
    # Running main app
    app.run(debug=True,
            host=HOST_WEB,
            port=PORT_WEB)
