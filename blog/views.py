from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics
from . models import Post, Category
from .serializer import postserializer, categoryserializer

# Create your views here.
class categorylist(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = categoryserializer


class postlist(generics.ListCreateAPIView):
    queryset = Post.postobjects.all()
    serializer_class = postserializer



class postdetails(generics.RetrieveDestroyAPIView):
    queryset = Post.postobjects.all()
    serializer_class = postserializer()