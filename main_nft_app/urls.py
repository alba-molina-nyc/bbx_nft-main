from django.urls import path
from . import  views

app_name = 'item_urls'
urlpatterns = [
# define all app-level URLS in this list
    path('', views.home, name='home'),  
    path("items/", views.ItemIndex.as_view(), name = "index"),
    path("items/<int:pk>/", views.items_detail, name = "detail"),
    path("items/<int:pk>/metadata/", views.get_json_metadata, name = "json_metadata"),
]
