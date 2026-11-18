from django.test import TestCase
from django.urls import reverse
from .models import Pendiente, PuntoVenta, Tecnico


class PendienteFlowTests(TestCase):
    def setUp(self):
        self.punto = PuntoVenta.objects.create(
            codigo="MSV", nombre="Materiales San Vito"
        )
        self.tecnico = Tecnico.objects.create(nombre="Técnico de prueba")

    def test_registro_asigna_codigo_estado_y_fecha(self):
        response = self.client.post(
            reverse("pendientes:crear"),
            {
                "titulo": "Monitor no enciende",
                "detalle": "El monitor del área de cajas no muestra imagen.",
                "punto_venta": self.punto.pk,
                "prioridad": Pendiente.Prioridad.ALTA,
            },
        )
        pendiente = Pendiente.objects.get()
        self.assertRedirects(
            response, reverse("pendientes:detalle", args=[pendiente.pk])
        )
        self.assertEqual(pendiente.codigo, "P-000001")
        self.assertEqual(pendiente.estado, Pendiente.Estado.PENDIENTE)
        self.assertIsNotNone(pendiente.fecha_registro)
        self.assertIsNone(pendiente.tecnico_resolvio)

    def test_resolver_guarda_tecnico_y_fecha(self):
        pendiente = Pendiente.objects.create(
            titulo="Equipo lento", detalle="Revisar equipo.", punto_venta=self.punto
        )
        response = self.client.post(
            reverse("pendientes:resolver", args=[pendiente.pk]),
            {
                "tecnico_resolvio": self.tecnico.pk,
                "nota_solucion": "Se reemplazó el disco.",
            },
        )
        pendiente.refresh_from_db()
        self.assertRedirects(
            response, reverse("pendientes:detalle", args=[pendiente.pk])
        )
        self.assertEqual(pendiente.estado, Pendiente.Estado.RESUELTO)
        self.assertEqual(pendiente.tecnico_resolvio, self.tecnico)
        self.assertIsNotNone(pendiente.fecha_resolucion)

    def test_tablero_muestra_conteo_de_abiertos(self):
        Pendiente.objects.create(
            titulo="Teclado", detalle="No funciona.", punto_venta=self.punto
        )
        response = self.client.get(reverse("pendientes:tablero"))
        self.assertContains(response, "Pendientes abiertos")
        self.assertContains(response, "MSV")

    def test_catalogos_permite_agregar_punto_venta(self):
        response = self.client.post(
            reverse("pendientes:catalogos"),
            {
                "tipo": "punto_venta",
                "punto_venta-codigo": "MCT",
                "punto_venta-nombre": "Materiales Ciudad Tejar",
            },
        )
        self.assertRedirects(response, reverse("pendientes:catalogos"))
        self.assertTrue(PuntoVenta.objects.filter(codigo="MCT").exists())
