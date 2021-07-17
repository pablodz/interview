import random
import json

from tests.Base import BaseCase


class TestUserLogin(BaseCase):

    def test_successful_login(self):
        # Given
        catid = f"{random.randint(1,10000)}"
        catname = f"catname{random.randint(1,10000)}"
        payload = json.dumps({
            "catid": catid,
            "catname": catname
        })
        response = self.app.post(
            '/api/auth/signup', headers={"Content-Type": "application/json"}, data=payload)

        # When
        response = self.app.post(
            '/api/auth/login', headers={"Content-Type": "application/json"}, data=payload)

        # Then
        self.assertEqual(str, type(response.json['token']))
        self.assertEqual(200, response.status_code)
