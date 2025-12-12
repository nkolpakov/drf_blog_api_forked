from django.contrib.auth import get_user_model
from django.test import TestCase

from blog.models import Blog, Category

# Create your tests here.


class BlogTest(TestCase):

    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(phone="98912888888")
        self.blog = Blog.objects.create(
            author=self.user, 
            title='title-test-1',
            body='title-test-1', 
            summary="summary-test-1",
            special=True,
            status='p',
            visits=1,
        )

    def test_str_method(self):
        self.assertEqual(str(self.blog), f"{self.user.first_name} {self.blog.title}")
        self.assertNotEqual(str(self.blog), f"{self.user.first_name}")

    def test_fields_blog_model(self):
        self.assertEqual(f"{self.blog.title}", "title-test-1")
        self.assertTrue(self.blog.special, True)
        self.assertNotEqual(self.blog.status, 'd')

    def test_is_generate_slug(self):
        self.assertIsNotNone(self.blog.slug)

    def test_the_profile_of_the_author_of_the_blog(self):
        self.assertEqual(self.blog.author.phone, "98912888888")
        self.assertNotEqual(self.blog.author.phone, "99999999999")


class CategoryTest(TestCase):

    def setUp(self) -> None:
        self.category1 = Category.objects.create(
            title="category test 1",
            slug="category-test-1",
            status=True,
        )
        self.category2 = Category.objects.create(
            parent=self.category1,
            title="category test 2",
            slug="category-test-2",
            status=True,
        )

    def test_str_method(self):
        self.assertEqual(str(self.category1), self.category1.title)
        self.assertEqual(str(self.category2), self.category2.title)

    def test_fields_category1_model(self):
        self.assertEqual(f"{self.category1.title}", "category test 1")
        self.assertEqual(self.category1.slug, "category-test-1")
        self.assertNotEqual(self.category1.status, False)

    def test_fields_category2_model(self):
        self.assertEqual(f"{self.category2.title}", "category test 2")
        self.assertEqual(self.category2.slug, "category-test-2")
        self.assertNotEqual(self.category2.status, False)

    def test_parent_category(self):
        self.assertIsNone(self.category1.parent)
        self.assertEqual(str(self.category2.parent), self.category1.title)