from typing import List
from pydantic import BaseModel


class Album(BaseModel):
    album_type: str
    name: str
    release_date: str


class Artist(BaseModel):
    name: str


class Track(BaseModel):
    artists: List[Artist]
    album: Album
    name: str


class AuthError(Exception):
    pass
