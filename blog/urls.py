from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    UserPostListView
)
from . import views


urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('about/', views.about, name='blog-about'),
    path('imagemedia_post/',views.ImageMedia, name='imagemedia-post'),
    path('audiomedia_post/',views.AudioMedia, name='audiomedia-post'),
    path('multimedia_post/',views.MultiMedia, name='multimedia-post'),
    path('multimedia_view/',views.MultiMediaView, name='multimedia-view'),
    path('audiomedia_view/',views.AudioPostListView.as_view(), name='audiomedia-view'),
    path('imagemedia_view/',views.ImagePostListView.as_view(), name='imagemedia-view'),

]
