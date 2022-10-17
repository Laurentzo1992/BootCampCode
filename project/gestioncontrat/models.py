from django.db import models

class Partenaire(models.Model):
    nom = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    telephone = models.CharField(max_length=100)
    email = models.EmailField()
    
    
class Structure(models.Model):
    sigle = models.CharField(max_length=100)
    nom = models.CharField(max_length=100)


class Financement(models.Model):
    intitule = models.CharField(max_length=100)
    
class Categorie(models.Model):
    intitule = models.CharField(max_length=100)

    
class Travail(models.Model):
    
    CDI = 'CDI'
    CDD = 'CDD'

    NATURE_CHOICES = (
        ('CDI', 'CDI'),
        ('CDD', 'CDD'),
    )
    reference = models.CharField(max_length=10)
    objet = models.TextField()
    nature = models.CharField(choices=NATURE_CHOICES, verbose_name='nature contrat')
    matricule = models.CharField(max_length=10)
    nom = models.CharField(max_length=60)
    prenom = models.CharField(max_length=80)
    montant = models.FloatField()
    duree = models.CharField(max_length=10)
    date_signature = models.DateField()
    date_debut = models.DateField()
    date_fin = models.DateField()
    nombre_renouv = models.IntegerField()
    date_renouvel = models.DateField()
    date_resiliation = models.DateField()
    lieu = models.CharField(max_length=100)
    date_alerte = models.DateField()
    



# Create your models here.
