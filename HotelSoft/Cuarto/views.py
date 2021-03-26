from django.shortcuts import render, HttpResponse
from django.views.generic import ListView, FormView
from .models import Cuarto, Reserva
from .forms import DisponibilidadForm
from Cuarto.funciones_reserva.disponibilidad import check_disponibilidad
# Create your views here.

class ListaHabitacion(ListView):
    model=Cuarto
    template_name = 'Cuarto/cuarto_list.html'

class ListaReserva(ListView):
    model=Reserva
    template_name = 'Cuarto/reserva_list.html'


class VistaReserva(FormView):
    form_class = DisponibilidadForm
    template_name = 'Cuarto/disponibilidad.form.html'

    def form_valid(self, form):
        data = form.cleaned_data
        cuarto_list = Cuarto.objects.filter(categoria=data['categoria_cuarto'])
        disponibilidad_cuartos =  []
        for cuarto in cuarto_list:
            if check_disponibilidad(Cuarto, data['check_in'], data['check_out']):
                disponibilidad_cuartos.append(Cuarto)

        if len(disponibilidad_cuartos) > 0:
            cuarto = disponibilidad_cuartos[0]
            reservas = Reserva.objects.create(
                user = self.request.user,
                cuarto = cuarto,
                check_in = data['check_in'],
                check_out = data['check_out']
            )
            Reserva.save()
            return HttpResponse(Reserva)
        else:
            return HttpResponse('Toda esta categoria de cuartos estan reservados! Intente otra categoria')

def Reserva_delete(request, id_reserva):
    reserva=Reserva.objects.get(id=id_reserva)
    if request.method=='POST':
        reserva.delete()
        return redirect('lista_reserva')
    return render(request, 'Cuarto/reserva_delete.html', {reserva: 'reserva'})
    





