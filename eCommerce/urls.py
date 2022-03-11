"""eCommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from carts.views import cart_home
from . import views
urlpatterns = [
    url(r'^$', views.HomePage.as_view(), name='home'),
    url(r'^about$', views.about_page, name='about'),
    url(r'^contact$', views.contact_page, name='contact'),
    url(r'^accounts/', include('accounts.urls')),
    url(r'^products/', include('products.urls')),
    # url(r'^products/', include("products.urls", namespace='products')),
    url(r'^search/', include('search.urls')),
    url(r'^cart/', include('carts.urls')),
    url(r'^admin/', admin.site.urls),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
