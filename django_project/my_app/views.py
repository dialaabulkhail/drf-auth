from django.shortcuts import render

from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListCreateAPIView
from .models import Animal
from .serializers import AnimalSerializer


class AnimalListView(ListCreateAPIView):
    queryset = Animal.objects.all()
    serializer_class = AnimalSerializer
    permission_classes = (IsAuthenticated,)
