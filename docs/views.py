from django.shortcuts import render

def docs_home(request):
    return render(request, 'docs/home.html')

def docs_products(request):
    return render(request, 'docs/products.html')

def docs_warehouses(request):
    return render(request, 'docs/warehouses.html')

def docs_inventory(request):
    return render(request, 'docs/inventory.html')