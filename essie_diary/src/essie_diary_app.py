from essie_diary.src.diaries import *


class DiaryApp:
    def __init__(self):
        self.username = None
        self.diaries = Diaries()

    def welcome_page(self) -> None:
        print("Welcome to Olofofo Diary place")
        self.welcome_menu()

    def welcome_menu(self) -> None:
        userinput = input("""
        ===================================
                    WELCOME
        ===================================
        SELECT:
        1 -> Login
        2 -> Sign Up
        3 -> Exit
        """)
        match userinput:
            case '1':
                self.login()
            case '2':
                self.sign_up()
            case '3':
                self.exit()
            case _:
                self.welcome_menu()

    def login(self):
        try:
            print("""
            ===================================
                            LOGIN
            ===================================
            """)
            username = input('Enter your username: ')
            password = input('Enter your password: ')
            if self.diaries.find_by_username(username).get_password() == password:
                self.main_menu()
            else:
                self.welcome_menu()
        except ValueError:
            print('Diary not found')
            self.welcome_menu()

    def sign_up(self):
        try:
            print("""
            ===================================
                        SIGN UP
            ===================================
            """)
            username = input('Enter your username: ')
            password = input('Enter your password: ')
            self.diaries.add(username, password)
            self.username = username
            self.login()
        except ValueError:
            print('Invalid input')
            self.welcome_menu()

    @staticmethod
    def exit():
        return exit(0)

    def main_menu(self):
        userinput = input("""
        ===============================
                MAIN MENU
        ===============================
        SELECT AN OPTION
        1. ADD ENTRY
        2. UPDATE ENTRY
        3. DELETE ENTRY
        4. FIND ENTRY
        5. LOCK DIARY
        6. LOG OUT 
        """)
        match userinput:
            case '1':
                self.add_entry()
            case '2':
                self.update_entry()
            case '3':
                self.delete_entry()
            case '4':
                self.find_entry()
            case '5':
                self.lock_diary()
            case '6':
                self.log_out()
            case _:
                print("Invalid input")
                self.welcome_menu()

    def add_entry(self):
        try:
            print("""
            ===================================
                        ADD ENTRY
            ===================================
            """)
            title = input('Enter your title: ')
            body = input('Enter your body: ')
            self.diaries.find_by_username(self.username).create_entry(title, body)
            self.diaries.find_by_username(self.username).lock_diary()
            self.main_menu()
        except ValueError:
            print('Invalid input')
            self.main_menu()

    def update_entry(self):
        try:
            self.unlock()
            print("""
            ===================================
                        UPDATE ENTRY
            ===================================
            """)
            i_d = input('Enter your id: ')
            title = input('Enter your title: ')
            body = input('Enter your body: ')
            self.diaries.find_by_username(self.username).update_diary(i_d, title, body)
            self.main_menu()
        except ValueError:
            print('Invalid input')
            self.main_menu()

    def delete_entry(self):
        try:
            self.unlock()
            print("""
            ===================================
                        DELETE ENTRY
            ===================================
            """)
            i_d = input('Enter your id: ')
            self.diaries.find_by_username(self.username).delete(i_d)
        except ValueError:
            print('Entry not found')

    def find_entry(self):
        try:
            self.unlock()
            print("""
            ===================================
                        FIND ENTRY
            ===================================
            """)
            i_d = input('Enter your id: ')
            print(self.diaries.find_by_username(self.username).find_entry(i_d).get_entry())
            self.main_menu()
        except ValueError:
            print('Entry not found')
            self.main_menu()

    def lock_diary(self):
        try:
            self.diaries.find_by_username(self.username).lock_diary()
            userinput = input("""
            ==================================
                    DIARY LOCKED
            ==================================
            SELECT AN OPTION
            1. Unlock
            2. Logout
            3. Exit
            """)
            match userinput:
                case '1':
                    self.unlock()
                    self.main_menu()
                case '2':
                    self.log_out()
                case '3':
                    self.exit()
                case _:
                    self.welcome_menu()
        except ValueError:
            print('Invalid input')
            self.lock_diary()

    def log_out(self):
        self.welcome_menu()

    def unlock(self):
        try:
            password = input('Enter your password to unlock: ')
            self.diaries.find_by_username(self.username).unlock_diary(password)
        except ValueError:
            print('Invalid password')
            self.unlock()


app = DiaryApp()
app.welcome_page()
