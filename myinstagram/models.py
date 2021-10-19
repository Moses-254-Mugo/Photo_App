from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    image = models.ImageField(upload_to ='profile_pics')
    

    def __str__(self):
        return f'{self.user.username} Profile'
    

class Post(models.Model):
    author = models.ForeignKey('auth.user',on_delete=models.CASCADE,related_name='author')
    image = models.ImageField(blank = True,null=True)
    caption = models.TextField()
    liked = models.ManyToManyField(User, default=None,blank= True,related_name='liked')

    
    def __str__(self):
        return f'{self.author.username}'
   
    @classmethod
    def search_category(cls,search):
        searches = cls.objects.filter(author__username__icontains = search)
        return searches
    @property
    def num_likes(self):
        return self.liked.all().count

   

    

class Comment(models.Model):
    post = models.ForeignKey('Post',related_name='comments',on_delete=models.CASCADE)
    comment = models.TextField()
    name = models.CharField(max_length=50)
   
  

    def __str__(self):
        return f'{self.post.caption,self.name}'
    
LIKE_CHOICES = (
    ('Like','Like'),
    ('Unlike','Unlike'),
)
class Like(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    value = models.CharField(choices=LIKE_CHOICES,default='Like',max_length=10)
    def __str__(self):
        return str(self.post)

        