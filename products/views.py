from django.shortcuts import render, get_object_or_404
from .models import Category, SubCategory, Product, Review
from datetime import timedelta
from django.utils import timezone
from django.db.models import Avg

# Home View
def home(request):
    products = Product.objects.filter(is_available=True).order_by('-created_at')[:10]
    categories = Category.objects.all()
    SubCategories = SubCategory.objects.all()
    context = {
        'products': products,
        'categories': categories,
        'SubCategories': SubCategories,
    }
    
    return render(request, 'products/home.html', context)

def product_list(request):
    selected_categories = request.GET.getlist('category')
    categories = Category.objects.all()

    if selected_categories:
        products = Product.objects.filter(category__slug__in=selected_categories)
    else:
        products = Product.objects.all()

    for product in products:
        # Mark new
        product.is_new = product.created_at >= timezone.now() - timedelta(days=7)

        # Add average rating
        reviews = product.reviews.all()
        if reviews.exists():
            avg = reviews.aggregate(Avg('rating'))['rating__avg']
            product.avg_rating = round(avg or 0)
        else:
            product.avg_rating = 0

    context = {
        'products': products,
        'categories': categories,
        'selected_categories': selected_categories,
    }
    return render(request, 'products/product_list.html', context)


# Product Detail View
def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    images = product.images.all()
    sizes = product.sizes.all()
    color = product.colors.all()
    reviews = product.reviews.all()
    discounted_price = product.get_discounted_price()

    context = {
        'product': product,
        'images': images,
        'sizes': sizes,
        'color': color,
        'reviews': reviews,
        'is_new': product.created_at >= timezone.now() - timedelta(days=7),
        'avg_rating': round(reviews.aggregate(Avg('rating'))['rating__avg'] or 0),
        'is_available': product.is_available,
        'discounted_price': discounted_price,
    }
    return render(request, 'products/product_detail.html', context)


# Filter by Category
def products_by_category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    products = Product.objects.filter(category=category, is_available=True)
    context = {
        'category': category,
        'products': products,
    }
    return render(request, 'products/products_by_category.html', context)


# Filter by SubCategory
def products_by_subcategory(request, slug):
    subcategory = get_object_or_404(SubCategory, slug=slug)
    products = Product.objects.filter(sub_category=subcategory, is_available=True)
    context = {
        'subcategory': subcategory,
        'products': products,
    }
    return render(request, 'shop/products_by_subcategory.html', context)
