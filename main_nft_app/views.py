from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from django.views.generic import ListView
from .models import Item, Collection
from django.shortcuts import render, redirect
from django.core.serializers.json import DjangoJSONEncoder
from django.core import serializers
import json
from json import JSONEncoder
from django.core.serializers import serialize

class LazyEncoder(DjangoJSONEncoder):
    def default(self):
        item = Item.objects.all()
        if isinstance(Item, item):
            return str(Item)
        return super(LazyEncoder, self).default(Item)
    # def get_json(self):
    #     json_metadata = serialize('json', Item.objects.all(), cls=LazyEncoder)
    #     return json_metadata

def get_json_metadata(request,pk):
    item = Item.objects.get(id = pk)
    json_metadata = serialize('json', Item.objects.all(), cls=LazyEncoder)
    return render(
      request, 'json_metadata.html',  {
          "json_metadata": json_metadata,
          "item": item,
      }
    )

    # return render(request, 'json_metadata.html', 
    # {
    #     "json_metadata": json_metadata,
    # }) 


# Create your views here.

class ItemIndex(ListView):
    model = Item
    template_name = 'items/index.html'

    def get_queryset(self):
        queryset = Item.objects.filter(user = self.request.user)
        return queryset

def items_detail(request, pk):
    item = Item.objects.get(id = pk)
    return render(
      request,
      "items/detail.html", {
          "item": item,
      }
    )

def home(request):
    return render(request, 'home.html')




