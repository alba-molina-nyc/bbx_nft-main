from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from django.views.generic import ListView
from .models import Item
from django.shortcuts import render, redirect
import json
# Create your views here.

def home(request):
    return render(request, 'home.html')

def assets(request):
    return render(request, 'projects/assets.html')

def asset_create(request):
    return render(request, 'asset_create.html')


class ItemsIndex(ListView):
    model = Item
    template_name = 'index.html'
    print(Item)



    # def get_queryset(self):
    #     queryset = Item.objects
    #     return queryset.filter(user=self.request.user)