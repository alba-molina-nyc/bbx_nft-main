from curses import meta
from importlib.util import LazyLoader
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from django.views.generic import ListView
from .models import Item
from django.shortcuts import render, redirect
from django.core.serializers.json import DjangoJSONEncoder
from django.core.serializers import serialize


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

def ItemsDetail(request, pk):
    item = Item.objects.get(id=pk)
    return render(
        request,
        'detail.html', {
            'item': Item,
    })





