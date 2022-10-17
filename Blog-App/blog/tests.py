from django.contrib.auth import get_user_model
from django.test import TestCase

from .models import Post

# Create your tests here.
class BlogTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(
            username="testuser", email="test@test.com", password="secret"
        )

        cls.post = Post.objects.create(
            title="test post",
            body="test body content",
            author=cls.user,
        )

    def test_post_model(self):
        self.assertEqual(self.post.title, "test post")
        self.assertEqual(self.post.body, "test body content")
        self.assertEqual(self.post.author.username, "testuser")
        self.assertEqual(str(self.post), "test post")
        self.assertEqual(self.post.get_absolute_url(), "/post/1/")
