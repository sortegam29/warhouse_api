from django.urls import path
from . import views

urlpatterns = [
    path('', views.docs_home, name='docs_home'),
    path('products/', views.docs_products, name='docs_products'),
    path('warehouses/', views.docs_warehouses, name='docs_warehouses'),
    path('inventory/', views.docs_inventory, name='docs_inventory'),
]