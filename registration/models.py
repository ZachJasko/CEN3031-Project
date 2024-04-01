from django.db import models
from django.contrib.auth.models import User
# Create your models here.


# Extending User Model Using a One-To-One Link
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    avatar = models.ImageField(default='anonUser.png', upload_to='static\images')
    bio = models.TextField()

    def __str__(self):
        return self.user.username