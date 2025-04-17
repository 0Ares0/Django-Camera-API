from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from .models import Blogpost, Camera, Lens
from .serializers import BlogpostSerializer, CameraSerializer, LensSerializer
from rest_framework.views import APIView

# Create your views here.


class BlogpostListCreate(generics.ListCreateAPIView):
    queryset = Blogpost.objects.all()
    serializer_class = BlogpostSerializer

    def delete(self, request, *args, **kwargs):
        Blogpost.objects.all().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class BlogpostRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Blogpost.objects.all()
    serializer_class = BlogpostSerializer
    lookup_field = "pk"


class CameraListCreate(generics.ListCreateAPIView):
    queryset = Camera.objects.all()
    serializer_class = CameraSerializer


class LensListCreate(generics.ListCreateAPIView):
    queryset = Blogpost.objects.all()
    serializer_class = LensSerializer
