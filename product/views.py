from django.shortcuts import render
from django.views import View
# Create your views here.


class Test(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')
    

class ProductDetails(View):
    def get(self, request, *args, **kwargs):
        return render(request, "product-detail.html")
    

class ContactUs(View):
    def get(self, request, *args, **kwargs):
        return render(request, "contact.html")