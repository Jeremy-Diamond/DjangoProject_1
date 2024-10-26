from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Goal(models.Model):
    title = models.CharField(max_length=75)
    details = models.TextField()
    completed = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self.title.replace(' ', '-')
        super().save(*args, **kwargs)
    image = models.ImageField(default='default.jpg', blank=True)
    owner = models.ForeignKey('auth.User', on_delete=models.CASCADE, default=None)
    

    def __str__(self):
        return self.title
