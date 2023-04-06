import os
import json
# from dataclasses import dataclass
from googleapiclient.discovery import build


class Channel:
    """Класс для ютуб-канала"""
    api_key: str = os.getenv('YT_API_KEY')
    youtube = build('youtube', 'v3', developerKey='AIzaSyAadr26UgIsn6iQWS9uITSr7wV0_h7JYfE')

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        channel = Channel.youtube.channels().list(id=channel_id, part='snippet,statistics').execute()
        self.__channel_id = channel_id
        self.title = channel.get('items')[0].get('snippet').get('title')
        self.description = channel.get('items')[0].get('snippet').get('description')
        self.url = 'https://www.youtube.com/' + channel.get('items')[0].get('snippet').get('customUrl')
        self.subscriberCount = channel.get('items')[0].get('statistics').get('subscriberCount')
        self.video_count = channel.get('items')[0].get('statistics').get('videoCount')
        self.viewCount = channel.get('items')[0].get('statistics').get('viewCount')

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        channel = self.youtube.channels().list(id=self.channel_id, part='snippet,statistics').execute()
        print(json.dumps(channel, indent=2, ensure_ascii=False))

    @property
    def channel_id(self) -> str:
        """Геттер для id канала"""
        return self.__channel_id

    @classmethod
    def get_service(cls):
        """Возвращает объект для работы с YouTube API"""
        return cls.youtube

    def to_json(self, file_name: str) -> None:
        """Сохраняет в файл значения атрибутов экземпляра Channel"""
        a = self.__dict__
        print(a)
        with open(file_name, 'w') as file:
            json.dump(a, file, indent='\t', ensure_ascii=False, default=self.default_value)

    @staticmethod
    def default_value(value):
        """Возвращает значение в формате json"""
        return json.dumps(value.__dict__, indent='\t', ensure_ascii=False, default=None)

    def __str__(self):
        """Отображает название и url канала"""
        return f'{self.title} ({self.url})'

    def __add__(self, other):
        """Складывает подписчиков 2-х каналов"""
        return int(self.subscriberCount) + int(other.subscriberCount)

    def __sub__(self, other):
        """Вычитает подписчиков"""
        return int(self.subscriberCount) - int(other.subscriberCount)

    def __ge__(self, other):
        """Сравнивает подписчиков"""
        if int(self.subscriberCount) >= int(other.subscriberCount):
            return True
        else:
            return False

    def __gt__(self, other):
        """Сравнивает подписчиков"""
        if int(self.subscriberCount) >= int(other.subscriberCount):
            return True
        else:
            return False
