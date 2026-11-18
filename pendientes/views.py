from django.contrib import messages
from django.db.models import Count, Q
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone
from .forms import PendienteForm, PuntoVentaForm, ResolverPendienteForm, TecnicoForm
from .models import Pendiente, PuntoVenta, Tecnico


def tablero(request):
    pendientes = Pendiente.objects.select_related("punto_venta")
    abiertos = pendientes.filter(estado=Pendiente.Estado.PENDIENTE)
    context = {
        "total_pendientes": abiertos.count(),
        "total_resueltos": pendientes.filter(estado=Pendiente.Estado.RESUELTO).count(),
        "recientes": pendientes[:6],
        "por_punto_venta": PuntoVenta.objects.filter(activo=True)
        .annotate(
            cantidad_pendientes=Count(
                "pendientes", filter=Q(pendientes__estado=Pendiente.Estado.PENDIENTE)
            )
        )
        .order_by("-cantidad_pendientes", "codigo")[:8],
    }
    return render(request, "pendientes/tablero.html", context)


def lista_pendientes(request):
    registros = Pendiente.objects.select_related("punto_venta", "tecnico_resolvio")
    estado = request.GET.get("estado", "")
    punto_venta = request.GET.get("punto_venta", "")
    prioridad = request.GET.get("prioridad", "")
    consulta = request.GET.get("q", "").strip()
    if estado:
        registros = registros.filter(estado=estado)
    if punto_venta:
        registros = registros.filter(punto_venta_id=punto_venta)
    if prioridad:
        registros = registros.filter(prioridad=prioridad)
    if consulta:
        registros = registros.filter(
            Q(codigo__icontains=consulta)
            | Q(titulo__icontains=consulta)
            | Q(detalle__icontains=consulta)
        )
    return render(
        request,
        "pendientes/lista.html",
        {
            "pendientes": registros,
            "puntos_venta": PuntoVenta.objects.filter(activo=True),
            "estados": Pendiente.Estado.choices,
            "prioridades": Pendiente.Prioridad.choices,
        },
    )


def crear_pendiente(request):
    form = PendienteForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        pendiente = form.save()
        messages.success(request, f"El pendiente {pendiente.codigo} fue registrado.")
        return redirect("pendientes:detalle", pk=pendiente.pk)
    return render(request, "pendientes/formulario.html", {"form": form})


def detalle_pendiente(request, pk):
    pendiente = get_object_or_404(
        Pendiente.objects.select_related("punto_venta", "tecnico_resolvio"), pk=pk
    )
    return render(request, "pendientes/detalle.html", {"pendiente": pendiente})


def resolver_pendiente(request, pk):
    pendiente = get_object_or_404(Pendiente, pk=pk)
    if pendiente.estado == Pendiente.Estado.RESUELTO:
        messages.info(request, "Este pendiente ya está resuelto.")
        return redirect("pendientes:detalle", pk=pk)
    form = ResolverPendienteForm(request.POST or None, instance=pendiente)
    if request.method == "POST" and form.is_valid():
        pendiente = form.save(commit=False)
        pendiente.estado = Pendiente.Estado.RESUELTO
        pendiente.fecha_resolucion = timezone.now()
        pendiente.full_clean()
        pendiente.save()
        messages.success(
            request, f"El pendiente {pendiente.codigo} fue marcado como resuelto."
        )
        return redirect("pendientes:detalle", pk=pk)
    return render(
        request, "pendientes/resolver.html", {"form": form, "pendiente": pendiente}
    )


def catalogos(request):
    formularios = {
        "punto_venta": PuntoVentaForm(prefix="punto_venta"),
        "tecnico": TecnicoForm(prefix="tecnico"),
    }
    if request.method == "POST":
        tipo = request.POST.get("tipo")
        configuracion = {
            "punto_venta": (PuntoVentaForm, "Punto de venta"),
            "tecnico": (TecnicoForm, "Técnico"),
        }
        if tipo in configuracion:
            clase_formulario, etiqueta = configuracion[tipo]
            formulario = clase_formulario(request.POST, prefix=tipo)
            if formulario.is_valid():
                formulario.save()
                messages.success(request, f"{etiqueta} agregado correctamente.")
                return redirect("pendientes:catalogos")
            formularios[tipo] = formulario
    return render(
        request,
        "pendientes/catalogos.html",
        {
            "formularios": formularios,
            "puntos_venta": PuntoVenta.objects.all(),
            "tecnicos": Tecnico.objects.all(),
        },
    )
