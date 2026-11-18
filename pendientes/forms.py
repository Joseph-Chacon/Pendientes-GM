from django import forms
from .models import Pendiente, PuntoVenta, Tecnico


class PendienteForm(forms.ModelForm):
    class Meta:
        model = Pendiente
        fields = ("titulo", "detalle", "punto_venta", "prioridad")
        widgets = {
            "titulo": forms.TextInput(attrs={"placeholder": "Ej. Monitor no enciende"}),
            "detalle": forms.Textarea(
                attrs={
                    "rows": 5,
                    "placeholder": "Describa el problema y datos relevantes.",
                }
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["punto_venta"].queryset = PuntoVenta.objects.filter(activo=True)
        for name, field in self.fields.items():
            field.widget.attrs["class"] = (
                "form-select"
                if name in ("punto_venta", "prioridad")
                else "form-control"
            )


class ResolverPendienteForm(forms.ModelForm):
    class Meta:
        model = Pendiente
        fields = ("tecnico_resolvio", "nota_solucion")
        widgets = {
            "nota_solucion": forms.Textarea(
                attrs={
                    "rows": 4,
                    "placeholder": "Indique brevemente la solución aplicada (opcional).",
                }
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["tecnico_resolvio"].queryset = Tecnico.objects.filter(activo=True)
        self.fields["tecnico_resolvio"].widget.attrs["class"] = "form-select"
        self.fields["nota_solucion"].widget.attrs["class"] = "form-control"


class PuntoVentaForm(forms.ModelForm):
    class Meta:
        model = PuntoVenta
        fields = ("codigo", "nombre")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs["class"] = "form-control"


class NombreCatalogoForm(forms.ModelForm):
    class Meta:
        fields = ("nombre",)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["nombre"].widget.attrs["class"] = "form-control"


class TecnicoForm(NombreCatalogoForm):
    class Meta(NombreCatalogoForm.Meta):
        model = Tecnico
