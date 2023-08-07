import stripe
import json
from django.shortcuts import get_object_or_404
from django.views import View
from django.conf import settings
from django.http import JsonResponse
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Product, Order, OrderItem, Review, User

from .forms import ReviewForm

stripe.api_key = settings.STRIPE_API_KEY_HIDDEN

YOUR_DOMAIN = 'http://localhost:8000'

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

    # id_list = product.review.all().values_list('id')
    # reviews_for_product = Review.objects.filter(id__in=id_list)
    if request.user.is_authenticated:
        user = request.user
        delivered_orders = Order.objects.filter(user=user, status='D', orderitem__product=product)

        if delivered_orders.exists():
            review_form = ReviewForm()
        else:
            review_form = None

    reviews_for_product = product.reviews.all()

    return render(request, 'products/detail.html', {
        'product': product, 
        'review_form': review_form,
        'reviews': reviews_for_product
    })


def add_review(request, product_id):
    form = ReviewForm(request.POST)

    if form.is_valid():
        product = Product.objects.get(id=product_id)
        # user = User.objects.get(id=user_id)
        user_id = request.user.id

        new_review = form.save(commit=False)
        new_review.product = product
        new_review.user_id = user_id
        new_review.save()

    return redirect('detail', product_id)
        


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
    pub_key = 'pk_test_51NcAplKTTNpybu1oBa9m6XeqC3TGQOCw0EYJQhJJHLCf3eC996sIC8pdtr7NSw3GBDYpPZdEEJIA4TW7FYZDvCD200HwjTkail'
    print('Hello')
    print(pub_key)
    cart = Order.objects.filter(user=request.user, status='C').last()
    cart.save()
    return render(request, 'checkout.html', {'cart': cart, 'pub_key': pub_key})


class CreateCheckoutSessionView(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        cart = Order.objects.filter(user=request.user, status='C').last()

        line_items = []
        for item in cart.orderitem_set.all():
            line_items.append({
                'price_data': {
                    'currency': 'usd',
                    # Stripe expects amounts in cents
                    'unit_amount': int(item.product.price * 100),
                    'product_data': {
                        'name': item.product.name,
                        # Add images if you have
                    },
                },
                'quantity': item.quantity,
            })

        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=line_items,
            mode='payment',
            success_url=YOUR_DOMAIN +
            '/success/?session_id={CHECKOUT_SESSION_ID}',
            cancel_url=YOUR_DOMAIN + '/cancel/',
        )

        # Replace placeholder with actual id
        checkout_session.success_url = checkout_session.success_url.replace(
            '{CHECKOUT_SESSION_ID}', checkout_session.id)

        # Store the session id in the order
        cart.session_id = checkout_session.id
        cart.save()

        return JsonResponse({
            'id': checkout_session.id
        })


def checkout_success(request):
    # Extract session_id from the URL
    session_id = request.GET.get('session_id')

    # Retrieve the session
    session = stripe.checkout.Session.retrieve(session_id)

    # Retrieve the order associated with this session
    order = Order.objects.get(session_id=session_id)

    # Update order status if the payment was successful
    if session.payment_status == 'paid':
        order.status = 'P'
        order.save()

    return render(request, 'success.html')


def checkout_cancel(request):
    return render(request, 'cancel.html')
