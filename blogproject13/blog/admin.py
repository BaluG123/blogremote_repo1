from django.contrib import admin
from blog.models import Post,Comment,Like

class PostAdmin(admin.ModelAdmin):
    list_display=['title','slug','author','body','publish','created','updated','status']
    list_filter=('status','created')
    prepopulated_fields={'slug':('title',)}
    search_fields=('title','body')
    raw_id_fields=('author',)
    date_hierarchy='publish'

class CommentAdmin(admin.ModelAdmin):
    list_display=['post','name','email','body','created','updated','active']
    list_filter=('created','active')
    date_hierarchy='created'

class LikeAdmin(admin.ModelAdmin):
    list_display=['post','uname','email','created','updated','active']
    list_filter=('created','active')
    date_hierarchy='created'

# Register your models here.
admin.site.register(Post,PostAdmin)
admin.site.register(Comment,CommentAdmin)
admin.site.register(Like,LikeAdmin)
