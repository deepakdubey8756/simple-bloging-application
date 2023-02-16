from django.db import models

from django.contrib.auth.models import User
# Create your models here.

STATUS  = (
    (0, "Draft"),
    (1, "Publish")
)

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    image_url = models.TextField(default=None)
    author=models.ForeignKey(User, on_delete=models.CASCADE)
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    created_on = models.DateField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=0)
    image_source = models.CharField(max_length=50, default=None)

    class Meta:
        ordering = ['-created_on']
    

    def __str__(self):
        return self.title
    

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=80)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=False)


    class Meta:
        ordering = ['created_on']
    

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.name)