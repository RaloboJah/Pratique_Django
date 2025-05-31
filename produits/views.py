# produits/views.py
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Produit
from .serializers import ProduitSerializer

@api_view(['GET'])
def liste_produits(request):
    produits = Produit.objects.all()
    serializer = ProduitSerializer(produits, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def ajouter_produit(request):
    serializer = ProduitSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def supprimer_produit(request, id):
    try:
        produit = Produit.objects.get(id=id)
    except Produit.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    produit.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['PUT'])
def modifier_produit(request, id):
    try:
        produit = Produit.objects.get(id=id)
    except Produit.DoesNotExist:
        return Response({'erreur': 'Produit non trouvé.'}, status=status.HTTP_404_NOT_FOUND)
    
    serializer = ProduitSerializer(produit, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

