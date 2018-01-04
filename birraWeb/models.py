# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class SistemaLocales(models.Model):
    id_local = models.AutoField(primary_key=True)
    padre = models.IntegerField(blank=True, null=True)
    codigo_anterior = models.IntegerField()
    nombre_local = models.CharField(unique=True, max_length=20, blank=True, null=True)
    descripcion = models.CharField(max_length=100, blank=True, null=True)
    imagen_logo = models.CharField(max_length=100, blank=True, null=True)
    razon_social = models.CharField(max_length=50, blank=True, null=True)
    ruc = models.CharField(max_length=20, blank=True, null=True)
    listado_precios_activo = models.IntegerField(blank=True, null=True)
    estado = models.IntegerField()
    capacidad_mesas = models.IntegerField(blank=True, null=True)
    capacidad_personas = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = '_sistema_locales'


class SistemaLogAccesos(models.Model):
    idlog = models.AutoField(primary_key=True)
    idusuario = models.IntegerField(blank=True, null=True)
    fechahora = models.DateTimeField(blank=True, null=True)
    direccionip = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = '_sistema_log_accesos'


class SistemaParametros(models.Model):
    parametro = models.CharField(primary_key=True, max_length=50)
    tipo = models.CharField(max_length=7, blank=True, null=True)
    valor = models.CharField(max_length=20)
    descripcion = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = '_sistema_parametros'


class SistemaUsuarios(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    estado = models.CharField(max_length=7, blank=True, null=True)
    locales = models.CharField(max_length=50, blank=True, null=True)
    nombre_usuario = models.CharField(max_length=20)
    pass_usuario = models.CharField(max_length=50)
    nivel_usuario = models.IntegerField()
    grupo_usuario = models.IntegerField(blank=True, null=True)
    pin_numerico = models.CharField(unique=True, max_length=100)
    nombres = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    fecha_nacimiento = models.DateField(blank=True, null=True)
    direccion = models.CharField(max_length=250)
    telefono = models.CharField(max_length=20)
    celular = models.CharField(max_length=20)
    email_usuario = models.CharField(max_length=50)
    cambiar_pass = models.TextField()  # This field type is a guess.
    ultimo_cambio_pass = models.DateTimeField()
    fecha_ingreso = models.DateField(blank=True, null=True)
    fecha_egreso = models.DateField(blank=True, null=True)
    imagen = models.TextField(blank=True, null=True)
    comentarios = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = '_sistema_usuarios'


class UsuariosRolesPermisos(models.Model):
    id_rol = models.AutoField(primary_key=True)
    id_usuario_rol = models.IntegerField()
    id_permiso_def = models.IntegerField()

    class Meta:
        managed = False
        db_table = '_usuarios_roles_permisos'


class Articulos(models.Model):
    id_articulo = models.IntegerField(primary_key=True)
    id_grupo_articulo = models.IntegerField()
    id_local = models.IntegerField(blank=True, null=True)
    codigo_erp = models.CharField(max_length=100, blank=True, null=True)
    codigo_barras = models.CharField(max_length=100, blank=True, null=True)
    descripcion_corta = models.CharField(max_length=40)
    descripcion_larga = models.CharField(max_length=255, blank=True, null=True)
    tipo_iva = models.IntegerField(blank=True, null=True)
    orden_articulo = models.IntegerField(blank=True, null=True)
    costo_principal = models.DecimalField(max_digits=15, decimal_places=4)
    costo_promedio = models.DecimalField(max_digits=15, decimal_places=4, blank=True, null=True)
    costo_ultimacompra = models.DecimalField(max_digits=15, decimal_places=4, blank=True, null=True)
    unidad_medida_um = models.IntegerField(blank=True, null=True)
    presentacion = models.IntegerField(blank=True, null=True)
    razon_pack = models.DecimalField(max_digits=11, decimal_places=4)
    contenido_exacto_cantidad = models.IntegerField(blank=True, null=True)
    contenido_exacto_um = models.IntegerField()
    proveedor = models.IntegerField(blank=True, null=True)
    articulo_imagen = models.TextField(blank=True, null=True)
    es_insumo = models.IntegerField(blank=True, null=True)
    compra = models.IntegerField(blank=True, null=True)
    receta = models.IntegerField(blank=True, null=True)
    stock = models.IntegerField(blank=True, null=True)
    venta = models.IntegerField(blank=True, null=True)
    impresora1 = models.IntegerField()
    impresora2 = models.IntegerField()
    impresora3 = models.IntegerField()
    impresora4 = models.IntegerField()
    impresora5 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'articulos'


class ArticulosGrupos(models.Model):
    id_grupo = models.AutoField(primary_key=True)
    grupo_nombre = models.CharField(max_length=50)
    grupo_imagen = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'articulos_grupos'


class ArticulosObservaciones(models.Model):
    id_observacion = models.AutoField(primary_key=True)
    id_articulo = models.IntegerField()
    observacion = models.CharField(max_length=700)

    class Meta:
        managed = False
        db_table = 'articulos_observaciones'


class ArticulosRecetas(models.Model):
    id_receta = models.AutoField(primary_key=True)
    id_insumo = models.IntegerField()
    cantidad_insumo = models.DecimalField(max_digits=10, decimal_places=2)
    costo_insumo = models.DecimalField(max_digits=11, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'articulos_recetas'
        unique_together = (('id_receta', 'id_insumo'),)


class DefImpuestos(models.Model):
    id_impuesto = models.AutoField(primary_key=True)
    descripcion_impuesto = models.CharField(max_length=50)
    iva = models.DecimalField(max_digits=10, decimal_places=0)

    class Meta:
        managed = False
        db_table = 'def_impuestos'


class DefMediosPago(models.Model):
    codigo_medio_pago = models.CharField(primary_key=True, max_length=5)
    descripcion_medio = models.CharField(max_length=100, blank=True, null=True)
    pago_real = models.IntegerField(blank=True, null=True)
    tipo_cambio = models.DecimalField(max_digits=11, decimal_places=3, blank=True, null=True)
    id_orden = models.IntegerField(unique=True)
    datos_adic = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'def_medios_pago'


class DefMediosPagoDatosAdic(models.Model):
    id_medio_pago_datos_adic = models.AutoField(primary_key=True)
    tipo_medio_pago = models.CharField(max_length=5)
    descripcion_medio_pago_datos_adi = models.CharField(max_length=150, blank=True, null=True)
    id_orden = models.IntegerField(unique=True)

    class Meta:
        managed = False
        db_table = 'def_medios_pago_datos_adic'


class DefMensajes(models.Model):
    id_mensaje = models.AutoField(primary_key=True)
    codigo_idioma = models.CharField(max_length=3, blank=True, null=True)
    tipo = models.CharField(max_length=5, blank=True, null=True)
    mensaje = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'def_mensajes'


class DefObservaciones(models.Model):
    observacion = models.CharField(max_length=700)

    class Meta:
        managed = False
        db_table = 'def_observaciones'


class DefPermisos(models.Model):
    id_permiso = models.AutoField(primary_key=True)
    valor_permiso = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'def_permisos'


class DefPresentacion(models.Model):
    id_presentacion = models.AutoField(primary_key=True)
    nombre_presentacion = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'def_presentacion'


class DefRolesUsuarios(models.Model):
    id_grupo = models.AutoField(primary_key=True)
    nombre = models.CharField(unique=True, max_length=20)

    class Meta:
        managed = False
        db_table = 'def_roles_usuarios'


class DefUnidadMedida(models.Model):
    id_um = models.AutoField(primary_key=True)
    nombre_um = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'def_unidad_medida'


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DocumentosAnulados(models.Model):
    id_documento_anulado = models.AutoField(primary_key=True)
    documento_anulado_tipo = models.CharField(max_length=50)
    documento_anulado_numero = models.IntegerField()
    motivo_anulacion = models.CharField(max_length=255, blank=True, null=True)
    supervisor_codigo = models.IntegerField(blank=True, null=True)
    supervisor_nombre_usuario = models.CharField(max_length=100, blank=True, null=True)
    operador_codigo = models.IntegerField(blank=True, null=True)
    operador_nombre_usuario = models.CharField(max_length=100, blank=True, null=True)
    fecha_evento = models.DateField(blank=True, null=True)
    local_evento = models.IntegerField(blank=True, null=True)
    fecha_hora = models.DateTimeField(blank=True, null=True)
    direccion_ip = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'documentos_anulados'


class ListadoPreciosCab(models.Model):
    id_lista = models.AutoField(primary_key=True)
    estado = models.CharField(max_length=23, blank=True, null=True)
    descripcion = models.CharField(max_length=255, blank=True, null=True)
    local = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'listado_precios_cab'


class ListadoPreciosDet(models.Model):
    id_detalle = models.AutoField(primary_key=True)
    id_lista_cabecera = models.IntegerField()
    id_articulo = models.IntegerField()
    precio01 = models.DecimalField(max_digits=15, decimal_places=4)
    precio02 = models.DecimalField(max_digits=15, decimal_places=4, blank=True, null=True)
    precio03 = models.DecimalField(max_digits=15, decimal_places=4, blank=True, null=True)
    promo_x_horas = models.IntegerField(blank=True, null=True)
    estado = models.CharField(max_length=23)

    class Meta:
        managed = False
        db_table = 'listado_precios_det'


class ListadoPreciosHoras(models.Model):
    id_detalle_hora = models.AutoField(primary_key=True)
    id_lista_detalle = models.ForeignKey(ListadoPreciosDet, models.DO_NOTHING, db_column='id_lista_detalle')
    dia_valido = models.CharField(max_length=1, blank=True, null=True)
    hora_valido = models.IntegerField(blank=True, null=True)
    lista_precio_usar = models.IntegerField()
    cantidad_minima_linea = models.IntegerField(blank=True, null=True)
    descripcion = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'listado_precios_horas'


class MaestroClientes(models.Model):
    id_cliente = models.AutoField(primary_key=True)
    ruc_documento_identidad = models.CharField(unique=True, max_length=20, blank=True, null=True)
    ruc_razon_social = models.CharField(max_length=32, blank=True, null=True)
    nombres = models.CharField(max_length=50, blank=True, null=True)
    apellidos = models.CharField(max_length=50, blank=True, null=True)
    telefono_movil = models.IntegerField(blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    fecha_nacimiento = models.DateField(blank=True, null=True)
    direccion_particular = models.CharField(max_length=255, blank=True, null=True)
    telefono_fijo_particular = models.IntegerField(blank=True, null=True)
    empresa = models.CharField(max_length=100, blank=True, null=True)
    cargo = models.CharField(max_length=100, blank=True, null=True)
    direccion_laboral = models.CharField(max_length=255, blank=True, null=True)
    telefono_fijo_laboral = models.IntegerField(blank=True, null=True)
    genero_cliente = models.CharField(max_length=1, blank=True, null=True)
    grupo_cliente = models.IntegerField(blank=True, null=True)
    tarjeta1_tipo = models.CharField(max_length=50, blank=True, null=True)
    tarjeta1_numero = models.CharField(max_length=100, blank=True, null=True)
    tarjeta1_fecha_emision = models.DateField(blank=True, null=True)
    tarjeta1_fecha_vencimiento = models.DateField(blank=True, null=True)
    tarjeta1_dato_adicional = models.CharField(max_length=100, blank=True, null=True)
    origen_cliente = models.CharField(max_length=20, blank=True, null=True)
    tarjeta2_tipo = models.CharField(max_length=50, blank=True, null=True)
    tarjeta2_numero = models.CharField(max_length=100, blank=True, null=True)
    tarjeta2_fecha_emision = models.DateField(blank=True, null=True)
    tarjeta2_fecha_vencimiento = models.DateField(blank=True, null=True)
    tarjeta2_dato_adicional = models.CharField(max_length=100, blank=True, null=True)
    registro_nombre_usuario = models.CharField(max_length=100, blank=True, null=True)
    registro_fecha_hora = models.DateTimeField(blank=True, null=True)
    registro_ip = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'maestro_clientes'


class MaestroClientesGrupos(models.Model):
    id_grupo = models.AutoField(primary_key=True)
    descripcion_grupo = models.CharField(max_length=100)
    porcentaje_descuento = models.IntegerField(blank=True, null=True)
    monto_limite_gentileza = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    comentarios = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'maestro_clientes_grupos'


class MaestroProveedores(models.Model):
    id_proveedor = models.AutoField(primary_key=True)
    ruc_proveedor = models.CharField(unique=True, max_length=20)
    nombre_razon_social = models.CharField(unique=True, max_length=50)
    telefono_fijo = models.CharField(max_length=20, blank=True, null=True)
    telefono_movil = models.CharField(max_length=20, blank=True, null=True)
    persona_contacto = models.CharField(max_length=100, blank=True, null=True)
    persona_cargo = models.CharField(max_length=20, blank=True, null=True)
    persona_email = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'maestro_proveedores'
        unique_together = (('id_proveedor', 'ruc_proveedor'),)


class Mesas(models.Model):
    id_mesa = models.AutoField(primary_key=True)
    abierto_en_terminal = models.IntegerField(blank=True, null=True)
    estado = models.CharField(max_length=10, blank=True, null=True)
    id_local = models.IntegerField()
    id_sector = models.IntegerField()
    nombre = models.CharField(max_length=20)
    pos_x = models.IntegerField(blank=True, null=True)
    pos_y = models.IntegerField(blank=True, null=True)
    cantidad_personas = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mesas'


class MesasEstados(models.Model):
    id_estado = models.AutoField(primary_key=True)
    cod_estado = models.CharField(max_length=3)
    desc_estado = models.CharField(max_length=30)
    desc_larga = models.CharField(max_length=200, blank=True, null=True)
    color_r = models.CharField(db_column='color_R', max_length=4, blank=True, null=True)  # Field name made lowercase.
    color_g = models.CharField(db_column='color_G', max_length=4, blank=True, null=True)  # Field name made lowercase.
    color_b = models.CharField(db_column='color_B', max_length=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'mesas_estados'


class PagosCabecera(models.Model):
    id_pago_cabecera = models.AutoField(primary_key=True)
    tipo_operacion_documento = models.CharField(max_length=48)
    numero_operacion = models.IntegerField()
    turno_caja = models.IntegerField()
    codigo_cliente = models.IntegerField()
    fecha_evento = models.DateField()
    local_evento = models.IntegerField()
    total_pago = models.FloatField()
    operador_codigo = models.IntegerField()
    operador_nombre_usuario = models.CharField(max_length=100)
    registro_fechahora = models.DateTimeField(blank=True, null=True)
    registro_ip = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pagos_cabecera'


class PagosDetalle(models.Model):
    id_pago_detalle = models.AutoField(primary_key=True)
    id_pago_cabecera = models.IntegerField()
    estado = models.CharField(max_length=14)
    medio_pago = models.CharField(max_length=53)
    medio_pago_subtipo = models.CharField(max_length=20, blank=True, null=True)
    monto_pago = models.FloatField()
    monto_tipo_cambio = models.FloatField()
    monto_original = models.FloatField()
    codigo_operacion_voucher = models.CharField(max_length=100, blank=True, null=True)
    entidad_emisora_banco = models.CharField(max_length=100, blank=True, null=True)
    usuario_codigo = models.IntegerField()
    usuario_nombre = models.CharField(max_length=50)
    registro_fechahora = models.DateTimeField(blank=True, null=True)
    registro_ip = models.CharField(max_length=100, blank=True, null=True)
    observacion = models.CharField(max_length=500, blank=True, null=True)
    fecha_evento = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pagos_detalle'

    def __unicode__(self):
        return self

class PedidosCabecera(models.Model):
    id_pedido_cabecera = models.BigAutoField(primary_key=True)
    estado = models.CharField(max_length=10, blank=True, null=True)
    id_local = models.IntegerField(unique=True, blank=True, null=True)
    id_mesa = models.IntegerField(blank=True, null=True)
    id_mozo = models.IntegerField(blank=True, null=True)
    id_turno_caja = models.IntegerField(blank=True, null=True)
    fecha_evento = models.DateField(blank=True, null=True)
    id_usuario_apertura = models.IntegerField(blank=True, null=True)
    fecha_apertura = models.DateTimeField(blank=True, null=True)
    id_usuario_cierre = models.IntegerField(blank=True, null=True)
    fecha_cierre = models.DateTimeField(blank=True, null=True)
    codigo_cliente = models.IntegerField(blank=True, null=True)
    monto_total = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    monto_propina = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    monto_descuento = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    cantidad_cubiertos = models.IntegerField(blank=True, null=True)
    factura_numero = models.BigIntegerField(blank=True, null=True)
    factura_timbrado = models.BigIntegerField(blank=True, null=True)
    factura_condicion_pago = models.CharField(max_length=7, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pedidos_cabecera'


class PedidosDetalle(models.Model):
    id_pedido_detalle = models.AutoField(primary_key=True)
    id_cabecera = models.IntegerField()
    producto_codigo = models.IntegerField()
    producto_desc = models.CharField(max_length=100, blank=True, null=True)
    cantidad = models.DecimalField(max_digits=12, decimal_places=4)
    monto_precio_unitario = models.DecimalField(max_digits=12, decimal_places=4)
    monto_total_linea = models.DecimalField(max_digits=12, decimal_places=4)
    monto_precio_costo = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    impuesto_tipo = models.CharField(max_length=5, blank=True, null=True)
    monto_descuento_linea = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    impuesto_porcentaje = models.IntegerField(blank=True, null=True)
    comentarios_linea = models.CharField(max_length=255, blank=True, null=True)
    impreso = models.IntegerField(blank=True, null=True)
    anulado = models.IntegerField(blank=True, null=True)
    monto_impuesto_total_linea = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    monto_total_antes_impuesto = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    registro_fechahora = models.DateTimeField(blank=True, null=True)
    registro_ip = models.CharField(max_length=40, blank=True, null=True)
    registro_nombreusuario = models.CharField(max_length=40, blank=True, null=True)
    local_evento = models.IntegerField()
    porcentaje_descuento_linea = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pedidos_detalle'


class Sectores(models.Model):
    id_sector = models.AutoField(primary_key=True)
    nombre_sector = models.CharField(unique=True, max_length=20)
    local_sector = models.IntegerField()
    punto_acceso = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sectores'


class SeriesNumeracion(models.Model):
    id_serie_numeracion = models.AutoField(primary_key=True)
    estado = models.IntegerField(blank=True, null=True)
    establecimiento = models.IntegerField()
    punto_emision_numero = models.IntegerField(blank=True, null=True)
    punto_emision_ubicacion = models.CharField(max_length=50)
    timbrado = models.IntegerField(blank=True, null=True)
    validez = models.DateField(blank=True, null=True)
    tipo_documento = models.CharField(max_length=13, blank=True, null=True)
    numero_inicial = models.IntegerField(blank=True, null=True)
    numero_final = models.IntegerField(blank=True, null=True)
    ultimo_numero = models.IntegerField(blank=True, null=True)
    registro_usuario = models.CharField(max_length=50, blank=True, null=True)
    registro_ip = models.CharField(max_length=50, blank=True, null=True)
    registro_fechahora = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'series_numeracion'


class StockActual(models.Model):
    id_stock = models.AutoField(primary_key=True)
    id_deposito = models.IntegerField()
    codigo_articulo = models.IntegerField()
    cantidad = models.DecimalField(max_digits=11, decimal_places=4)
    ultima_actualizacion = models.DateTimeField()
    codigo_control = models.IntegerField(unique=True)

    class Meta:
        managed = False
        db_table = 'stock_actual'


class StockDepositos(models.Model):
    id_deposito = models.AutoField(primary_key=True)
    deposito_nombre = models.CharField(max_length=20)
    tipo_deposito = models.CharField(max_length=10, blank=True, null=True)
    locales = models.CharField(max_length=10, blank=True, null=True)
    ubicacion = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stock_depositos'


class StockMovimientosCab(models.Model):
    id_movimiento = models.AutoField(primary_key=True)
    tipo_documento = models.IntegerField()
    tipo_movimiento = models.CharField(max_length=20)
    movimiento_estado = models.CharField(max_length=35, blank=True, null=True)
    fecha_evento = models.DateField()
    proveedor = models.IntegerField()
    local_evento = models.IntegerField()
    deposito_entrada = models.IntegerField()
    deposito_salida = models.IntegerField()
    registro_usuario_codigo = models.IntegerField()
    registro_usuario_nombre = models.CharField(max_length=20)
    aprobado_usuario_codigo = models.IntegerField(blank=True, null=True)
    aprobado_usuario_nombre = models.CharField(max_length=20, blank=True, null=True)
    movimiento_comentarios = models.CharField(max_length=255, blank=True, null=True)
    lista_precio = models.IntegerField()
    total_entrega = models.DecimalField(max_digits=11, decimal_places=2, blank=True, null=True)
    total_devolucion = models.DecimalField(max_digits=11, decimal_places=2, blank=True, null=True)
    total_venta = models.DecimalField(max_digits=11, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stock_movimientos_cab'


class StockMovimientosDet(models.Model):
    id_movimiento_det = models.AutoField(primary_key=True)
    id_movimiento_cab = models.IntegerField()
    codigo_proveedor = models.IntegerField(blank=True, null=True)
    codigo_articulo = models.IntegerField()
    cantidad_entrada = models.DecimalField(max_digits=11, decimal_places=4)
    cantidad_salida = models.DecimalField(max_digits=11, decimal_places=4, blank=True, null=True)
    precio_costo = models.DecimalField(max_digits=11, decimal_places=2, blank=True, null=True)
    precio_venta = models.DecimalField(max_digits=11, decimal_places=2, blank=True, null=True)
    operador_codigo = models.IntegerField(blank=True, null=True)
    registro_ip = models.CharField(max_length=100, blank=True, null=True)
    operador_nombre_usuario = models.CharField(max_length=20, blank=True, null=True)
    registro_fechahora = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'stock_movimientos_det'


class StockNiveles(models.Model):
    id_nivel = models.AutoField(primary_key=True)
    id_deposito = models.IntegerField()
    codigo_articulo = models.IntegerField()
    cantidad_min = models.DecimalField(max_digits=11, decimal_places=4)
    cantidad_max = models.DecimalField(max_digits=11, decimal_places=4)
    codigo_control = models.IntegerField(unique=True)
    registro_fechahora = models.DateTimeField(blank=True, null=True)
    registro_codigo_usuario = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stock_niveles'


class StockTipoMovimiento(models.Model):
    codigo_num_movimiento = models.AutoField(primary_key=True)
    codigo_string_mov = models.CharField(max_length=20, blank=True, null=True)
    tipo_movimiento = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stock_tipo_movimiento'


class TurnosCajas(models.Model):
    id_turno_caja = models.AutoField(primary_key=True)
    estado = models.CharField(max_length=7, blank=True, null=True)
    fecha_evento = models.DateField()
    local_evento = models.IntegerField()
    supervisor_codigo = models.IntegerField(blank=True, null=True)
    supervisor_nombre_usuario = models.CharField(max_length=100, blank=True, null=True)
    operador_codigo = models.IntegerField()
    operador_nombre_usuario = models.CharField(max_length=100, blank=True, null=True)
    apertura_fechahora = models.DateTimeField(blank=True, null=True)
    cierre_fechahora = models.DateTimeField(blank=True, null=True)
    serie_numeracion = models.IntegerField(blank=True, null=True)
    monto_caja_chica = models.DecimalField(max_digits=12, decimal_places=4)
    monto_total_venta = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    comentarios = models.CharField(max_length=100, blank=True, null=True)
    monto_diferencia_venta = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'turnos_cajas'


class TurnosCajasDet(models.Model):
    id_detalle = models.AutoField(primary_key=True)
    id_cabecera = models.IntegerField()
    medio_pago = models.CharField(max_length=5)
    estado = models.CharField(max_length=28)
    monto_original = models.DecimalField(max_digits=12, decimal_places=4)
    monto_tipo_cambio = models.DecimalField(max_digits=11, decimal_places=2, blank=True, null=True)
    monto_final = models.DecimalField(max_digits=11, decimal_places=2, blank=True, null=True)
    operador_codigo = models.IntegerField()
    operador_nombreusuario = models.CharField(max_length=20)
    supervisor_codigo = models.IntegerField(blank=True, null=True)
    supervisor_nombreusuario = models.CharField(max_length=20, blank=True, null=True)
    registro_fechahora = models.DateTimeField()
    registro_ip = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'turnos_cajas_det'
