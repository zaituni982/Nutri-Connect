from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import Order
from .forms import OrderForm
from marketplace.models import FoodItem

# Dashboard view for buyers (NGOs / Marketplaces)
@login_required
def dashboard(request):
    # Show orders for the logged-in user
    orders = Order.objects.filter(buyer=request.user)
    return render(request, 'logistics/order_list.html', {'orders': orders})

# Create a new order
@login_required
def create_order(request, food_id):
    # Only NGOs and Marketplaces can create orders
    if request.user.role not in ['ngo', 'marketplace']:
        return redirect('dashboard')

    food = get_object_or_404(FoodItem, id=food_id)
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.buyer = request.user
            order.food_item = food
            order.save()
            return redirect('logistics-dashboard')
    else:
        form = OrderForm()
    return render(request, 'logistics/order_form.html', {'form': form, 'food': food})


