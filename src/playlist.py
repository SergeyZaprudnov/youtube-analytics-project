import datetime
import os
import isodate
from src.video import Channel
from googleapiclient.discovery import build


class PlayList:
    def __init__(self, id_playlist):
        self.id_playlist = id_playlist
        self.url = 'https://www.youtube.com/playlist?list=' + self.id_playlist
        self.youtube = Channel.get_service().playlistItems().list(
            playlistId=self.id_playlist,
            part='snippet,contentDetails,id,status',
            maxResults=10,
        ).execute()
