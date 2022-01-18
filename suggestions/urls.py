from django.urls import path

from . import views

urlpatterns = [
    path('', views.view_suggestions, name='view_suggestions'),
]