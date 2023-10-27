from django.urls import path
from .views import *

app_name = 'home_app'

urlpatterns = [
    path('', index),
    path('home/<int:int_id>', int_view),
    path('home/<slug:int_id>', slug_view),
]