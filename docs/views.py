from django.shortcuts import render

def docs_home(request):
    return render(request, 'docs/home.html')

def docs_products(request):
    return render(request, 'docs/products.html')

def docs_products_variants(request):
    return render(request, 'docs/product-variants.html')

def docs_warehouses(request):
    return render(request, 'docs/warehouses.html')

def docs_locations(request):
    return render(request, 'docs/locations.html')

def docs_inventory(request):
    return render(request, 'docs/inventory.html')

def docs_movements(request):
    return render(request, 'docs/movements.html')

def docs_batches(request):
    return render(request, 'docs/batches.html')

def docs_authentication(request):
    return render(request, 'docs/authentication.html')