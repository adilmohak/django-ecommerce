from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    url(r'^$', views.ProductListView.as_view(), name='products'),
    # path('<str:slug>/', views.ProductDetailView.as_view(), name='product_detail'),
    url(r'^(?P<slug>[\w-]+)/$', views.ProductDetailView.as_view(), name='product_detail'),
]
