from django.shortcuts import render, get_object_or_404
from .models import Category, Product
from cart.forms import CartAddProductForm
from .forms import ReviewForm
# from .forms import SizeForm

def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    filter_by = request.GET.get('filter_by')
    print(filter_by)
    if filter_by:
        if filter_by == 'gt':
            products = products.order_by('price')
        else:
            products = products.order_by('-price')

    return render(request, 'catalog/list.html',
                {'category': category,
                'categories': categories,
                'products': products,
                'section': 'catalog'})

def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    reviews = product.reviews.order_by('-date')
    cart_product_form = CartAddProductForm()
    if request.method == 'POST':
        review_form = ReviewForm(request.POST)
        if review_form.is_valid():
            new_comment = review_form.save(commit=False)
            new_comment.product = product
            new_comment.author = request.user
            new_comment.save()
    else:
        review_form = ReviewForm()
    return render(request, 'catalog/detail.html',
        {'product': product, 'reviews': reviews, 
        'review_form': review_form,
        'cart_product_form': cart_product_form})
    

        