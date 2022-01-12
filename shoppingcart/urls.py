from django.urls import path

from . import views

urlpatterns = [
    path('', views.view_cart, name='view_cart'),
    path('add/<plant_id>/', views.add_to_cart, name='add_to_cart' ),
    path('del/<plant_id>/', views.delete_from_cart, name='delete_from_cart' ),
]