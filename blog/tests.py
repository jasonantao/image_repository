from django.test import TestCase
from django.utils import timezone

from blog.models import Post
from users.models import User

# Test Case Suite for Posts: image entries

class BlogTestCasesBase(TestCase):
    @classmethod
    def setUpTestData(cls):
        User.objects.create()
        user = User.objects.get(id=1)
        Post.objects.create(title="test_title", content="lake", author=user)
    
    #  Tests to_string method to output post title
    def test_blog_title_str(self):
        post = Post.objects.get(id=1)
        self.assertEqual(str(post), "test_title")
    
    # Tests default for file extension
    def test_def_file_extension(self):
        post = Post.objects.get(id=1)
        self.assertEqual(post.extension(), "")

    # Tests getting the url for viewing post information
    def test_get_absolute_url(self):
        post = Post.objects.get(id=1)
        self.assertEqual(post.get_absolute_url(), "/post/1/")
    
    # Tests maximum length of post title - a business logic restriction
    def test_post_title_max_allowed(self):
        post = Post.objects.get(id=1)
        field_max_length = post._meta.get_field('title').max_length
        self.assertEqual(field_max_length, 100)
    

