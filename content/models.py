from django.db import models
from django.contrib.auth.models import User

class Blog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200)
    content = models.TextField(blank=True)
    content2 = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title + ' - por ' + self.user.username

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='comments')  # Relación con Blog
    content = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    likes = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.blog.title} - por {self.user.username}"  # Retorna los primeros 50 caracteres
