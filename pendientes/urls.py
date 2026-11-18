from django.urls import path
from . import views

app_name = "pendientes"

urlpatterns = [
    path("", views.tablero, name="tablero"),
    path("pendientes/", views.lista_pendientes, name="lista"),
    path("pendientes/nuevo/", views.crear_pendiente, name="crear"),
    path("pendientes/<int:pk>/", views.detalle_pendiente, name="detalle"),
    path("pendientes/<int:pk>/resolver/", views.resolver_pendiente, name="resolver"),
    path("catalogos/", views.catalogos, name="catalogos"),
]
