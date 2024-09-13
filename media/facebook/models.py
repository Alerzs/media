from django.db import models
from django.contrib.auth.models import User

class SocialUser(models.Model):
    user = models.OneToOneField(User , on_delete=models.PROTECT)
    followers = models.ManyToManyField("self")

class Comment(models.Model):
    text = models.TextField()
    user = models.ManyToManyField(SocialUser)

class Post(models.Model):
    user = models.ForeignKey(SocialUser ,on_delete=models.PROTECT)
    text = models.TextField()
    pic = models.ImageField(blank= True , null=True)
    likers = models.ManyToManyField(SocialUser , related_name="liker")
    comment = models.ManyToManyField(Comment , related_name="com")








