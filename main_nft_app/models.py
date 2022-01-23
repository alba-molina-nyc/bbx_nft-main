from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Item(models.Model):
    file = models.CharField(max_length=250, blank=False)
    name = models.CharField(max_length=100, blank=False)
    details_link = models.CharField(max_length=255)
    description = models.TextField()
    collection = models.CharField(max_length=250, blank=False)
    properties = models.CharField(max_length=100, blank=False)
    levels = models.CharField(max_length=100, blank=False)
    stats = models.CharField(max_length=100, blank=False)
    unlockable_content = models.BooleanField(default=False)
    explicit_or_sensitive_content = models.BooleanField(default=False)
    supply = models.IntegerField(default=1)
    blockchain = models.CharField(max_length=100, blank=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
        
    def __str__(self):
        return f'{self.name}'











