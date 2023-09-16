class Entry:
    def __init__(self, i_d: str, title: str, body: str):
        self.__i_d = i_d
        self.__title = title
        self.__body = body

    def get_entry(self) -> str:
        return self.__i_d + " " + self.__title + " " + self.__body

    def get_id(self):
        return self.__i_d

    def set_title(self, new_title: str):
        self.__title += " " + new_title

    def set_body(self, new_body: str):
        self.__body += " " + new_body
