from django.shortcuts import render
from rest_framework import generics
from .serializers import TodoSerializer

# Create your views here.
from .models import Todo


class ListTodo(generics.ListAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


class DetailTodo(generics.RetrieveAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
