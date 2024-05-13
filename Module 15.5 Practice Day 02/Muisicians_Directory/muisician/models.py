from django.db import models

# Create your models here.
class Muisician(models.Model):
    # id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=100)
    instrument_type = models.TextField(blank=True)

    def __str__(self):
        return f"{self.first_name}  {self.last_name}"