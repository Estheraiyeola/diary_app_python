from essie_diary.src.entry import Entry


class Diary:
    def __init__(self, username: str, password: str):
        self.__username = username
        self.__password = password
        self.is_locked = False
        self.__entries = []

    def lock_diary(self) -> None:
        self.is_locked = True

    def check_is_locked(self) -> bool:
        return self.is_locked

    def unlock_diary(self, password: str) -> None:
        self.validate(password)
        self.is_locked = False

    def validate(self, password: str) -> None:
        if self.__password != password:
            raise ValueError('Invalid password')

    def create_entry(self, title: str, body: str) -> None:
        entry = Entry(self.generate_id(), title, body)
        self.__entries.append(entry)
        self.lock_diary()

    def find_entry(self, i_d: str) -> Entry:
        for entry in self.__entries:
            if entry.get_id() == i_d:
                return entry
            self.lock_diary()
        raise ValueError('Entry not found')

    def generate_id(self) -> str:
        return str(len(self.__entries) + 1)

    def delete(self, i_d: str) -> None:
        entry = self.find_entry(i_d)
        self.__entries.remove(entry)

    def update_diary(self, i_d: str, new_title: str, new_body: str) -> None:
        self.find_entry(i_d).set_title(new_title)
        self.find_entry(i_d).set_body(new_body)

    def get_username(self) -> str:
        return self.__username

    def get_password(self):
        return self.__password

    def get_user(self):
        return self.__username + " " + self.__password
