"""Punto de entrada ejecutable para la aplicación "Organizando Mi Mundo".

Este módulo inicializa el `TaskController` y arranca el bucle principal de
la aplicación gráfica.

Ejecución:

    python src/organizando_mi_mundo/main.py

Nota: `conftest.py` para las pruebas añade `src/` al `PYTHONPATH`. Aquí
se añade la carpeta padre del paquete al `sys.path` solo cuando se ejecuta
directamente como script para permitir la ejecución desde la carpeta del
proyecto sin instalar el paquete.
"""

import sys
from pathlib import Path

# Añade la carpeta `src` al path cuando se ejecuta el módulo como script.
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from organizando_mi_mundo.controllers.task_controller import TaskController


def main() -> None:
    """Inicia la aplicación creando el controlador principal."""
    controller = TaskController()
    controller.run()


if __name__ == "__main__":
    main()
