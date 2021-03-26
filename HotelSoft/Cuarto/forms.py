from django import forms

class DisponibilidadForm(forms.Form):
    CATEGORIAS_CUARTO = (
        ('SC','SENCILLA'),
        ('DBL','DOBLE'),
        ('KG','KING'),
        ('QN','QUEEN'),
        ('LJ','LUJO'),
    
    )
    categoria_cuarto = forms.ChoiceField(choices = CATEGORIAS_CUARTO, required=True)
    Entrada = forms.DateTimeField(required=True, input_formats=["%Y-%m-%dT-%H:%M",])
    salida = forms.DateTimeField(required=True, input_formats=["%Y-%m-%dT-%H:%M",])
