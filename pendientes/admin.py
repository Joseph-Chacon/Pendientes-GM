from django.contrib import admin
from .models import Pendiente, PuntoVenta, Tecnico


@admin.register(PuntoVenta)
class PuntoVentaAdmin(admin.ModelAdmin):
    list_display = ("codigo", "nombre", "activo", "fecha_creacion")
    list_filter = ("activo",)
    search_fields = ("codigo", "nombre")


@admin.register(Tecnico)
class TecnicoAdmin(admin.ModelAdmin):
    list_display = ("nombre", "activo")
    list_filter = ("activo",)
    search_fields = ("nombre",)


@admin.register(Pendiente)
class PendienteAdmin(admin.ModelAdmin):
    list_display = (
        "codigo",
        "titulo",
        "punto_venta",
        "prioridad",
        "estado",
        "tecnico_resolvio",
        "fecha_registro",
    )
    list_filter = ("estado", "prioridad", "punto_venta")
    search_fields = ("codigo", "titulo", "detalle")
    readonly_fields = ("codigo", "fecha_registro", "fecha_resolucion")
