from typing import ItemsView
from django.contrib import admin

from .models import Collection, Item

# Register your models here.
admin.site.register(Item)
admin.site.register(Collection)