from django.db import models


class  Gifs(models.Model):
    titre = models.CharField(max_length=200)
    url = models.URLField()
    nom_uploader = models.CharField(max_length=200)
    likes = models.IntegerField()
    created_at = models.DateField(auto_now=True)
    
    def __str__(self):
        return self.titre
    
    
class Categorie(models.Model):
    nom = models.CharField(max_length=200)
    gifs = models.ManyToManyField(Gifs, related_name='gifs', blank=True)
    
    def __str__(self):
        return self.nom
    

# Create your models here.
