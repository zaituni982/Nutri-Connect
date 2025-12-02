from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='logistics-dashboard'),
    path('create/<int:food_id>/', views.create_order, name='create-order'),
]
