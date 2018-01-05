from django.db.models import Q
from django.shortcuts import render
from birraWeb.models import *
import datetime


# Create your views here.


def homeView(request):
    if not request.user.is_authenticated():
        return render(request, 'registration/login.html')
    else:
        return render(request, 'home/index.html')


def calculoTotalFacturado(request):
    fecha = request.GET.get('fecha')
    print(fecha)
    sep_fec = fecha.split('-')
    if fecha != '' and request.is_ajax():
        today_min = datetime.datetime.combine(datetime.date(int(sep_fec[0]), int(sep_fec[1]), int(sep_fec[2])),
                                              datetime.time.min)
        today_max = datetime.datetime.combine(datetime.date(int(sep_fec[0]), int(sep_fec[1]), int(sep_fec[2])),
                                              datetime.time.max)
    else:

        today_min = datetime.datetime.combine(datetime.date.today(), datetime.time.min)
        today_max = datetime.datetime.combine(datetime.date.today(), datetime.time.max)

    # Seccion que calcula el total Vendido
    lista_pedidos_cabecera = PedidosCabecera.objects.filter(fecha_evento__range=(today_max, today_min),
                                                            estado__in=('ACTIVO', 'FACTURADO', 'PREFACTURA'))
    lista_pedidos_detalle = PedidosDetalle.objects.filter(Q(id_cabecera__in=lista_pedidos_cabecera))

    sum_pago = 0
    for i in lista_pedidos_detalle.filter(anulado=0):
        sum_pago += i.monto_total_linea

    # Seccion que calcula el total a Facturar
    monto_fact = 0
    for i in lista_pedidos_cabecera.filter(estado__exact='FACTURADO'):
        monto_fact += i.monto_total

    # Seccion que calcula el pendiente a facturar
    monto_pend_fact = 0
    for i in lista_pedidos_cabecera.filter(estado__exact='ACTIVO',
                                           factura_numero__isnull=True,
                                           factura_timbrado__isnull=True):
        monto_pend_fact += i.monto_total
    # Seccion que calcula la cantidad de cubiertos
    canti_cub = 0
    for i in lista_pedidos_cabecera:
        canti_cub += i.cantidad_cubiertos

    # Seccion que calcula el promedio
    prom = 0.0
    try:
        prom = sum_pago / canti_cub
    except Exception as e:
        prom = 0.0

    context = {
        "sum_pago": sum_pago,
        "canti_cub": canti_cub,
        "prom": prom,
        "monto_fact": monto_fact,
        "monto_pend_fact":monto_pend_fact
    }
    return render(request, 'resultados/totalFacturadoEnDia.html', context)
