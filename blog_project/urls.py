from django.urls import path
from .views import (
    HomeView,
    AboutView,
    ContactView,
    BlogPostListView,
    BlogPostDetailView,
    BlogPostCreateView,
    BlogPostUpdateView,
    BlogPostDeleteView
)

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('about/', AboutView.as_view(), name='about'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('posts/', BlogPostListView.as_view(), name='blogpost_list'),
    path('posts/<int:pk>/', BlogPostDetailView.as_view(), name='blogpost_detail'),
    path('posts/new/', BlogPostCreateView.as_view(), name='blogpost_create'),
    path('posts/<int:pk>/edit/', BlogPostUpdateView.as_view(), name='blogpost_update'),
    path('posts/<int:pk>/delete/', BlogPostDeleteView.as_view(), name='blogpost_delete'),
]
