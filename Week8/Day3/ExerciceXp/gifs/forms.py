from django import  forms
from gifs.models import Gifs, Categorie


class  GifForm(forms.ModelForm):
    class Meta:
        gifs = forms.SelectMultiple()
        model = Gifs
        fields = '__all__'
        


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Categorie
        fields = ['nom']