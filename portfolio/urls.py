from django.urls import path
from . import views

urlpatterns = [
    # Your existing URLs...
    path('', views.home, name='home'),  # Assuming you have a home view
    path('contact/', views.contact, name='contact'), 
]
