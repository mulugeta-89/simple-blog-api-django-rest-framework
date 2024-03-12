from django.urls import path
from . import views
urlpatterns = [
    path("blogposts/", views.BlogPostListViewCreate.as_view(), name="blogpost-view-create"),
    path("blogposts/", views.BlogPostList.as_view(), name="blog-post-list"),
    path("blogposts/<int:pk>", views.BlogPostRetrieveUpdateDestory.as_view(), name="retrieve-update-destroy"),
    
]