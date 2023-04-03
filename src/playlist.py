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


@property
def video_ids(self):
    """Получаем все id листа"""
    video_ids: list[str] = [video['contentDetails']['videoId'] for video in self.youtube['items']]
    return video_ids

@property
def video_time(self):
    """Длительность роликов"""
    res = datetime.timedelta()

    for video in self.video_response['items']:
        iso_8601_duration = video['contentDetails']['duration']
        duration = isodate.parse_duration(iso_8601_duration)
        res += duration
    return res

