from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views

urlpatterns = [
    path("blogposts/", views.BlogpostListCreate.as_view(), name="blogpost-view-create"),
    path(
        "blogposts/<int:pk>/",
        views.BlogpostRetrieveUpdateDestroy.as_view(),
        name="update",
    ),
    path("Cameras/", views.CameraListCreate.as_view(), name="Camera-view-create"),
    path("Lenses/", views.LensListCreate.as_view(), name="Lenses-view-create"),
]
