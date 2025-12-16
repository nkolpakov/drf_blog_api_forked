from django.urls import reverse, resolve
from django.test import SimpleTestCase

from comment.api import views

# Create your tests here.


class UrlsTest(SimpleTestCase):

    def test_comment_list(self):
        path = reverse('comment:api:list', args=[1])
        self.assertEqual(resolve(path).func.view_class, views.CommentsList)
        self.assertNotEqual(resolve(path).func.view_class, views.CommentCreate)

    def test_comment_create(self):
        path = reverse('comment:api:create')
        self.assertEqual(resolve(path).func.view_class, views.CommentCreate)
        self.assertNotEqual(resolve(path).func.view_class, views.CommentsList)
    
    def test_comment_create(self):
        path = reverse('comment:api:update-delete', args=[1])
        self.assertEqual(resolve(path).func.view_class, views.CommentUpdateDelete)
        self.assertNotEqual(resolve(path).func.view_class, views.CommentsList)