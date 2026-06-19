# Proceso de desarrollo

Este documento describe el proceso completo de desarrollo del proyecto "Organizando Mi Mundo".

## 1. Planificación

El objetivo fue crear una aplicación en Python que permitiera crear, listar y completar tareas con una interfaz gráfica moderna. También se definió la necesidad de exportar datos a CSV y de estructurar el proyecto con MVC y POO.

## 2. Diseño del sistema

Se definieron los componentes principales:
- `Task` en `models/task.py` como clase modelo.
- `TaskView` en `views/task_view.py` como la interfaz de texto enriquecido.
- `TaskController` en `controllers/task_controller.py` para manejar la lógica.
- `main.py` como punto de entrada.

Se decidió usar `customtkinter` para la interfaz gráfica, `plyer` para notificaciones de escritorio y `pandas` para la exportación a CSV.

## 3. Desarrollo

### 3.1 Modelo (POO)

`Task` es una clase que guarda:
- título
- descripción
- estado de completado

La clase incluye validación del título y un método para marcar la tarea como completada.

### 3.2 Vista (Visualización)

`TaskView` utiliza `customtkinter` para:
- mostrar una ventana gráfica moderna.
- agregar tareas mediante campos de entrada.
- seleccionar y completar tareas desde una lista.
- exportar tareas a CSV mediante un diálogo de guardado.
- mostrar ventanas informativas y advertencias.

También utiliza `plyer` para enviar notificaciones de escritorio cuando se crea, completa o exporta una tarea.

### 3.3 Controlador (Lógica)

`TaskController` implementa el flujo principal:
- mostrar menú
- crear tarea
- listar tareas
- completar tarea
- exportar tareas a CSV
- salir

La vista y el modelo se mantienen separados en sus responsabilidades.

## 4. Pruebas

Se usó `pytest` para crear pruebas unitarias en `tests/test_task.py`:
- prueba válida de creación de tarea.
- prueba válida de marcar como completada.
- prueba inválida para el caso de título vacío usando `pytest.raises`.

También se agregó `tests/conftest.py` para configurar el `PYTHONPATH` de las pruebas.

## 5. Documentación

Se incluyó esta documentación y un diagrama de clases en Mermaid en `docs/diagrama_clases.mmd`.

## 6. Control de versiones

Se recomienda usar Git con commits claros como:
- `git commit -m "Inicializa proyecto con estructura MVC"`
- `git commit -m "Agrega exportación a CSV con pandas"`
- `git commit -m "Integra CustomTkinter para interfaz gráfica"`
- `git commit -m "Agrega pruebas unitarias con pytest"`

## 7. Resultados

El proyecto cumple con los requisitos del curso:
- Python
- POO
- MVC
- librerías externas
- pruebas con `pytest`
- documentación y diagrama de clases
- lista para subir a GitHub

## 8. Instrucciones de entrega

1. Asegúrate de haber ejecutado las pruebas.
2. Guarda las capturas de pantalla en `docs/screenshots/`.
3. Sube el repositorio a GitHub.
4. Comparte el enlace del repositorio con el profesor.

## Anexos: comprobaciones y capturas recomendadas

Antes de entregar, toma las siguientes capturas y guárdalas en `docs/screenshots/`:

- `estructura_proyecto.png`: el explorador de archivos de VS Code mostrando `src/`, `tests/`, `docs/`, `requirements.txt` y `README.md`.
- `instalacion_dependencias.png`: terminal con el comando `python -m pip install -r requirements.txt` y salida exitosa.
- `ejecucion_programa.png`: terminal mostrando la ejecución de `python src/organizando_mi_mundo/main.py` con el menú principal visible.
- `pruebas_pytest.png`: terminal mostrando `pytest` con "5 passed".
- `diagrama_clases.png`: archivo `docs/diagrama_clases.mmd` abierto en el editor (o exportado a imagen) mostrando las clases.
- `readme_abierto.png`: ventana del editor con `README.md` visible (encabezado e instrucciones de ejecución).

Con estas capturas se evidencian los requisitos funcionales, la estructura del proyecto y la documentación necesaria para la entrega.
