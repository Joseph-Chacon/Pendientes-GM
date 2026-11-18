from django.core.exceptions import ValidationError
from django.db import models


class PuntoVenta(models.Model):
    codigo = models.CharField("código", max_length=10, unique=True)
    nombre = models.CharField("nombre", max_length=150)
    activo = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "punto de venta"
        verbose_name_plural = "puntos de venta"
        ordering = ["codigo"]

    def save(self, *args, **kwargs):
        self.codigo = self.codigo.upper().strip()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.codigo} — {self.nombre}"


class Tecnico(models.Model):
    nombre = models.CharField(max_length=120, unique=True)
    activo = models.BooleanField(default=True)

    class Meta:
        verbose_name = "técnico"
        verbose_name_plural = "técnicos"
        ordering = ["nombre"]

    def __str__(self):
        return self.nombre


class Pendiente(models.Model):
    class Prioridad(models.TextChoices):
        BAJA = "BAJA", "Baja"
        MEDIA = "MEDIA", "Media"
        ALTA = "ALTA", "Alta"

    class Estado(models.TextChoices):
        PENDIENTE = "PENDIENTE", "Pendiente"
        RESUELTO = "RESUELTO", "Resuelto"

    codigo = models.CharField(max_length=20, unique=True, editable=False, blank=True)
    titulo = models.CharField(max_length=160)
    detalle = models.TextField()
    punto_venta = models.ForeignKey(
        PuntoVenta, on_delete=models.PROTECT, related_name="pendientes"
    )
    prioridad = models.CharField(
        max_length=10, choices=Prioridad.choices, default=Prioridad.MEDIA
    )
    estado = models.CharField(
        max_length=12, choices=Estado.choices, default=Estado.PENDIENTE
    )
    tecnico_resolvio = models.ForeignKey(
        Tecnico,
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        related_name="pendientes_resueltos",
    )
    nota_solucion = models.TextField(blank=True)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    fecha_resolucion = models.DateTimeField(null=True, blank=True)

    class Meta:
        ordering = ["estado", "-fecha_registro"]

    def clean(self):
        if self.estado == self.Estado.RESUELTO and not self.tecnico_resolvio:
            raise ValidationError(
                {"tecnico_resolvio": "Seleccione el técnico que resolvió el pendiente."}
            )

    def save(self, *args, **kwargs):
        creating = self._state.adding
        super().save(*args, **kwargs)
        if creating and not self.codigo:
            self.codigo = f"P-{self.pk:06d}"
            type(self).objects.filter(pk=self.pk).update(codigo=self.codigo)

    def __str__(self):
        return f"{self.codigo} — {self.titulo}"
