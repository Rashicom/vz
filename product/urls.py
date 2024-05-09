
from django.urls import path
from . import views

urlpatterns = [
    path("", views.HomePage.as_view()),
    path("newarrivals", views.NewArrivals.as_view()),
    path("offer-products", views.OfferProducts.as_view()),
    path("combo-offer-products", views.ComboProducts.as_view()),
    path("contact", views.ContactUs.as_view()),
    path("place-order", views.PlaceOrder.as_view()),

]