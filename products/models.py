from django.db import models
from django.urls import reverse
from django.db.models.signals import pre_save

from django.db.models import Q

from .utils import *


class ProductQuerySet(models.query.QuerySet):
    def active(self):
        return self.filter(active=True)

    def featured(self):
        return self.filter(featured=True, active=True)

    def search(self, query):
        lookups = (Q(title__icontains=query) | 
                  Q(description__icontains=query) | 
                  Q(price__icontains=query) | 
                  Q(tag__title__icontains=query)
                  )
        # tshirt, t-shirt, t shirt, red, green, blue,
        return self.filter(lookups).distinct()

class ProductManager(models.Manager):
    def get_queryset(self):
        return ProductQuerySet(self.model, using=self._db)

    def all(self):
        return self.get_queryset().active()

    def featured(self): #Product.objects.featured() 
        return self.get_queryset().featured()

    def get_by_id(self, id):
        qs = self.get_queryset().filter(id=id) # Product.objects == self.get_queryset()
        if qs.count() == 1:
            return qs.first()
        return None

    def search(self, query):
        return self.get_queryset().active().search(query)


class Product(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(blank=True, unique=True)
    brand = models.CharField(max_length=50)
    price = models.FloatField(max_length=120, null=True)
    discount_price = models.FloatField(max_length=120, blank=True, null=True)
    size = models.CharField(max_length=100, blank=True)
    color = models.CharField(max_length=100, blank=True)
    image = models.ImageField(default='default.png', upload_to='image')
    description = models.TextField(blank=True)
    # updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    featured = models.BooleanField(default=False)
    active = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    objects = ProductManager()

    def __str__(self):
        return self.title

    # @property
    # def get_full_name(self):
    #     full_name = self.username
    #     if self.first_name and self.last_name:
    #         full_name = self.first_name + " " + self.last_name
    #     return full_name

    def get_absolute_url(self):
        return reverse('product_detail', kwargs={'slug': self.slug})


def product_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

pre_save.connect(product_pre_save_receiver, sender=Product)
