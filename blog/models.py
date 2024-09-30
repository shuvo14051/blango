from django.db import models
from django.conf import settings
# from django.contrib.auth.models import User # another way


class Tag(models.Model):
    value = models.TextField(max_length=100)

    def __str__(self):
        return self.value
    
class Post(models.Model):
    # author = models.ForeignKey(User, on_delete=models.PROTECT) # another way
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    published_at = models.DateTimeField(blank=True, null=True)
    title = models.TextField(max_length=100)
    slug = models.SlugField()
    summary = models.TextField(max_length=500)
    context = models.TextField()
    tags = models.ManyToManyField(Tag, related_name = 'posts')

    def __str__(self):
        return self.title

