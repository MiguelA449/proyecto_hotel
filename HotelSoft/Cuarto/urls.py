from django.urls import path
from .views import ListaHabitacion, ListaReserva, VistaReserva, Reserva_delete



urlpatterns=[
    path('lista_habitacion/', ListaHabitacion.as_view(), name='ListaHabitacion'),
    path('lista_reserva/', ListaReserva.as_view(), name='ListaReserva'),
    path('vista_reserva/', VistaReserva.as_view(), name='VistaReserva'),
    path('reserva_delete/<id_reserva>', Reserva_delete, name='Reserva_delete'),

]



#path('reserva_delete/', Reserva_delete(), name='Reserva_delete')
