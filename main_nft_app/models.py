from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.shortcuts import render, redirect

# Create your models here.
class Collection(models.Model):
    collection_choice_text = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    
    def __str__(self):
        return f'collection {self.collection_choice_text} by {self.user.id}'

    def get_absolute_url(self):
        return reverse('items:detail', kwargs={'pk': self.item.id})

class Item(models.Model):
    BLOCKCHAIN = (
        ('E', 'Ethereum'),
        ('P', 'Polygon'),
    )
    file = models.CharField(max_length=250, blank=False)
    name = models.CharField(max_length=100, blank=False)
    details_url = models.URLField(max_length=200)
    description = models.TextField()
    properties = models.CharField(max_length=100, blank=False)
    levels = models.CharField(max_length=100, blank=False)
    stats = models.CharField(max_length=100, blank=False)
    unlockable_content = models.BooleanField(default=False)
    explicit_or_sensitive_content = models.BooleanField(default=False)
    supply = models.IntegerField(default=1)
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE)
    blockchain = models.CharField(
        max_length=1,
        choices=BLOCKCHAIN)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
        
    def __str__(self):
        return f'{self.name}'

    def get_absolute_url(self):
        return reverse('detail', kwargs={'app_id': self.id})

    












