from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='marketplace-home'),
    path('add/', views.add_food, name='add-food'),
    path('edit/<int:pk>/', views.edit_food, name='edit-food'),
    path('delete/<int:pk>/', views.delete_food, name='delete-food'),
]
