from django.db import models

# Create your models here.
class Muisician(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=50)
    phone_number = models.CharField(max_length=15)
    instrument_type = models.CharField(max_length=30)


    def __str__(self):
        return self.first_name + " " + self.last_name