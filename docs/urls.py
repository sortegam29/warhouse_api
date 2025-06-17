from django.urls import path
from . import views

urlpatterns = [
    path('', views.docs_home, name='docs_home'),
    path('products/', views.docs_products, name='docs_products'),
    path('products-variants/', views.docs_products_variants, name='docs_products_variants'),
    path('warehouses/', views.docs_warehouses, name='docs_warehouses'),
    path('locations/', views.docs_locations, name='docs_locations'),
    path('inventory/', views.docs_inventory, name='docs_inventory'),
    path('movements/', views.docs_movements, name='docs_movements'),
    path('batches/', views.docs_movements, name='docs_batches'),
    path('authentication/', views.docs_authentication, name='docs_authentication'),
]