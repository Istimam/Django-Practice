from django.db import models
from Muisician.models import Muisician
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

STAR_RATING = [
        (1, '1 star'),
        (2, '2 star'),
        (3, '3 star'),
        (4, '4 star'),
        (5, '5 star'),
    ]

class Album(models.Model):
    name = models.CharField(max_length=100)
    muisician = models.ForeignKey(Muisician, on_delete=models.CASCADE, related_name='albums')
    release_date = models.DateField(auto_now_add=True, null= True)
    rating = models.IntegerField(choices=STAR_RATING, default=1)
    def __str__(self) -> str:
        return self.name