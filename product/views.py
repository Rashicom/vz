from django.shortcuts import render, redirect
from django.views import View
from .models import ProductBottles,Products
import json
from datetime import datetime
import urllib.parse
from django.db.models import Q
from django.core.mail import send_mail
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
                    "pk":str(bottle.pk),
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
                    "pk":str(bottle.pk),
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
                    "pk":str(bottle.pk),
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
                    "pk":str(bottle.pk),
                    "bottle_size_ml":bottle.bottle_size_ml,
                    "bottle_price":bottle.price,
                    "price_after_discount":bottle.price_after_discount
                } for bottle in product.bottles.all()])
            })
        return render(request, 'index.html', {"products":products})
    

class SearchProduct(View):

    def get(self, request, *args, **kwargs):
        search_key = request.GET.get("search_key")
        lookup = Q(name__icontains=search_key) | Q(description__icontains=search_key)
        products = []
        for product in Products.objects.filter(lookup):
            products.append({
                "name":product.name,
                "description":product.description,
                "first_image":product.images.first().image.url,
                "image_urls":json.dumps([img.image.url for img in product.images.all()]),
                "bottles":json.dumps([{
                    "pk":str(bottle.pk),
                    "bottle_size_ml":bottle.bottle_size_ml,
                    "bottle_price":bottle.price,
                    "price_after_discount":bottle.price_after_discount
                } for bottle in product.bottles.all()])
            })
        return render(request, 'index.html', {"products":products})


class PlaceOrder(View):
    def get(self, request):
        bottle_obj = ProductBottles.objects.filter(pk=request.GET.get('bottle_pk')).last()
        bottle_name = request.GET.get('product_name')
        bottle_size = bottle_obj.bottle_size_ml
        bottle_price = bottle_obj.price_after_discount

        address = request.GET.get('address')
        pin_code = request.GET.get('postcode')
        contact_number = request.GET.get('contact_number')

        message = f"I would like to order a perfume bottle of {bottle_name} {bottle_size} ML priced at {bottle_price}₹ to be delivered to the following Address :\n\n{address} Postal Code: {pin_code}\nContact Number: {contact_number}"
        encoded_message = urllib.parse.quote(message)
        watsapp_url = f"https://wa.me/7736721813?text={encoded_message}"
        print(watsapp_url)
        return redirect(watsapp_url)
    


# Contact us
class ContactUs(View):
    def get(self, request, *args, **kwargs):
        return render(request, "contact.html")

    def post(self, request, *args, **kwargs):
        email = request.POST.get("email")
        message = request.POST.get("message")
        print("email", email)
        print("message", message)
        message = message + " " + "From:" + str(email)
        try:
            send_mail(
                "Vz Enquiry",
                message,
                "rashid.kp484@gmail.com",
                ["vzperfumeshub555@gmail.com"],
                fail_silently=False,
            )
        except Exception as e:
            print(e)
            # TODO: log exception

        return render(request, "contact.html")
    