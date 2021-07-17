import os
from datetime import datetime

from flask import Flask, jsonify, redirect, request, url_for
from flask.templating import render_template
from flask_pymongo import PyMongo
from flask_restful import Api, Resource
from flask_docs import ApiDoc

from _constants import (COLLECTION_DEFAULT, DATABASE_DEFAULT,
                        HOST_WEB, LIMIT_QUERY, MONGO_URI, PORT_WEB)
from _index import Index

# Configs
app = Flask(__name__)
# RESTful Api documents to be excluded
app.config["API_DOC_URL_PREFIX"] = "/docs/v1/api"
app.config['RESTFUL_API_DOC_EXCLUDE'] = []

cred = {
    'db': os.environ['MONGO_INITDB_DATABASE'],
    'username': os.environ['MONGODB_USERNAME'],
    'password': os.environ['MONGODB_PASSWORD'],
    'host': os.environ['MONGODB_HOST'],
}
uri = f"mongodb://{cred['username']}:{cred['password']}@{cred['host']}:27017/{cred['db']}"
print(uri)
app.config["MONGO_URI"] = uri
mongo = PyMongo(app)
API_URL = "http://127.0.0.1:5000"


class CatResource(Resource):
    """
    Dog class that has attributes to register a new cat
    """

    def get(self, catid=None, catname=None):
        """
        Returns all cats stored on MongoDB
        """
        print('CAT GET')
        data = []

        if catid:
            print(catid)
            catid_info = mongo.db.cats.find_one(
                {"catid": catid}, {"_id": 0})
            if catid_info:
                return jsonify(
                    {
                        "status": "200",
                        "data": catid_info,
                    }
                )
            else:
                return {"response": "no cat found for {}".format(catid)}

        elif catname:
            print(catname)
            cursor = mongo.db.cats.find({"catname": catname}, {"_id": 0}).limit(
                LIMIT_QUERY
            )
            for cat in cursor:
                cat["url"] = API_URL + \
                    url_for("cats") + "/" + cat.get("catid")
                data.append(cat)

            return jsonify({"catname": catname, "response": data})

        else:
            cursor = mongo.db.cats.find({}, {"_id": 0, "update_time": 0}).limit(
                LIMIT_QUERY
            )

            for cat in cursor:
                print(cat, API_URL, url_for("cats"), "/", cat.get("catid"))
                cat["url"] = API_URL + url_for("cats") + "/" + cat.get("catid")
                data.append(cat)

            return jsonify({"response": data})

    def post(self):
        """
        Handle new cat json entries.
        Args:
            JSON
        Returns:
            JSON response

        Example:
            {"catid": "1","catname": "michifuz"}
        """
        print('CAT POST')
        data = request.get_json()
        if not data:
            data = {"response": "ERROR"}
            return jsonify(data)
        else:
            catid = data.get("catid")
            if catid:
                if mongo.db.cats.find_one({"catid": catid}):
                    return {"response": "cat already exists."}
                else:
                    mongo.db.cats.insert(data)
            else:
                return {"response": "catid number missing"}

        return redirect(url_for("cats"))

    def put(self, catid):
        """
        PUT Method
        """
        print('CAT PUT')
        data = request.get_json()
        mongo.db.cats.update({"catid": catid}, {"$set": data})
        return redirect(url_for("cats"))

    def delete(self, catid):
        """
        DELETE Method
        """
        print('CAT DELETE')
        mongo.db.cats.remove({"catid": catid})
        return redirect(url_for("cats"))


# Endpoints
api = Api(app)
ApiDoc(app)  # Documentation
# api.add_resource(HomePage, '/') # HomePage
api.add_resource(Index, "/", endpoint="index")
api.add_resource(CatResource, "/v1/api", endpoint="cats")
api.add_resource(CatResource, "/v1/api/<string:catid>", endpoint="catid")
api.add_resource(CatResource, "/v1/api/catname/<string:catname>",
                 endpoint="catname")

if __name__ == "__main__":
    # Running main app
    app.run(debug=True,
            host=HOST_WEB,
            port=PORT_WEB)
