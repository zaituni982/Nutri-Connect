from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import FoodItem
from .forms import FoodItemForm

# List all food items
@login_required
def home(request):
    foods = FoodItem.objects.all()
    return render(request, 'marketplace/food_list.html', {'foods': foods})

# Only logged-in farmers can add food
@login_required
def add_food(request):
    if request.user.role != 'farmer':
        return redirect('dashboard')

    if request.method == 'POST':
        form = FoodItemForm(request.POST)
        if form.is_valid():
            food = form.save(commit=False)
            food.farmer = request.user
            food.save()
            return redirect('marketplace-home')
    else:
        form = FoodItemForm()
    return render(request, 'marketplace/food_form.html', {'form': form})

# Only the owner farmer can edit
@login_required
def edit_food(request, pk):
    food = get_object_or_404(FoodItem, pk=pk)
    if request.user.role != 'farmer' or food.farmer != request.user:
        return redirect('dashboard')
    if request.method == 'POST':
        form = FoodItemForm(request.POST, instance=food)
        if form.is_valid():
            form.save()
            return redirect('marketplace-home')
    else:
        form = FoodItemForm(instance=food)
    return render(request, 'marketplace/food_form.html', {'form': form})

# Only the owner farmer can delete
@login_required
def delete_food(request, pk):
    food = get_object_or_404(FoodItem, pk=pk)
    if request.user.role != 'farmer' or food.farmer != request.user:
        return redirect('dashboard')
    if request.method == 'POST':
        food.delete()
        return redirect('marketplace-home')
    return render(request, 'marketplace/food_confirm_delete.html', {'food': food})

