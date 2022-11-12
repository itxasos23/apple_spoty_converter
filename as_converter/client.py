import requests
import base64
from typing import Dict

from models import AuthError
from secrets import client_id, client_secret


class SpotyClient:
    def __init__(self):
        self.token = self._get_token()

    def _get_token(self) -> str:
        try:
            b64_string = base64.b64encode(
                client_id.encode() + b":" + client_secret.encode()
            ).decode()
            response = requests.post(
                url="https://accounts.spotify.com/api/token",
                data={"grant_type": "client_credentials"},
                headers={"Authorization": f"Basic {b64_string}"},
            )
            return response.json().get("access_token")
        except Exception as ex:
            raise AuthError("Could not get token from Spotify API") from ex

    def request_track_info(self, track_id: str) -> Dict[str, str]:
        response = requests.get(
            url=f"https://api.spotify.com/v1/tracks/{track_id}",
            headers={"Authorization": f"Bearer {self.token}"},
        )

        return response.json()
