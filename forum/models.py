from django.db import models
from django.urls import reverse
# Default User model
from django.contrib.auth.models import User

# Create your models here.

# Model for author information
class Author(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)  
    profile_pic = models.ImageField(default="gator-mascot-head-vector.png", null=True, blank=True)
    is_moderator = models.BooleanField(default=False) 
    bio = models.TextField(max_length=150, blank=True)

    def __str__(self):
        return self.user.username 

# Model for user posts
class UserPost(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True)
    category = models.CharField(max_length=25, null=True) 
    title = models.CharField(max_length=30, null=True)  
    description = models.TextField(max_length=500, null=True) 
    date_created = models.DateTimeField(auto_now_add=True, null=True)  
    gatorpnts = models.IntegerField(null=True)  
    is_open = models.BooleanField(default=True)  

    def __str__(self):
        return self.title  

    # Method to get the absolute URL of the post
    def get_absolute_url(self):
        return reverse('topic-detail', kwargs={
            'pk': self.pk
        })

    # Method to get the count of answers related to the post
    @property
    def answer_count(self):
        return Answer.objects.filter(user_post=self).count()

    # Method to get the count of topic views related to the post
    @property
    def topic_view_count(self):
        return TopicView.objects.filter(user_post=self).count()

# Model for answers to user posts
class Answer(models.Model):
    user_post = models.ForeignKey(UserPost, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete = models.CASCADE) 
    content = models.TextField(max_length=500) 
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    accepted = models.BooleanField(default=False)
    gatorpnts = models.IntegerField(null=True)

    def __str__(self):
        return self.user_post.title  

# Model for blog posts
class BlogPost(models.Model):
    title = models.CharField(max_length=100)  
    slug = models.SlugField(max_length=200, unique=True, null=True, blank=True)  
    content = models.TextField(blank=True, null=True)  
    timestamp = models.DateTimeField(auto_now_add=True)  
    thumbnail = models.ImageField(default="header.jpg", null=True, blank=True)  

    def __str__(self):
        return self.title  

# Model for tracking topic views
class TopicView(models.Model):
    user_post = models.ForeignKey(UserPost, on_delete=models.CASCADE)  
    user = models.ForeignKey(User, on_delete = models.CASCADE)  
   
    def __str__(self):
        return self.user_post.title 

# Model for leaderboard
class Leaderboard(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE) 
    lead_names = models.CharField(max_length=100)  
    tot_gatorpnts = models.IntegerField(default=0, null=True) 
    
    def __str__(self):
        return self.user.username
