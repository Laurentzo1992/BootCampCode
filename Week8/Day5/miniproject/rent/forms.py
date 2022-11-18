from django import forms
from rent.models import Type, Vehicule, Tarif, Location, Taille, Client



class LocationForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = '__all__'
        
        
        
class VehiculeForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = '__all__'
        
        
class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = '__all__'