# 🌍 ORGANIZANDO MI MUNDO 📚✅

## Integrante

* 👨‍💻 José Rodríguez Escobar

---

## 📖 Descripción del Proyecto

**Organizando Mi Mundo** es una aplicación de consola desarrollada en **Python 🐍** para ayudar a los estudiantes a gestionar sus tareas académicas y personales.

La aplicación ofrece una experiencia rápida y clara en la terminal, con funciones para:

- ✅ Crear tareas.
- 📋 Listar todas las tareas.
- ✔️ Marcar tareas como completadas.
- 📄 Exportar tareas a un archivo CSV.

El proyecto está diseñado con **Programación Orientada a Objetos (POO)** y la arquitectura **MVC (Modelo - Vista - Controlador)** para mantener la lógica separada, el código legible y fácil de mantener.

---

## 🚀 Resumen

Esta solución permite organizar el trabajo diario de forma simple y eficiente desde la terminal, con una estructura enfocada en:

- Modularidad.
- Reutilización de código.
- Pruebas unitarias.
- Interfaz más agradable con `rich`.

---

## 🧩 Características principales

- Crear tareas con título y descripción.
- Ver el estado de cada tarea.
- Completar tareas y actualizar su estado.
- Exportar el listado completo a un archivo CSV.
- Validación de entradas para evitar datos erróneos.

---

## 🛠️ Tecnologías utilizadas

| Tecnología      | Uso                        |
| --------------- | -------------------------- |
| 🐍 Python       | Lenguaje principal         |
| 🎨 Rich         | Interfaz visual en consola |
| 📊 Pandas       | Exportación de datos a CSV |
| 🧪 Pytest       | Pruebas unitarias          |
| 🌐 Git y GitHub | Control de versiones       |

---

## 🏛️ Arquitectura del proyecto

El proyecto sigue el patrón **MVC**:

- **Modelo:** maneja datos y reglas de negocio (`Task`, `TaskManager`).
- **Vista:** presenta la información en consola (`TaskView`).
- **Controlador:** dirige las acciones del usuario y enlaza modelo y vista (`TaskController`).

---

## 📁 Estructura del proyecto

- `src/organizando_mi_mundo/main.py` — Punto de entrada de la aplicación.
- `src/organizando_mi_mundo/controllers/task_controller.py` — Lógica de flujo y comandos.
- `src/organizando_mi_mundo/models/task.py` — Definición del modelo de tarea.
- `src/organizando_mi_mundo/models/task_manager.py` — Gestión de la colección de tareas.
- `src/organizando_mi_mundo/views/task_view.py` — Presentación en consola.
- `tests/` — Pruebas unitarias con Pytest.

---

## ⚙️ Instalación y ejecución

1. Clona el repositorio.
2. Abre una terminal en la carpeta del proyecto.
3. Instala dependencias:

```bash
pip install -r requirements.txt
```

4. Ejecuta la aplicación:

```bash
python src/organizando_mi_mundo/main.py
```

---

## 🧪 Pruebas

Para ejecutar las pruebas unitarias usa:

```bash
pytest
```

Se incluyen pruebas para:

- Creación y validación de tareas.
- Completar tareas.
- Listado y almacenamiento de tareas.

---

## 📸 Evidencias del proyecto

Las capturas del flujo de uso se encuentran en `organizando-mi-mundo/docs/screenshots/`.

![Prueba 1](https://github.com/jose10-2008/Organizando-mi-mundo-1/raw/main/organizando-mi-mundo/docs/screenshots/1era_prueba.png)

![Prueba 2](https://github.com/jose10-2008/Organizando-mi-mundo-1/raw/main/organizando-mi-mundo/docs/screenshots/2da_prueba.png)

![Prueba 3](https://github.com/jose10-2008/Organizando-mi-mundo-1/raw/main/organizando-mi-mundo/docs/screenshots/3er_prueba.png)

![Prueba 4](https://github.com/jose10-2008/Organizando-mi-mundo-1/raw/main/organizando-mi-mundo/docs/screenshots/4ta_prueba.png)

![Prueba 4 - parte 2](https://github.com/jose10-2008/Organizando-mi-mundo-1/raw/main/organizando-mi-mundo/docs/screenshots/4ta_prueba_parte2.png)

![Cierre del programa](https://github.com/jose10-2008/Organizando-mi-mundo-1/raw/main/organizando-mi-mundo/docs/screenshots/5ta_prueba_final.png)

---

## 🏆 Conclusión

El proyecto demuestra una implementación sólida de una aplicación de tareas con **POO**, **MVC** y pruebas unitarias. Además, mejora la presentación en consola y permite exportar los resultados a CSV.

---

## 📌 Nota final

Este repositorio está preparado para ser evaluado como entrega final, con documentación clara, pruebas y un flujo de trabajo completo.

---

# 🚀 ¡Gracias por usar Organizando Mi Mundo! 🌍📚✨
