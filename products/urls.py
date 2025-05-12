from django.urls import path
from .views import home, product_list, product_detail, products_by_category, products_by_subcategory


urlpatterns = [
    path('', home, name='home'),
    path('products/', product_list, name='product_list'),
    path('products/<int:pk>/', product_detail, name='product_detail'),
    path('category/<slug:slug>/', products_by_category, name='products_by_category'),
    path('subcategory/<slug:slug>/', products_by_subcategory, name='products_by_subcategory'),
]