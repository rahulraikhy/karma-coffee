from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Product, Order, OrderItem

# Create your views here.


def home(request):
    return render(request, 'home.html')


def learn(request):
    return render(request, 'learn.html')


def products_index(request):
    products = Product.objects.all()
    return render(request, 'products/index.html', {
        'products': products
    })


def products_detail(request, product_id):
    product = Product.objects.get(id=product_id)
    return render(request, 'products/detail.html', {
        'product': product
    })


def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
        else:
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)


def cart(request):
    # If user is authenticated, get their cart
    if request.user.is_authenticated:
        cart = Order.objects.filter(user=request.user, status='C').last()
    # If not, fetch the cart from the session
    else:
        cart_id = request.session.get('cart_id')
        cart = Order.objects.filter(
            id=cart_id, status='C').last() if cart_id else None

    return render(request, 'cart.html', {'cart': cart})


def add_to_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    # Fetch the quantity from POST data
    quantity = int(request.POST.get('quantity', 1))

    # If the user is authenticated, associate the cart with the user
    if request.user.is_authenticated:
        order, created = Order.objects.get_or_create(
            user=request.user, status='C')
    # If not, check if there's a cart in the session
    else:
        order_id = request.session.get('cart_id')
        if order_id:
            order = Order.objects.get(id=order_id, status='C')
        else:
            order = Order.objects.create(status='C')
            request.session['cart_id'] = order.id

    # Check if the product already exists in the cart
    order_item, item_created = OrderItem.objects.get_or_create(
        product=product, order=order, quantity=quantity)

    # If the product already exists in the cart, increase its quantity
    if item_created:
        order_item.quantity = quantity
    else:
        order_item.quantity += quantity

        order_item.save()

    messages.success(request, "Item added to cart successfully!")
    return redirect('detail', product_id=product_id)


def update_cart(request, product_id):
    if request.method == 'POST':
        quantity = int(request.POST.get('quantity'))

        if request.user.is_authenticated:
            cart = Order.objects.filter(user=request.user, status='C').last()
        else:
            cart_id = request.session.get('cart_id')
            cart = Order.objects.filter(
                id=cart_id, status='C').last() if cart_id else None

        if not cart:
            messages.warning(request, "No active cart found!")
            return redirect('cart')

        order_item = OrderItem.objects.filter(
            product_id=product_id, order=cart).first()

        if order_item:
            order_item.quantity = quantity
            order_item.save()
            messages.success(request, "Item quantity updated successfully!")
        else:
            messages.warning(request, "Item not found in the cart!")

    return redirect('cart')


def remove_from_cart(request, product_id):
    if request.user.is_authenticated:
        cart = Order.objects.filter(user=request.user, status='C').last()
    else:
        # Handle guest users by fetching the cart from the session
        cart_id = request.session.get('cart_id')
        cart = Order.objects.filter(
            id=cart_id, status='C').last() if cart_id else None

    if not cart:
        messages.warning(request, "No active cart found!")
        return redirect('cart')

    order_item = OrderItem.objects.filter(
        product_id=product_id, order=cart).first()
    if order_item:
        order_item.delete()
        messages.success(request, "Item removed from cart successfully!")
    else:
        messages.warning(request, "Item not found in the cart!")

    return redirect('cart')


def checkout(request):
    cart = Order.objects.filter(user=request.user, status='C').last()
    cart.status = 'P'
    cart.save()
    return redirect('cart')
