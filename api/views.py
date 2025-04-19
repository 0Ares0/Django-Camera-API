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


# camera stuff here
class CameraListCreate(generics.ListCreateAPIView):
    queryset = Camera.objects.all()
    serializer_class = CameraSerializer

    def delete(self, request, *args, **kwargs):
        Camera.objects.all().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CameraRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Camera.objects.all()
    serializer_class = CameraSerializer
    lookup_field = "pk"


# lens stuff here


class LensListCreate(generics.ListCreateAPIView):
    queryset = Lens.objects.all()
    serializer_class = LensSerializer

    def delete(self, request, *args, **kwargs):
        Lens.objects.all().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class LensRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Lens.objects.all()
    serializer_class = LensSerializer
    lookup_field = "pk"
