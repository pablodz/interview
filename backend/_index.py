from flask import redirect, url_for
from flask_restful import Api, Resource


class Index(Resource):
    def get(self):
        return redirect(url_for("cats"))
