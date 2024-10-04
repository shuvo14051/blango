from django.contrib import admin
from blog.models import Tag, Post, Comment

admin.site.register(Tag)

class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug":("title",)}
    list_display = ('slug', 'published_at')
    

admin.site.register(Post, PostAdmin)

class CommentAdmin(admin.ModelAdmin):
    list_display = ['content', 'creator','content_type', 'object_id', 'content_object']

admin.site.register(Comment, CommentAdmin)