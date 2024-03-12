from django.test import TestCase
from rest_framework.test import APITestCase
from .models import BlogPost
from django.urls import reverse
from rest_framework import status
# Create your tests here.
class BlogPostApiTest(APITestCase):
    def setUp(self):
        self.blog = BlogPost.objects.create(title="mula", content="this is mulugeta hailegnaw")
    def test_get_blog_posts(self):
        response = self.client.get("/blogposts/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)
    def test_create_blog_post(self):
        sample = { "title": "nelson", "content": "this is nelson brandy"}
        response = self.client.post("/blogposts/", sample)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(BlogPost.objects.count(), 2)
    def test_update_blog_post(self):
        url = reverse("retrieve-update-destroy", args=[self.blog.id])
        data = {"title": "updated title", "content": "updated content"}
        response = self.client.put(url, data, format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.blog.refresh_from_db()
        self.assertEqual(self.blog.title, "updated title")
        self.assertEqual(self.blog.content, "updated content")
    def test_delete_blog_post(self):
        url = reverse("retrieve-update-destroy", args=[self.blog.id])
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(BlogPost.objects.count(),0)
    def test_filter_blog_by_title(self):
        url = reverse("blog-post-list")
        response = self.client.get(url, {"title": "mula"})

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["title"], "mula")

    

