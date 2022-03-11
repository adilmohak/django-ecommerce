from django.shortcuts import render, redirect
from products.models import Product
from .models import Cart
from django.http import JsonResponse


def cart_home(request):
    cart_obj, new_obj = Cart.objects.new_or_get(request)
    return render(request, "carts/home.html", {'cart': cart_obj})


def cart_update(request):
    product_id = request.POST.get('product_id')

    if product_id is not None:
        try:
            product_obj = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            print("Show message to user, product is gone?")
            return redirect("cart")
        cart_obj, new_obj = Cart.objects.new_or_get(request)
        if product_obj in cart_obj.products.all():
            cart_obj.products.remove(product_obj)
            added = False
        else:
            cart_obj.products.add(product_obj) # cart_obj.products.add(product_id)
            added = True
        request.session['cart_items'] = cart_obj.products.count()
        if request.is_ajax():
            return JsonResponse({'added': added})
        # return redirect(product_obj.get_absolute_url())
 
    return redirect("cart")


def items_count(request):
    cart_obj, new_obj = Cart.objects.new_or_get(request)
    counter = cart_obj.products.all().count()
    print(counter)
    return JsonResponse({"counter": counter})
