from django.urls import path, include
from .views import home

urlpatterns = [
    path('', home, name='home'),  # route racine
    path('api/', include('produits.urls')),
]
