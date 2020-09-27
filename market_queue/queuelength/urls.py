from django.urls import path
from . import views

urlpatterns = [
   path('',views.queue_info,name='queue_length'),
    ]