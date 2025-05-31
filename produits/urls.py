# produits/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('produits/', views.liste_produits, name='liste_produits'),
    path('produits/ajouter/', views.ajouter_produit, name='ajouter_produit'),
    path('produits/supprimer/<int:id>/', views.supprimer_produit, name='supprimer_produit'),
    path('produits/modifier/<int:id>/', views.modifier_produit, name='modifier_produit'),
]
