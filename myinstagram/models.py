from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.
class Profile (models.Model):
    profile_pic = models.ImageField(upload_to='profile/')
    bio = models.CharField(max_length=250, default='My Bio', blank=True)
    name = models.CharField(blank=True, max_length=100)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')

   
    def save_profile(self):
        self.save()
    
    def delete_profile(self):
        self.delete()
    
    @receiver(post_save, sender=User)
    def create_profile(sender, instance, created, **kwargs):
        if created:
            Profile.object.create(user= instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()


    
    @classmethod
    def search_profile(cls, name):
        return cls.objects.filter(user__username__icontians=name).all()


    def __str__(self):
        return f'{self.user.username} Profile'

class Images(models.Model):
    image = models.ImageField(upload_to='images/')
    name = models.CharField(max_length=200, blank=True)
    caption = models.CharField(max_length=250, blank=True)
    likes = models.ManyToManyField(User, related_name= 'like', blank=True)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='images')
    comment = models.CharField(max_length=200)

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()
    
    def all_likes(self):
        return self.likes.count()
    
    @property
    def get_all_comments(self):
        return self.comment.all()
    
    def __str__(self):
        return f'{self.user.name} Image'
    class Meta:
        ordering = ["-pk"]