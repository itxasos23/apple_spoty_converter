import re
from typing import Dict

from models import Track
from client import SpotyClient


def get_track_id(spoty_link: str) -> str:
    return re.match(r"^https://open\.spotify\.com/track/(.+)\?.*$", spoty_link).group(1)


def get_track_info(spoty_link: str) -> Dict[str, str]:
    track_dict = SpotyClient().request_track_info(get_track_id(spoty_link))
    track = Track(**track_dict)

    return {
        "track_link": spoty_link,
        "track_name": track.name,
        "artists": list(map(lambda x: x.name, track.artists)),
        "album_name": track.album.name,
    }


if __name__ == "__main__":
    spoty_link = (
        "https://open.spotify.com/track/0GiMQKtXETUOKHEXnDmqEm?si=a96f2b3f8ec54097"
    )
    get_track_info(spoty_link)
