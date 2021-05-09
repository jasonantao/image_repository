from django.test import TestCase

from users.models import User

# Test Case Suite for Users
class UserTestCasesBase(TestCase):
    @classmethod
    def setUpTestData(cls):
        User.objects.create()
    
    #  Tests to_string method for user with no username yet
    def test_user_str_no_username(self):
        user = User.objects.get(id=1)
        self.assertEqual(str(user), "")

    #  Tests to_string method for user with username set
    def test_user_str_with_username(self):
        user = User.objects.get(id=1)
        user.username = "jasonantao"
        self.assertEqual(str(user), "jasonantao")
