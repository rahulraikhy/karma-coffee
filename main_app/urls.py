from django.urls import path
from . import views
from .views import remove_from_cart


urlpatterns = [
    path('', views.home, name='home'),
    path('learn/', views.learn, name='learn'),
    path('products/', views.products_index, name='index'),
    path('products/<int:product_id>/', views.products_detail, name='detail'),
    path('accounts/signup/', views.signup, name='signup'),
    path('cart/', views.cart, name='cart'),
    path('products/<int:product_id>/add/',
         views.add_to_cart, name='add_to_cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('cart/<int:product_id>/remove/',
         views.remove_from_cart, name='remove-from-cart'),
    path('cart/<int:product_id>/update/',
         views.update_cart, name='update-cart'),
    path('create-checkout-session/', views.CreateCheckoutSessionView.as_view(),
         name='create-checkout-session'),
    path('success/', views.checkout_success, name='checkout_success'),
    path('cancel/', views.checkout_cancel, name='checkout_cancel'),
]
