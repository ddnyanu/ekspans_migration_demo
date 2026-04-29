from django.shortcuts import render

# Create your views here.
from rest_framework.generics import ListCreateAPIView
from .models import Product
from .serializers import ProductSerializer

class ProductAPIView(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer