from django.db import models

# Create your models here.


class Blogpost(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Camera(models.Model):
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    megapixels = models.DecimalField(max_digits=5, decimal_places=2)
    release_year = models.PositiveBigIntegerField()

    def __str__(self):
        return self.brand


class Lens(models.Model):
    brand = models.CharField(max_length=100)
    focal_length = models.CharField(max_length=100)
    apperture = models.CharField(max_length=100)
    compatibility = models.PositiveBigIntegerField()

    def __str__(self):
        return self.brand
