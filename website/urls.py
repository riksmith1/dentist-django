from django.urls import path
from . import views


app_name = 'website'

urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('pricing/', views.pricing, name='pricing'),
    path('appointment', views.appointment, name='appointment'),
]
