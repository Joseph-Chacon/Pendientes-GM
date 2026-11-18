"""Carga opcional de variables locales sin depender de paquetes externos."""

import os
from pathlib import Path


def cargar_entorno(base_dir: Path) -> None:
    archivo = base_dir / ".env"
    if not archivo.exists():
        return

    for linea in archivo.read_text(encoding="utf-8").splitlines():
        linea = linea.strip()
        if not linea or linea.startswith("#") or "=" not in linea:
            continue
        clave, valor = linea.split("=", 1)
        os.environ.setdefault(clave.strip(), valor.strip().strip('"').strip("'"))
