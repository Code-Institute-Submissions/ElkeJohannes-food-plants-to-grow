from django.urls import path

from . import views

urlpatterns = [
    path('', views.all_plants, name='all_plants'),
    path('<category>/', views.all_plants,),
] 