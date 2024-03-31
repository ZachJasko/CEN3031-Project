from django.urls import path

from .import views

urlpatterns = [
    path('', views.home, name='home'),
    path('user-post/', views.userPost, name='user-post'),
    path('topic/<int:pk>/', views.postTopic, name='topic-detail'),
    path('accept-job/<int:pk>/', views.acceptJobPosting, name='accept_job_posting'),
    path('search-result/', views.searchView, name='search-result'),
    path('user-dashboard/', views.userDashboard, name='user-dashboard'),
    path('blog/', views.blogListView, name='blog'),
    path('article/<slug:slug>/', views.blogDetailView, name='article-detail'),
]
