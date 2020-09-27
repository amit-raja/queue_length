from django.urls import path
from . import views

urlpatterns = [
   path('',views.queue_list,name='queue_list'),
    ]
