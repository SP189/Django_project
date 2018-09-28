from django.db import models
from django.urls import reverse


# Create your models here.
class Lehengas(models.Model):
   # lehenga_price = models.IntegerField()
    lehenga_desc = models.CharField(max_length=500)
    lehenga_size = models.CharField(max_length=10)
    lehenga_pic = models.CharField(max_length=10000)
    lehenga_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    available = models.BooleanField(default=True)
    stock = models.PositiveIntegerField(default=10)


    def get_absolute_url(self):
        return reverse('dresses:detail2', kwargs={'pk':self.pk})

    def __str__(self):
        return  self.lehenga_desc + ' - ' + self.lehenga_size

class weddingLehenga(models.Model):
    lehenga = models.ForeignKey(Lehengas, on_delete=models.CASCADE)
    wedL_colour = models.CharField(max_length= 50)

    def __str__(self):
        return self.wedL_colour

