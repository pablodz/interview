
import unittest

from ..app import app
from flask_pymongo import PyMongo
import os
cred = {
    'db': "webapp",
    'username': "interview",
    'password': "interview",
    'host': "mongodb",
}
uri = f"mongodb://{cred['username']}:{cred['password']}@{cred['host']}:27017/{cred['db']}"
print(uri)
app.config["MONGO_URI"] = uri
mongo = PyMongo(app)

class BaseCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.db = db.get_db()

