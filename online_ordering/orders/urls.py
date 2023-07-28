from django.urls import path
from .views import register_view, order_create, order_confirmation
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
    path('register/', register_view, name='register'),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('order/', order_create, name='order'),  # if the function that handles this URL is order_create, the name should be 'order'
    path('order-history/', views.order_history_view, name='order-history'),
    path('order-tracking/<int:order_id>/', views.order_tracking_view, name='order-tracking'),
    path('contact-support/', views.contact_support_view, name='contact-support'),
    path('contact/', views.contact_view, name='contact'),
    path('order-create/', views.order_create, name='order_create'),  # this one should be 'order_create'
    path('order-confirmation/<int:order_id>/', order_confirmation, name='order_confirmation'),
    path('order-success/', views.order_success_view, name='order_success'),
    path('accounts/profile/', views.dashboard, name='profile'),
    path('', views.home, name='home'),
]
