from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
from taggit.managers import TaggableManager


# Create your models here.
class CustomManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status='published')

class Post(models.Model):
    STATUS_CHOICES=(('draft','Draft'),('published','Published'))
    title=models.CharField(max_length=128)
    slug=models.SlugField(max_length=128,unique_for_date='publish')
    author=models.ForeignKey(User,related_name='blog_posts',on_delete=models.CASCADE)
    body=models.TextField()
    publish=models.DateTimeField(default=timezone.now)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    status=models.CharField(max_length=10,default='draft',choices=STATUS_CHOICES)
    tags=TaggableManager()
    objects=CustomManager()

    class Meta:
        ordering=['-publish']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('detail',args=[self.publish.year,self.publish.strftime('%m'),self.publish.strftime('%d'),self.slug])

    def get_absolute_url1(self):
        return reverse('home')

class Comment(models.Model):
    post=models.ForeignKey(Post,on_delete=models.CASCADE,related_name='comments')
    name=models.CharField(max_length=128)
    email=models.EmailField()
    body=models.TextField()
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    active=models.BooleanField(default=True)

    class Meta:
        ordering=['-created']

    def __str__(self):
        return '{} commented on this {}'.format(self.name,self.created)

class Like(models.Model):
    post=models.ForeignKey(Post,related_name='likes',on_delete=models.CASCADE)
    uname=models.CharField(max_length=128)
    email=models.EmailField()
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    active=models.BooleanField(default=True)

    class Meta:
        ordering=['-created']

    def __str__(self):
        return self.uname
