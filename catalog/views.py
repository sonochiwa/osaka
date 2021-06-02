from django.shortcuts import render, get_object_or_404
from .models import Category, Product
from cart.forms import CartAddProductForm
# from .forms import SizeForm

def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request, 'catalog/list.html',
                {'category': category,
                'categories': categories,
                'products': products,
                'section': 'catalog'})

def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    # cart_product_form = CartAddProductForm(product.size.all())
    cart_product_form = CartAddProductForm()
    return render(request, 'catalog/detail.html',
        {'product': product,
        'cart_product_form': cart_product_form})

        