from django.urls import path
from .views import SocialMediaPostList

urlpatterns = [
    path('posts/', SocialMediaPostList.as_view(), name='social-media-posts'),
]