"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from app import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register_view, name="register"),
    path("query/places/<str:q>", views.query, name="query"),
    path("flight", views.flight, name="flight"),
    path("review", views.review, name="review"),
    path("flight/ticket/book", views.book, name="book"),
    path("flight/ticket/payment", views.payment, name="payment"),
    path('flight/ticket/api/<str:ref>', views.ticket_data, name="ticketdata"),
    path('flight/ticket/print',views.get_ticket, name="getticket"),
    path('flight/bookings', views.bookings, name="bookings"),
    path('flight/ticket/cancel', views.cancel_ticket, name="cancelticket"),
    path('flight/ticket/resume', views.resume_booking, name="resumebooking"),
    path('contact', views.contact, name="contact"),
    path('privacy-policy', views.privacy_policy, name="privacypolicy"),
    path('terms-and-conditions', views.terms_and_conditions, name="termsandconditions"),
    path('about-us', views.about_us, name="aboutus"),
    path("admin/",admin.site.urls)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
