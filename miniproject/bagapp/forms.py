from django import forms
from . models import Newarrival


class Arrivalform(forms.ModelForm):
    # newimage=forms.ImageField(widget=forms.ImageField(attrs={'placeholder':'upload'}))
    newimage=forms.ImageField(widget=forms.FileInput(attrs={'placeholder':'upload','class':'upimg'}))
    description=forms.CharField(widget=forms.TextInput(attrs={'placeholder':'enter the description','class':'form-desc'}))
    # offer=forms.CharField(widget=forms.CharField(attrs={'placeholder':'Enter the offer name','class':'form-offer'}))
    class Meta:
        model=Newarrival
        fields='__all__'