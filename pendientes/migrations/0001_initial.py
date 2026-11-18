# Generated manually for the initial project structure.
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True
    dependencies = []
    operations = [
        migrations.CreateModel(
            name="Categoria",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nombre", models.CharField(max_length=80, unique=True)),
                ("activa", models.BooleanField(default=True)),
            ],
            options={
                "verbose_name": "categoría",
                "verbose_name_plural": "categorías",
                "ordering": ["nombre"],
            },
        ),
        migrations.CreateModel(
            name="PuntoVenta",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "codigo",
                    models.CharField(max_length=10, unique=True, verbose_name="código"),
                ),
                ("nombre", models.CharField(max_length=150, verbose_name="nombre")),
                ("activo", models.BooleanField(default=True)),
                ("fecha_creacion", models.DateTimeField(auto_now_add=True)),
            ],
            options={
                "verbose_name": "punto de venta",
                "verbose_name_plural": "puntos de venta",
                "ordering": ["codigo"],
            },
        ),
        migrations.CreateModel(
            name="Tecnico",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nombre", models.CharField(max_length=120, unique=True)),
                ("activo", models.BooleanField(default=True)),
            ],
            options={
                "verbose_name": "técnico",
                "verbose_name_plural": "técnicos",
                "ordering": ["nombre"],
            },
        ),
        migrations.CreateModel(
            name="Pendiente",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "codigo",
                    models.CharField(
                        blank=True, editable=False, max_length=20, unique=True
                    ),
                ),
                ("titulo", models.CharField(max_length=160)),
                ("detalle", models.TextField()),
                (
                    "prioridad",
                    models.CharField(
                        choices=[
                            ("BAJA", "Baja"),
                            ("MEDIA", "Media"),
                            ("ALTA", "Alta"),
                        ],
                        default="MEDIA",
                        max_length=10,
                    ),
                ),
                (
                    "estado",
                    models.CharField(
                        choices=[("PENDIENTE", "Pendiente"), ("RESUELTO", "Resuelto")],
                        default="PENDIENTE",
                        max_length=12,
                    ),
                ),
                ("nota_solucion", models.TextField(blank=True)),
                ("fecha_registro", models.DateTimeField(auto_now_add=True)),
                ("fecha_resolucion", models.DateTimeField(blank=True, null=True)),
                (
                    "categoria",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="pendientes",
                        to="pendientes.categoria",
                    ),
                ),
                (
                    "punto_venta",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="pendientes",
                        to="pendientes.puntoventa",
                    ),
                ),
                (
                    "tecnico_resolvio",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="pendientes_resueltos",
                        to="pendientes.tecnico",
                    ),
                ),
            ],
            options={"ordering": ["estado", "-fecha_registro"]},
        ),
    ]
