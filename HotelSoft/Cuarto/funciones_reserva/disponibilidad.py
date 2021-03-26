import datetime
from Cuarto.models import Cuarto, Reserva

def check_disponibilidad(Cuarto, check_in, check_out):
    dispon_list = []
    lista_reservas = Reserva.objects.filter(cuarto=Cuarto)
    for reserva in lista_reservas:
        if reserva.check_in > check_out or reserva.check_out < check_in:
            dispon_list.append(True)
        else:
            dispon_list.append(False)
    return all(dispon_list)


