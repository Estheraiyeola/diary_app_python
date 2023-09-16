from unittest import TestCase
from essie_diary.src.diaries import *


class TestCaseForClassDiaries(TestCase):
    def setUp(self) -> None:
        self.diaries = Diaries()

    def test_that_a_diary_can_be_added_to_a_list_of_diaries(self):
        self.diaries.add('username', 'password')
        self.assertEqual(self.diaries.find_by_username('username').get_username(), 'username')

    def test_that_a_diary_can_be_deleted_from_the_list_of_diaries(self):
        self.diaries.add('username', 'password')
        self.assertEqual(self.diaries.find_by_username('username').get_username(), 'username')

        self.diaries.add('Username', 'Password')
        self.assertEqual(self.diaries.find_by_username('Username').get_username(), 'Username')

        self.diaries.delete('Username', 'Password')
        self.assertRaises(ValueError, self.diaries.find_by_username, 'Username')

        self.diaries.delete('Username', 'Password')
        self.assertRaises(ValueError, self.diaries.find_by_username, 'Username')

    def test_that__list_of_diaries_have_unique_users(self):
        self.diaries.add('username', 'password')
        self.assertEqual(self.diaries.find_by_username('username').get_username(), 'username')

        self.diaries.add('Username', 'Password')
        self.assertEqual(self.diaries.find_by_username('Username').get_username(), 'Username')

        self.assertRaises(ValueError, self.diaries.add, 'username', 'password')
