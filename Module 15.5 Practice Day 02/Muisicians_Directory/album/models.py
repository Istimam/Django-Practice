from django.db import models
from muisician.models import Muisician
# Create your models here.
class Rating(models.IntegerChoices):
    ONE_STAR = 1, '1 Star'
    TWO_STARS = 2, '2 Stars'
    THREE_STARS = 3, '3 Stars'
    FOUR_STARS = 4, '4 Stars'
    FIVE_STARS = 5, '5 Stars'
class Album(models.Model):
    album_name = models.CharField(max_length=100)
    artist = models.ForeignKey(Muisician, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=Rating.choices)
    release_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.album_name