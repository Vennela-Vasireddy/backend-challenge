from django.urls import path
from .views import home  # Ensure this import matches the location of the home function.

urlpatterns = [
    path('', home, name='home'),
]