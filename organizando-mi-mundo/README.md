# 🌍 Organizando Mi Mundo 📚✅

## ¿Qué hace este programa?

Organizando Mi Mundo es una aplicación de escritorio creada con Python para gestionar tareas escolares y personales.

La aplicación permite:

- Crear tareas con título.
- Registrar una fecha de vencimiento obligatoria.
- Añadir una hora opcional.
- Marcar tareas como completadas.
- Exportar las tareas a un archivo CSV.
- Enviar notificaciones de escritorio cuando llegue el día de vencimiento.
- Reproducir avisos hablados con voz.

---

## Con qué se hizo

La aplicación se desarrolló usando el patrón **MVC** (Modelo-Vista-Controlador). Esto permite separar la lógica del programa, la interfaz de usuario y la gestión de datos.

### Funciones y módulos principales

- `Task`: representa una tarea individual, con título, descripción, fecha y hora.
- `TaskManager`: administra la lista de tareas y permite agregarlas, listarlas y completarlas.
- `TaskView`: construye la interfaz gráfica con `customtkinter`.
- `TaskController`: valida datos, controla el flujo de la aplicación y mantiene sincronizada la vista y el modelo.
- `parse_due_datetime`: valida la fecha obligatoria y la hora opcional.
- `check_due_tasks`: revisa periódicamente si alguna tarea alcanzó su fecha de vencimiento y dispara notificaciones.

---

## Tecnologías usadas

- `customtkinter`: para crear la interfaz gráfica.
- `plyer`: para mostrar notificaciones de escritorio.
- `pyttsx3`: para avisos hablados.
- `pandas`: para exportar tareas a CSV.
- `pytest`: para pruebas unitarias.

---

## Cómo se usa

1. Ejecuta la aplicación con `python src/organizando_mi_mundo/main.py`.
2. Escribe el título de la tarea.
3. Ingresa la fecha en formato `dd/mm/aaaa`.
4. Opcionalmente, escribe la hora en formato `HH:MM`.
5. Presiona "Agregar tarea".
6. Selecciona una tarea y presiona "Marcar completada".
7. Presiona "Exportar a CSV" para guardar las tareas.

---

## Por qué cumple los requisitos

- Tiene interfaz gráfica, tal como pide el profesor.
- Usa librerías externas (`customtkinter`, `plyer`, `pyttsx3`, `pandas`).
- Permite fecha obligatoria y hora opcional.
- Envía notificaciones cuando entra el día de vencimiento.
- Está organizado con MVC.
- Incluye pruebas unitarias.

---

## Ejecución y pruebas

Instalación de dependencias:

```bash
pip install -r requirements.txt
```

Ejecución:

```bash
python src/organizando_mi_mundo/main.py
```

Pruebas:

```bash
python -m pytest -q
```

---

## Archivos clave

- `src/organizando_mi_mundo/main.py`: inicia la aplicación.
- `src/organizando_mi_mundo/controllers/task_controller.py`: control de la aplicación.
- `src/organizando_mi_mundo/models/task.py`: modelo de tarea.
- `src/organizando_mi_mundo/models/task_manager.py`: gestor de tareas.
- `src/organizando_mi_mundo/views/task_view.py`: interfaz gráfica.

---

## Nota final

Esta aplicación está lista para entregar como trabajo final con interfaz gráfica, manejo de fechas, notificaciones y voz.
