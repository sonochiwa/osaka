from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.views.decorators.http import require_POST
from catalog.models import Category, Product, Size
from cart.models import Mart, OrderItem, Promo
from .cart import Cart
from .forms import CartAddProductForm, OrderForm
from django.core.exceptions import ObjectDoesNotExist


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
    if request.method == 'POST':
        if not request.user.is_authenticated:
            return redirect('login')
        order_form = OrderForm(request.POST)
        if order_form.is_valid():
            cd = order_form.cleaned_data    
            if len(cart):
                if cd['mart'] or cd['address']:                
                    new_order = order_form.save(commit=False)
                    new_order.user = request.user
                    new_order.save()
                    for item in cart:
                        size = Size.objects.get(size=item['size'])
                        
                        # promo = Promo.objects.get(promo='summersale')
                        try:
                            promo = Promo.objects.get(promo=cd['promo'])  
                        except ObjectDoesNotExist:
                            promo = None
                        if promo:
                            price = item['price'] - item['price'] * promo.percent / 100
                        else: 
                            price = item['price']
                        OrderItem.objects.create(order = new_order, 
                                                product = item['product'], 
                                                price =  price,
                                                quantity = item['quantity'],
                                                size = size)
                    cart.clear()
                    return redirect('cart:cart_detail')
        for item in cart:
            product = item['product']
            count = product.count - item['quantity']
            if count <= 0:
                product.count = 0
            else:
                product.count = count
            product.save()
        cart.clear()
        return redirect('cart:cart_detail')
    else:
        order_form = OrderForm()
        return render(request, 'cart/detail.html', {'cart': cart, 'order_form': order_form})