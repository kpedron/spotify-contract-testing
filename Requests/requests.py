import requests


class Requests:

    def playlists_get(self, access_token, userid):
        base_url = "https://api.spotify.com/v1/users/"
        url = base_url + userid + "/playlists"

        headers = {"Authorization": "Bearer " + access_token}
        query = {"limit": 2}

        return requests.get(url=url, headers=headers, params=query)

    def playlist_create(self, access_token, userid, body):
        base_url = "https://api.spotify.com/v1/users/"
        url = base_url + userid + "/playlists"

        headers = {"Authorization": "Bearer " + access_token}

        return requests.post(url=url, headers=headers, json=body)

