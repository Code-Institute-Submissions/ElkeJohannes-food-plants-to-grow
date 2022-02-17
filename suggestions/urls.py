from django.urls import path
from . import views


urlpatterns = [
    path('', views.view_suggestions, name='view_suggestions'),
    path('add/', views.add_suggestion, name='add_suggestion'),
    path('upvote/<suggestion_id>', views.upvote_suggestion,
         name='upvote_suggestion'),
    path('edit/<suggestion_id>', views.edit_suggestion,
         name='edit_suggestion'),
    path('delete/<suggestion_id>', views.delete_suggestion,
         name='delete_suggestion'),
]
