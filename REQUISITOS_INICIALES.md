# Requisitos iniciales — Registro de Pendientes TI

Documento vivo para reunir los acuerdos funcionales antes de iniciar el desarrollo.

## Objetivo

Crear una aplicación web responsive para el área de TI de una cadena de ferreterías. Debe permitir registrar y dar seguimiento a pendientes técnicos, por ejemplo: un monitor defectuoso o un equipo con el sistema operativo dañado.

La aplicación deberá poder utilizarse desde computadora y celular, y en una fase posterior podrá alojarse en Azure.

## Enfoque técnico inicial

- Aplicación web desarrollada con Python.
- Propuesta inicial de backend: Django.
- Interfaz responsive para computadora y celular (por ejemplo, Bootstrap).
- Base de datos de pruebas: PostgreSQL.
- PostgreSQL permite validar la aplicación localmente y, si se aprueba el proyecto, puede mantenerse en producción mediante Azure Database for PostgreSQL o infraestructura interna.

## Identidad visual y diseño

La interfaz deberá usar la identidad visual de Grupo Materiales y mostrar su logo, especialmente en el encabezado o pantalla de acceso de la aplicación.

- Logo de referencia: `assets/logo-grupo-materiales.png`.
- Color principal: rojo corporativo.
- Colores complementarios: blanco y amarillo corporativo.
- El diseño debe conservar una apariencia limpia y profesional, con buena legibilidad tanto en computadora como en celular.
- Se recomienda utilizar el rojo para encabezados, acciones principales y elementos de identidad; blanco para fondos y contenido; y amarillo para acentos o avisos visuales puntuales.
- No se debe comprometer la legibilidad: el texto debe usar suficiente contraste sobre los fondos de color.

## Idioma

- Todo el desarrollo orientado a las personas usuarias debe estar en español: pantallas, botones, etiquetas, mensajes de validación, documentación y datos de ejemplo.
- Los nombres técnicos internos indispensables del framework pueden permanecer en inglés cuando corresponda, pero no deberán mostrarse en la interfaz.

## Estados y flujo del pendiente

Solo existirán dos estados:

- `Pendiente`
- `Resuelto`

Flujo:

1. Se registra un pendiente y queda automáticamente con estado `Pendiente`.
2. El sistema guarda automáticamente la fecha y hora de registro.
3. No se debe guardar quién creó el pendiente.
4. Cuando el trabajo esté terminado, se cambia el estado a `Resuelto`.
5. Al resolverlo, es obligatorio seleccionar al compañero/técnico que realizó la tarea.
6. El sistema guarda automáticamente la fecha y hora de resolución.
7. Se podrá registrar una nota breve con la solución aplicada.

No se utilizará asignación previa ni la acción de “tomar pendiente”.

## Datos del pendiente

- Código interno (por definir formato).
- Título.
- Detalle.
- Punto de venta.
- Prioridad.
- Estado: `Pendiente` o `Resuelto`.
- Técnico que resolvió (solo al estar resuelto).
- Nota de solución (opcional, solo al estar resuelto).
- Fecha y hora de registro.
- Fecha y hora de resolución (solo al estar resuelto).

## Puntos de venta

Cada punto de venta tendrá:

- Identificador interno.
- Código corto único.
- Nombre.
- Estado activo/inactivo.
- Fecha de creación.

Ejemplo:

| Código | Nombre |
| --- | --- |
| MSV | Materiales San Vito |

En formularios, listados y filtros se mostrará preferiblemente como:

`MSV — Materiales San Vito`

Los puntos de venta podrán agregarse cuando sea necesario. Si uno deja de utilizarse, se marcará como inactivo para conservar el historial de pendientes relacionados.

## Consultas y filtros esperados

- Filtrar pendientes por punto de venta.
- Consultar cuántos pendientes hay por punto de venta.
- Filtrar por estado y prioridad.
- Consultar pendientes resueltos por técnico.
- Consultar fechas de registro y resolución.

## Pendientes de definición

- Catálogo de puntos de venta reales.
- Lista de compañeros/técnicos que podrán seleccionarse al resolver.
- Catálogo de prioridades.
- Formato del código interno del pendiente.
- Si se permitirá reabrir un pendiente resuelto y cómo se conservará su historial.
