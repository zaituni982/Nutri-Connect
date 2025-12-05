# users/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm
from .models import CustomUser, Order, Crop, Project, Donation

# Registration
def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account created successfully. Please log in.")
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'users/register.html', {'form': form})

# Login with role-based redirect
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            if user.role == 'farmer':
                return redirect('farmer_dashboard')
            elif user.role == 'ngo':
                return redirect('ngo_dashboard')
            elif user.role == 'marketplace':
                return redirect('marketplace_dashboard')
            else:
                return redirect('client_dashboard')
        else:
            messages.error(request, "Invalid username or password.")
    return render(request, 'users/login.html')

# Logout
def logout_view(request):
    logout(request)
    return redirect('login')


# -------------------- DASHBOARDS --------------------

@login_required
def client_dashboard(request):
    orders = Order.objects.filter(client=request.user)
    return render(request, 'users/client_dashboard.html', {'orders': orders})

@login_required
def farmer_dashboard(request):
    crops = Crop.objects.filter(farmer=request.user)
    orders = Order.objects.filter(crop__farmer=request.user)  # Optional: if linked
    return render(request, 'users/farmer_dashboard.html', {'crops': crops, 'orders': orders})

@login_required
def ngo_dashboard(request):
    projects = Project.objects.filter(ngo=request.user)
    donations = Donation.objects.filter(ngo=request.user)
    return render(request, 'users/ngo_dashboard.html', {'projects': projects, 'donations': donations})

@login_required
def market_dashboard(request):
    total_clients = CustomUser.objects.filter(role='client').count()
    total_farmers = CustomUser.objects.filter(role='farmer').count()
    total_orders = Order.objects.count()
    return render(request, 'users/market_dashboard.html', {
        'total_clients': total_clients,
        'total_farmers': total_farmers,
        'total_orders': total_orders
    })

