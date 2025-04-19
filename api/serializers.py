from rest_framework import serializers
from .models import Blogpost, Camera, Lens


class BlogpostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blogpost
        fields = "__all__"


class CameraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Camera
        fields = "__all__"


class LensSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lens
        fields = "__all__"
