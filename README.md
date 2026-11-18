# Registro de Pendientes TI

MVP web para registrar y resolver pendientes técnicos de los puntos de venta de Grupo Materiales.

## Funcionalidades incluidas

- Registro de pendientes con título, detalle, punto de venta y prioridad.
- Estados limitados a `Pendiente` y `Resuelto`.
- Resolución con técnico responsable, fecha/hora automática y nota opcional.
- Tablero con conteo de pendientes abiertos por punto de venta.
- Listado con filtros por estado, punto de venta, categoría, prioridad y texto.
- Administración de puntos de venta y técnicos mediante Django Admin.

## Puesta en marcha local

1. Instale las dependencias: `python -m pip install -r requirements.txt`.
2. Cree la base de datos: `python manage.py migrate`.
3. Cree un usuario administrador: `python manage.py createsuperuser`.
4. Ejecute: `python manage.py runserver`.
5. Abra `http://127.0.0.1:8000/`.

Antes de registrar pendientes, agregue puntos de venta y técnicos en `http://127.0.0.1:8000/catalogos/`.

## PostgreSQL

La base `registro_pendientes` ya fue creada en PostgreSQL 18, puerto `5432`, con todas las tablas necesarias. La configuración local se encuentra en `.env` (archivo excluido del repositorio), por lo que al ejecutar la aplicación los datos se guardan automáticamente en PostgreSQL. El proyecto usa SQLite solo si no existen variables `DB_NAME`, `DB_USER` y `DB_PASSWORD`, con el fin de facilitar una primera demostración local.

Para iniciar la aplicación usando PostgreSQL basta con ejecutar:

```powershell
python manage.py runserver
```

Si se configura otra computadora, cree su propio `.env` a partir de `.env.example` o configure las variables en la sesión de PowerShell (no guarde la contraseña en el repositorio):

```powershell
$env:DB_NAME = "registro_pendientes"
$env:DB_USER = "postgres"
$env:DB_PASSWORD = "<contraseña-de-postgresql>"
$env:DB_HOST = "localhost"
$env:DB_PORT = "5432"
python manage.py runserver
```

PostgreSQL es la configuración recomendada para pruebas compartidas y para un futuro despliegue en Azure.
