from django.shortcuts import render
from django.views import View
from .models import ProductBottles,Products
import json
from datetime import datetime
# Create your views here.


class HomePage(View):

    def get(self, request, *args, **kwargs):
        products = []
        for product in Products.objects.all():
            products.append({
                "name":product.name,
                "description":product.description,
                "first_image":product.images.first().image.url,
                "image_urls":json.dumps([img.image.url for img in product.images.all()]),
                "bottles":json.dumps([{
                    "bottle_size_ml":bottle.bottle_size_ml,
                    "bottle_price":bottle.price,
                    "price_after_discount":bottle.price_after_discount
                } for bottle in product.bottles.all()])
            })
        return render(request, 'index.html', {"products":products})
    

# new arrival filter : product added in this month
class NewArrivals(View):
    def get(self, request, *args, **kwargs):
        products = []
        for product in Products.objects.filter(created_at__month=datetime.now().date().month):
            products.append({
                "name":product.name,
                "description":product.description,
                "first_image":product.images.first().image.url,
                "image_urls":json.dumps([img.image.url for img in product.images.all()]),
                "bottles":json.dumps([{
                    "bottle_size_ml":bottle.bottle_size_ml,
                    "bottle_price":bottle.price,
                    "price_after_discount":bottle.price_after_discount
                } for bottle in product.bottles.all()])
            })
        return render(request, 'index.html', {"products":products})
    

# offered product filter : Not immlimented
class OfferProducts(View):
    def get(self, request, *args, **kwargs):
        products = []
        for product in Products.objects.all():
            products.append({
                "name":product.name,
                "description":product.description,
                "first_image":product.images.first().image.url,
                "image_urls":json.dumps([img.image.url for img in product.images.all()]),
                "bottles":json.dumps([{
                    "bottle_size_ml":bottle.bottle_size_ml,
                    "bottle_price":bottle.price,
                    "price_after_discount":bottle.price_after_discount
                } for bottle in product.bottles.all()])
            })
        return render(request, 'index.html', {"products":products})
    


# combo offeres: not implimented
class ComboProducts(View):
    def get(self, request, *args, **kwargs):
        products = []
        for product in Products.objects.all():
            products.append({
                "name":product.name,
                "description":product.description,
                "first_image":product.images.first().image.url,
                "image_urls":json.dumps([img.image.url for img in product.images.all()]),
                "bottles":json.dumps([{
                    "bottle_size_ml":bottle.bottle_size_ml,
                    "bottle_price":bottle.price,
                    "price_after_discount":bottle.price_after_discount
                } for bottle in product.bottles.all()])
            })
        return render(request, 'index.html', {"products":products})


class ContactUs(View):
    def get(self, request, *args, **kwargs):
        return render(request, "contact.html")