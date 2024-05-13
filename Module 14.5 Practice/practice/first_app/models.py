from django.db import models
from datetime import datetime
# Create your models here.
class User(models.Model):
    userId = models.IntegerField(primary_key= True, default= None)
    username = models.CharField(default='Rahim', max_length=20)
    password = models.CharField(max_length=20)
    email = models.EmailField() 
    file_field = models.FileField(upload_to='files/',default=None)
    float_field = models.FloatField(default= 0.0)
    image_field = models.ImageField(default=None,upload_to='images/')
    # slug_field = models.SlugField()
    text_field = models.TextField(default=None)
    time_field = models.TimeField(default=datetime.now().time())
    url_field = models.URLField(default=None)

    def __str__(self):
        return f"Id : {self.userId} - {self.username}"