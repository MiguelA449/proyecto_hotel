from django.db import models

from django.db import models
from django.conf import settings
# Create your models here.
class Cuarto(models.Model):
    CATEGORIAS_CUARTO = (
        ('SC','SENCILLA'),
        ('DBL','DOBLE'),
        ('KG','KING'),
        ('QN','QUEEN'),
        ('LJ','LUJO'),
    
    )
    numero_hab = models.IntegerField()
    categoria = models.CharField(max_length=3, choices=CATEGORIAS_CUARTO)
    camas = models.IntegerField()
    capacidad = models.IntegerField()
    
    def __str__(self):
        return f'{self.numero_hab}. {self.categoria} con {self.camas} cama(s) para {self.capacidad} persona(s)'

class Reserva(models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    cuarto = models.ForeignKey(Cuarto, on_delete=models.CASCADE)
    check_in = models.DateTimeField()
    check_out = models.DateTimeField()

    def __str__(self):
        return f'{self.usuario} ha reservado {self.cuarto} desde {self.check_in} hasta {self.check_out}'

        
