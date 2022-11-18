from django.db import models


class Personne(models.Model):

	nom = models.CharField(max_length=200, null=True)
	email = models.EmailField(null=False)
	phone = models.IntegerField(null=True, blank=True)
	address = models.TextField(null=True)

	def __str__(self):
		return self.nom

# Create your models here.
