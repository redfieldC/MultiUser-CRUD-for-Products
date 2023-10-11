from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Product

@login_required
def create_product(request):
    if request.method == 'POST':
        product = Product(
            name=request.POST['name'],
            price=request.POST['price'],
            quantity=request.POST['quantity'],
            category=request.POST['category'],
            description=request.POST['description'],
            user=request.user
        )
        product.save()
        return redirect('product_list')
    return render(request, 'product/create_product.html')

@login_required
def product_list(request):
    products = Product.objects.filter(user=request.user)
    return render(request, 'product/product_list.html', {'products': products})

@login_required
def edit_product(request, product_id):
    product = get_object_or_404(Product, id=product_id, user=request.user)
    if request.method == 'POST':
        product.name = request.POST['name']
        product.price = request.POST['price']
        product.quantity = request.POST['quantity']
        product.category = request.POST['category']
        product.description = request.POST['description']
        product.save()
        return redirect('product_list')
    return render(request, 'product/edit_product.html', {'product': product})

@login_required
def delete_product(request, product_id):
    product = get_object_or_404(Product, id=product_id, user=request.user)
    product.delete()
    return redirect('product_list')
