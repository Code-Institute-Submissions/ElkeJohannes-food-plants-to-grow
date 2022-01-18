from django.urls import path

from . import views

urlpatterns = [
    path('', views.view_suggestions, name='view_suggestions'),
    path('add/', views.add_suggestion, name='add_suggestion'),
]