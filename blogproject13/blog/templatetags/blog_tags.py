from django import template
register=template.Library()
from blog.models import Post
from django.db.models import Count

@register.simple_tag(name='my_tag')
def total_posts():
    return Post.objects.count()

@register.inclusion_tag('blog/latest.html')
def show_latest_posts(count=4):
    latest_posts=Post.objects.order_by('-publish')[:count]
    return {'latest_posts':latest_posts}

@register.simple_tag
def most_commented_post(count=4):
    return Post.objects.annotate(total_comments=Count('comments')).order_by('-total_comments')[:count]

@register.simple_tag
def most_liked_post(count=4):
    return Post.objects.annotate(total_likes=Count('likes')).order_by('-total_likes')[:count]    
