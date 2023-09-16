from essie_diary.src.diary import *


class Diaries:
    def __init__(self):
        self.is_empty = False
        self.__diaries = []

    def check_is_empty(self):
        return self.is_empty

    def add(self, username: str, password: str) -> None:
        self.check_if_user_exists(username)
        diary = Diary(username, password)
        self.__diaries.append(diary)

    def find_by_username(self, username: str) -> Diary:
        for diary in self.__diaries:
            if diary.get_username() == username:
                return diary
        raise ValueError('User not found')

    def delete(self, username: str, password: str) -> None:
        for diary in self.__diaries:
            if diary.get_username() == username and diary.get_password() == password:
                self.__diaries.remove(diary)

    def check_if_user_exists(self, username: str) -> None:
        for diary in self.__diaries:
            if diary.get_username() == username:
                raise ValueError('Username already exists. Get a Unique username')
