from django.urls import path
import json
from django.urls import converters

from app.rengong.views import index,data_info
urlpatterns = [
    path('home/', index, name='home'),
    path('data_info/', data_info, name='data_info'),




]