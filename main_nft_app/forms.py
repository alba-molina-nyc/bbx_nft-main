from django import forms
from django.forms import ModelForm
from .models import Item, Collection

class ItemForm(ModelForm):
    class Meta: 
        model = Item
        fields = '__all__' 
# Creating a form to add an application
form = ItemForm()

# Creating a form to change an existing application
item = Item.objects.get(pk=1)
form = ItemForm(instance=item)


class CollectionForm(ModelForm):
    class Meta:
        model = Collection
        fields = '__all__'

form = CollectionForm()

# Creating a form to change an existing application
collection = Collection.objects.get(pk=1)
form = CollectionForm(instance=collection)