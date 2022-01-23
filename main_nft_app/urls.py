from django.urls import path
from . import views


urlpatterns = [
# define all app-level URLS in this list
    path('', views.home, name='home'),  
    path("assets/", views.assets, name = "assets"),
    path("assets/create/", views.asset_create, name = "asset_create"),
    path('items/', views.ItemsIndex.as_view(), name='index'),
]
