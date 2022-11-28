from django.urls import path
from . import views


urlpatterns = [
    path('',views.home,name="my-home"),
    path('stats/',views.stats,name="stats"),
    
    
]