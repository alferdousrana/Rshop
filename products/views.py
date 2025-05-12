from django.shortcuts import render, get_object_or_404
from .models import Category, SubCategory, Product, Review

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


#Product List View
def product_list(request):
    products = Product.objects.filter(is_available=True)
    categories = Category.objects.all()
    
    context = {
        'products': products,
        'categories': categories,
        
    }
    return render(request, 'products/product_list.html', context)


# Product Detail View
def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    images = product.images.all()
    sizes = product.sizes.all()
    colors = product.colors.all()
    reviews = product.reviews.filter(is_verified=True)

    context = {
        'product': product,
        'images': images,
        'sizes': sizes,
        'colors': colors,
        'reviews': reviews,
    }
    return render(request, 'products/single_product.html', context)


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
