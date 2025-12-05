from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register, name='register'),

    # Dashboards
    path('dashboard/client/', views.client_dashboard, name='client_dashboard'),
    path('dashboard/farmer/', views.farmer_dashboard, name='farmer_dashboard'),
    path('dashboard/ngo/', views.ngo_dashboard, name='ngo_dashboard'),
    path('dashboard/market/', views.market_dashboard, name='market_dashboard'),
]

