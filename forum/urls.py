from django.urls import path

from .import views

# Put your url redirects here
urlpatterns = [
    path('', views.home, name='home'),
    path('user-post/', views.userPost, name='user-post'),
    path('topic/<int:pk>/', views.postTopic, name='topic-detail'),
    path('search-result/', views.searchView, name='search-result'),
    path('user-dashboard/', views.userDashboard, name='user-dashboard'),
    path('blog/', views.blogListView, name='blog'),
    path('article/<slug:slug>/', views.blogDetailView, name='article-detail'),
    path('accept-answer/<int:pk>/', views.accept_answer, name='accept_answer'),
    path('close-post/<int:pk>/', views.close_post, name='close-post'),
    path('open-post/<int:pk>/', views.open_post, name='open-post'),
]