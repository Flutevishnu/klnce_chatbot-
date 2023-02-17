from django.urls import path
from . import views

urlpatterns = [
    path('', views.web),
    path('chat', views.get_data,)
]