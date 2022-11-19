from django.db import models


class Hotel(models.Model):
    nom = models.CharField(max_length=200)
    emplacement = models.CharField(max_length=200)
    description = models.TextField()
    disponible = models.BooleanField(default=True)
    image = models.ImageField(upload_to='hotel_img', null=True, blank=True)
    
    def __str__(self):
        return self.nom
    

class Reservation(models.Model):
    hotel = models.ForeignKey(Hotel, null=True, blank=True, on_delete=models.CASCADE)
    avis =models.CharField(max_length=200)
    
    def __str__(self):
        return self.hotel

# Create your models here.
