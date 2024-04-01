from forum.models import Author
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile

# Create profile signal
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    
    if not instance.is_superuser:
        if created:
            print("Profile Created")

# Save profile signal
@receiver(post_save, sender=User)
def save_profile(sender, instance, created, **kwargs):
    instance.profile.save()
    
    if not instance.is_superuser:
        if created == True:
            pass
        else:
            instance.author.save()
            print("Profile Updated")