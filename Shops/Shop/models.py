from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User

class Shop(models.Model):
    owner=models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    name=models.CharField(max_length=255,)
    latitude=models.DecimalField(max_digits=9,decimal_places=6,validators=[MinValueValidator(-90.0),MaxValueValidator(90.0)])
    longitude=models.DecimalField(max_digits=9,decimal_places=6,validators=[MinValueValidator(-180.0),MaxValueValidator(180.0)])
    def __str__(self):
        return self.name

# Create your models here.
