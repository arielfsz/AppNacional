from django import forms


class FutbolistaFormulario(forms.Form):

    nombre = forms.CharField()
    apellido = forms.CharField()
    nacimiento = forms.DateField(widget=forms.TextInput(attrs={'class': 'input', 'type':'date'}))
    posicion = forms.CharField()

class TecnicoFormulario(forms.Form):

    nombre = forms.CharField()
    apellido = forms.CharField()
    nacimiento = forms.DateField(widget=forms.TextInput(attrs={'class': 'input', 'type':'date'}))

class TorneoFormulario(forms.Form):

    nombre = forms.CharField()
    año = forms.IntegerField()
    caracter = forms.CharField()
    nacionalidad = forms.CharField()
    