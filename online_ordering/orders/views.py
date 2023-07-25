from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.shortcuts import render, redirect
from .models import Product, Order, Contact
from django.core.mail import send_mail
from django.contrib import messages
from .forms import ContactForm, OrderForm


def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

@login_required
def order_history_view(request):
    orders = Order.objects.filter(user=request.user)
    return render(request, 'order_history.html', {'orders': orders})

@login_required
def order_tracking_view(request, order_id):
    order = Order.objects.get(id=order_id, user=request.user)
    return render(request, 'order_tracking.html', {'order': order})

@login_required
def contact_support_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your message has been sent. Our team will get back to you soon.')
            return redirect('home')  # or where you want to redirect the user after a successful form submission
    else:
        form = ContactForm()
    return render(request, 'contact_support.html', {'form': form})

def order_create(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            # Check if the user is authenticated
            if request.user.is_authenticated:
                # Save the order
                order = form.save(commit=False)
                order.user = request.user
                order.save()
                return redirect('order_success')
            else:
                # Handle guest user
                # Retrieve guest order count from session or initialize to 0
                guest_order_count = request.session.get('guest_order_count', 0)
                # If the guest user has already made 2 orders, redirect to registration
                if guest_order_count >= 2:
                    return redirect('register')
                else:
                    # Increment the order count for guest user
                    request.session['guest_order_count'] = guest_order_count + 1
                    # Save the order with user=None
                    order = form.save(commit=False)
                    order.user = None
                    order.save()
                    return redirect('order_success')
    else:
        form = OrderForm()
    return render(request, 'order_create.html', {'form': form})

def order_confirmation(request, order_id):
    # Retrieve the order using the order_id
    order = Order.objects.get(id=order_id)

    # Render the order confirmation page
    return render(request, 'order_confirmation.html', {'order': order})

def order_success_view(request):
    return render(request, 'order_success.html')

@login_required
def dashboard(request):
    return render(request, 'accounts/profile.html')

def home(request):
    return render(request, 'home.html')
