from src.channel import Channel


class Video:

    def __init__(self, id_video: str) -> None:
        self.id_video = id_video

    @property
    def youtube(self):
        return Channel.get_service().videos().list(
            part='snippet,statistics,contentDetails,topicDetails', id=self.id_video
        ).execute()

    @property
    def name(self):
        return self.youtube.get('items')[0].get('snippet').get('title')

    @property
    def url(self):
        return 'https://www.youtube.com/watch?v=' + self.youtube.get('items')[0].get('id')

    @property
    def view_count(self):
        return self.youtube.get('items')[0].get('statistics').get('viewCount')

    @property
    def like_count(self):
        return self.youtube.get('items')[0].get('statistics').get('likeCount')

    def __str__(self):
        return f'{self.name}'


class PLVideo(Video):

    def __init__(self, id_video, id_playlist):
        self.id = id_video
        self.id_playlist = id_playlist
        super().__init__(id_video)
