
from django.urls import path
from . import views

urlpatterns = [
    path("", views.HomePage.as_view()),
    path("newarrivals", views.NewArrivals.as_view()),
    path("contact", views.ContactUs.as_view()),

]