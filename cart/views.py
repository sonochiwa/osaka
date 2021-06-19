from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.views.decorators.http import require_POST
from catalog.models import Category, Product
from .cart import Cart
from .forms import CartAddProductForm, OrderForm


@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    sizes = product.sizes.all()
    form = CartAddProductForm(sizes, request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product,
            quantity=cd['quantity'],
            size=cd['size'],
            update_quantity=cd['update'])
    return redirect('cart:cart_detail')

def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart:cart_detail')

def cart_detail(request, **kwargs):
    cart = Cart(request)
    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(
            initial={'quantity': item['quantity'],
                    'update': True})
    # if request.method == 'POST':
    #     for item in cart:
    #         product = item['product']
    #         count = product.count - item['quantity']
    #         if count <= 0:
    #             product.count = 0
    #         else:
    #             product.count = count
    #         product.save()
    #     cart.clear()
    #     return redirect('cart:cart_detail')
    return render(request, 'cart/detail.html', {'cart': cart})

def order(request):
    if request.method == 'POST': 
        order_form = OrderForm(request.POST)
        if order_form.is_valid():
            pass
    else:
        order_form = OrderForm()