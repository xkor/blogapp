from django.urls import path
from .views import (
    PostListView,
    post_detail_view,
    TagListView,
    tag_detail_view,
    post_create_view
)

urlpatterns = [
    path('', PostListView.as_view(), name='posts_list_url'),
    path('create/', post_create_view, name='post_create_view'),
    path('post/<str:slug>', post_detail_view, name='post_detail_url'),
    path('tags/', TagListView.as_view(), name='tags_list_url'),
    path('tag/<str:slug>', tag_detail_view, name='tag_detail_url')
]

