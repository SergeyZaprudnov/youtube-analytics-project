from src.channel import Channel


class Video:

    def __init__(self, id_video: str) -> None:
        self.id_video = id_video
        try:
            self.youtube = Channel.get_service().videos().list(
                part='snippet,statistics,contentDetails,topicDetails', id=self.id_video
            ).execute()
            self.title = self.youtube.get('items')[0].get('snippet').get('title')
            self.url = 'https://www.youtube.com/watch?v=' + self.youtube.get('items')[0].get('id')
            self.viev_count = self.youtube.get('items')[0].get('statistics').get('viewCount')
            self.like_count = self.youtube.get('items')[0].get('statistics').get('likeCount')
        except IndexError:
            print('Не верная ссылка!!!')
            self.youtube = None
            self.title = None
            self.url = None
            self.viev_count = None
            self.like_count = None

    def __str__(self):
        return f'{self.title}'


class PLVideo(Video):

    def __init__(self, id_video, id_playlist):
        self.id = id_video
        self.id_playlist = id_playlist
        super().__init__(id_video)
