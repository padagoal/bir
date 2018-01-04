from django.shortcuts import render
from birraWeb.models import *
import datetime
# Create your views here.


def homeView (request):
    if not request.user.is_authenticated():
        return render(request, 'registration/login.html')
    else:
        return render(request, 'home/index.html')



def calculoTotalFacturado(request):
    if not request.user.is_authenticated():
        return render(request, 'registration/login.html')
    else:
        today_min = datetime.datetime.combine(datetime.date.today(), datetime.time.min)
        today_max = datetime.datetime.combine(datetime.date.today(), datetime.time.max)
        pagos_detalle = PagosDetalle.objects.filter(fecha_evento__range=(today_max, today_min))
        sum_pago = 0.0
        for i in pagos_detalle:
            sum_pago+=i.monto_pago
        return render(request, 'home/index.html')