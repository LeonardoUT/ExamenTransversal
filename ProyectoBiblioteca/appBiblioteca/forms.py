from django import forms

class BuscarLibro(forms.Form):
    title = forms.CharField(label='Título de Libro', max_length=150, required=True)