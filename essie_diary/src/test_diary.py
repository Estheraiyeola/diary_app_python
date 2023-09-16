from unittest import TestCase
from essie_diary.src.diary import *


class TestCaseForDiaryClass(TestCase):

    def setUp(self) -> None:
        self.diary = Diary("Username", "password")

    def test_that_user_can_lock_diary(self):
        self.diary.lock_diary()
        self.assertTrue(self.diary.check_is_locked())

    def test_that_user_can_unlock_diary(self):
        self.diary.lock_diary()
        self.assertTrue(self.diary.check_is_locked())
        self.diary.unlock_diary('password')
        self.assertFalse(self.diary.check_is_locked())

    def test_that_user_can_create_entries(self):
        self.diary.create_entry('title', 'body')
        self.diary.unlock_diary('password')
        self.assertEqual(self.diary.find_entry('1').get_entry(), Entry('1', 'title', 'body').get_entry())

    def test_that_user_can_delete_entry(self):
        self.diary.create_entry('title', 'body')
        self.assertTrue(self.diary.check_is_locked())
        self.diary.unlock_diary('password')
        self.assertEqual(self.diary.find_entry('1').get_entry(), Entry('1', 'title', 'body').get_entry())

        self.diary.create_entry('second title', 'second body')
        self.assertTrue(self.diary.check_is_locked())
        self.diary.unlock_diary('password')
        self.assertEqual(self.diary.find_entry('2').get_entry(), Entry('2', 'second title', 'second body').get_entry())

        self.assertTrue(self.diary.check_is_locked())
        self.diary.delete('1')
        self.assertRaises(ValueError, self.diary.find_entry, '1')

    def test_that_user_can_update_element(self):
        self.diary.create_entry('Title', 'Body')
        self.assertTrue(self.diary.check_is_locked())
        self.diary.unlock_diary('password')
        self.assertEqual(self.diary.find_entry('1').get_entry(), Entry('1', 'Title', 'Body').get_entry())

        self.diary.create_entry('Second title', 'Second body')
        self.assertTrue(self.diary.check_is_locked())
        self.diary.unlock_diary('password')
        self.assertEqual(self.diary.find_entry('2').get_entry(), Entry('2', 'Second title', 'Second body').get_entry())

        self.assertTrue(self.diary.check_is_locked())
        self.diary.update_diary('1', 'is good', 'is also good')
        self.assertEqual(self.diary.find_entry('1').get_entry(),
                         Entry('1', 'Title is good', 'Body is also good').get_entry())
