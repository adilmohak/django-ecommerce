from django.conf.urls import url

from .views import (
        cart_home, 
        cart_update,
        items_count
        )

urlpatterns = [
    url(r'^$', cart_home, name='cart'),
    url(r'^update/$', cart_update, name='update'),
    url(r'^items_count/$', items_count, name='items_count'),
]
