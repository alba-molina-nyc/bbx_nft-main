from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.shortcuts import render, redirect

# Create your models here.
class Item(models.Model):
    file = models.CharField(max_length=250, blank=False)
    name = models.CharField(max_length=100, blank=False)
    details_link = models.CharField(max_length=255)
    description = models.TextField()
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

    def get_absolute_url(self):
        return reverse('main_nft_app:index')

    

class Collection(models.Model):
    collection_choice_text = models.CharField(max_length=200)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)

    
    def __str__(self):
        return self.collection_choice_text










