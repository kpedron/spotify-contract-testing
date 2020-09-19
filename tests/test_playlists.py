import unittest
from Resources import utils as Utils
from Requests.request_oauth2 import MyOAuth2
from Requests.requests import Requests

import jsonschema
import pytest
import json

class Playlists(unittest.TestCase):

    def setUp(self):
        self.data = Utils.load_json_file("data.json")

        # Get Token
        oauth2 = MyOAuth2()
        self.token = oauth2.access_token_get(self.data["client_id"],
                                             self.data["client_secret"],
                                             self.data["scope"],
                                             self.data["callback_uri"],
                                             self.data["token"])

        self.access_token = self.token["access_token"]
        self.request = Requests()

    def test_get_playlists(self):
        response = self.request.playlists_get(self.access_token, "kpedron")
        assert response.status_code == 200

        try:
            playlist_schema = Utils.load_schema_file("playlists_schema.json")
            jsonschema.validate(json.loads(response.text), playlist_schema)
        except:
            pytest.fail("JSON file received doesn't have the expected format \n", False)

    def test_create_new_playlist(self):
        body = {
            "name": "Playlist Python 20203",
            "description": "Essa playlist foi criado via python requests",
            "public": True
        }

        response = self.request.playlist_create(self.access_token, "kpedron", body)
        assert response.status_code == 201

        try:
            playlist_schema = Utils.load_schema_file("create_playlist_schema.json")
            jsonschema.validate(json.loads(response.text), playlist_schema)
        except:
            pytest.fail("JSON file received doesn't have the expected format \n", False)

    def tearDown(self):
        # Update the access token and refresh token in data.json
        self.data["token"] = self.token
        Utils.update_json_file("data.json", self.data)
