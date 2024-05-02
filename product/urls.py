
from django.urls import path
from . import views

urlpatterns = [
    path("", views.Test.as_view()),
    path("product", views.ProductDetails.as_view()),
    path("contact", views.ContactUs.as_view()),

]