from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.
class Profile(models.Model):
    profile_pic = models.ImageField(upload_to='image/')
    bio = models.CharField(max_length=250)
    username = models.CharField(max_length=100, defualt='Your name')

   
    def save_profile(self):
        self.save()
    
    def delete_profile(self):
        self.delete()

    def posts_profiles(self):
        return self.image_set.all()
    
    def search_profile(cls, name):
        find_user = User.objects.get(name=name)
        return find_user

    def __str__(self):
        return self.name

    

class Images(models.Model):
    image = models.ImageField(upload_to='images/')
    name = models.CharField(max_length=100)
    caption = models.CharField(max_length=250)
    likes = models.IntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()
    
    def all_likes(self):
        return self.likes.count()
    
    def update_image(self):
        self._do_update()

    @classmethod
    def all_images(cls):
        pics = cls.objects.all()
        return pics

    @classmethod
    def user_picture(cls, user):
        user_pic = cls.objects.filter(user=user)
        return user_pic
    
    @classmethod
    def search_image(cls,search_term):
        search_image = cls.objects.filter(name=search_term)
        return search_image
    
    @classmethod
    def delete_post(cls, post_id):
        post = cls.object.filter(pk=post_id)
        post.delete()
    
    @classmethod
    def get_all_posts(cls):
        return cls.objects.order_by()
    

   
    @classmethod
    def get_all_comments(cls):
        return cls.objects.all()
    
    def __str__(self):
        return self.name

class Comments(models.Model):
    image_id = models.ForeignKey(Images, on_delete=models.CASCADE)
    comment = models.TextField(max_length=250)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user
    
    def save_comments(self):
        self.save()
    
    def delete_comments(self):
        self.delete()
    
    @classmethod
    def get_comments(cls, id):
        comments = cls.objects.filter(pic_id=id)
        return comments



class Follow(models.Model):
    follower = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='following')
    followed = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='followers')


    def __str__(self):
        return self.follower

