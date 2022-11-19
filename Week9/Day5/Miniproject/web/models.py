from django.db import models
from  django.contrib.auth.models import User

class Hotel(models.Model):
    nom = models.CharField(max_length=200)
    emplacement = models.CharField(max_length=200)
    description = models.TextField()
    disponible = models.BooleanField(default=True)
    image = models.ImageField(upload_to='hotel_img', null=True, blank=True)
    
    def __str__(self):
        return self.nom
    
    
    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url
    

class Reservation(models.Model):
    hotel = models.ForeignKey(Hotel, null=True, blank=True, on_delete=models.CASCADE)
    avis =models.CharField(max_length=200)
    reservation = models.DateField()
    sortit = models.DateField()
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.hotel.nom

# Create your models here.
