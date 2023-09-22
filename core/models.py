from django.db import models
import uuid
from django.utils.html import format_html
from django.contrib.auth.models import User

class Profile(models.Model):
    username = models.ForeignKey(User,on_delete=models.CASCADE)
    user_id = models.UUIDField(default=uuid.uuid4())
    bio = models.CharField(max_length=350, null=True)
    profile_image = models.ImageField(upload_to='user-image',default='default.png')
    address = models.CharField(max_length=100, blank=True)
    dtime = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.username.username
    def Image(self):
        return format_html("<img width=90 style='border-radius:5px;' src='{}'>".format(self.profile_image.url))


class Post(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4)
    user = models.CharField(max_length=80)
    image = models.ImageField(upload_to='image-post')
    caption = models.TextField()
    
    dtime = models.DateTimeField(auto_now_add=True)
    no_likes = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.id} - {self.user}"
    
    # def Image(self):
    #     return format_html("<img width=90 style='border-radius:5px;' src='{}'>".format(self.image.url))

class Like(models.Model):
    post_id = models.CharField(max_length=90)
    user = models.CharField(max_length=90)

    def __str__(self) -> str:
        return self.post_id
    
class Comment(models.Model):
    author = models.CharField(max_length=90)
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name='comments')
    user = models.CharField(max_length=90)
    comment = models.TextField()

    def __str__(self) -> str:
        return f"{self.author} comments for {self.user}"