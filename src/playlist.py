from src.video import Channel
import datetime
import os
import isodate
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
        self.title = self.youtube.get('items')[0].get('snippet').get('title')[-19:].replace(' ', '. ')
        self.video_response = Channel.get_service().videos().list(
            part='contentDetails,statistics',
            id=','.join(self.video_ids)
        ).execute()


@property
def total_duration(self):
    """длительность плейлиста"""
    return self.video_time


@property
def video_ids(self):
    """все id листа"""
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


def show_best_video(self):
    """ссылка на самое популярное видео """
    like_count = 0
    id_best_video = ''
    for item in self.video_response.get('items'):
        if int(item.get('statistics').get('likeCount')) > like_count:
            id_best_video = item.get('id')
    return 'https://youtu.be/' + id_best_video
