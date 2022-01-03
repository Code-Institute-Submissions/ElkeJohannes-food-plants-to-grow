from django.urls import path

from . import views

urlpatterns = [
    path('', views.all_plants, name='all_plants'),
    path('<int:plant_id>/', views.single_plant, name='single_plant')
] 