from django.contrib.auth import authenticate, login, get_user_model
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render,redirect

from .forms import ContactForm

# def home_page(request):
#     # print(request.session.get("first_name", "Unknown"))
#     # request.session['first_name']
#     context = {
#         "title": "Home | eCommerce"
#     }
#     if request.user.is_authenticated:
#         context["premium_content"] = "Welcome " + request.user.get_full_name
#     return render(request, "home_page.html", context)

from django.views.generic import ListView
from django.shortcuts import render
from products.models import Product
from carts.models import Cart


class HomePage(ListView):
    model = Product
    template_name = "home_page.html"
    
    def get_context_data(self, *args, **kwargs):
        context = super(HomePage, self).get_context_data(*args, **kwargs)
        cart_obj, new_obj = Cart.objects.new_or_get(self.request)
        context['cart'] = cart_obj
        return context


def about_page(request):
    context = {
        "title": "About Page"
    }
    return render(request, "about_page.html", context)

def contact_page(request):
    contact_form = ContactForm(request.POST or None)
    context = {
        "title": "Contact",
        "form": contact_form
    }
    if contact_form.is_valid():
        print(contact_form.cleaned_data)
        if request.is_ajax():
            return JsonResponse({"message": "Thank you for your submission"})

    if contact_form.errors:
        errors = contact_form.errors.as_json()
        if request.is_ajax():
            return HttpResponse(errors, status=400, content_type='application/json')

    # if request.method == "POST":
    #     #print(request.POST)
    #     print(request.POST.get('fullname'))
    #     print(request.POST.get('email'))
    #     print(request.POST.get('content'))
    return render(request, "contact_page.html", context)
