# Python System Monitor

Monitor interactivo de recursos del sistema en tiempo real para la terminal, desarrollado en Python con una arquitectura modular. Utiliza `psutil` para consultar métricas de hardware y procesos activos, y `rich` para renderizar una interfaz visual dinámica en consola.

## Arquitectura del Proyecto

El proyecto está organizado en módulos independientes para mantener una separación clara de responsabilidades, facilitar el mantenimiento y permitir futuras ampliaciones.

```text
python-system-monitor/
├── .gitignore
├── LICENSE
├── README.md
├── requirements.txt
└── src/
    ├── __init__.py
    ├── system_info.py
    ├── layout.py
    └── main.py
```

### Descripción de los módulos

- **`src/__init__.py`**: Define el directorio `src` como un paquete de Python.
- **`src/system_info.py`**: Se encarga de consultar las métricas del sistema mediante `psutil`, incluyendo el uso de CPU, memoria RAM, almacenamiento y procesos activos.
- **`src/layout.py`**: Construye y organiza los elementos visuales de la interfaz de terminal utilizando `rich`, como paneles, tablas y componentes de información.
- **`src/main.py`**: Es el punto de entrada de la aplicación. Coordina los módulos, administra el ciclo de actualización de las métricas y controla la ejecución del monitor.
- **`requirements.txt`**: Contiene las dependencias necesarias para ejecutar el proyecto.
- **`.gitignore`**: Especifica los archivos y directorios que Git debe excluir del control de versiones.
- **`LICENSE`**: Contiene los términos de distribución y uso del proyecto.
- **`README.md`**: Documenta la arquitectura, las características y las instrucciones de instalación y ejecución.

## Características principales

- **Monitoreo de CPU:** Consulta el porcentaje de utilización del procesador.
- **Monitoreo de memoria RAM:** Muestra información sobre el consumo y la disponibilidad de memoria.
- **Monitoreo de almacenamiento:** Permite consultar información sobre el espacio utilizado y disponible en disco.
- **Monitor de procesos:** Identifica los cinco procesos con mayor consumo de memoria RAM.

## Requisitos previos

Antes de instalar el proyecto, asegúrate de contar con los siguientes componentes:

- Python 3.8 o superior.
- Git para clonar el repositorio.
- Una terminal compatible con la interfaz de `rich`.
- Conexión a Internet para instalar las dependencias.

## Instalación y uso

### 1. Clonar el repositorio

Clona el repositorio desde GitHub y accede al directorio del proyecto.

```bash
git clone https://github.com/tu-usuario/python-system-monitor.git
cd python_system_monitor
```

Reemplaza `tu-usuario` por el nombre de tu cuenta de GitHub.

### 2. Instalar las dependencias

- una vez estes en la carpeta raiz, ejecuta:

```bash
python -m pip install -r requirements.txt
```

Este comando instala las bibliotecas necesarias para el funcionamiento de la aplicación.

Las dependencias principales son:

- `psutil`: permite obtener información sobre el hardware, el uso de recursos y los procesos del sistema.
- `rich`: proporciona herramientas para construir interfaces visuales en la terminal.

### 3. Ejecutar la aplicación

Desde el directorio src del proyecto, ejecuta:

```bash
python main.py
```

Para finalizar la ejecución, utiliza `Ctrl+C` en la terminal.

## Tecnologías utilizadas

- **Python:** lenguaje de programación principal.
- **psutil:** consulta de métricas del sistema y administración de procesos.
- **Rich:** presentación de información y componentes visuales en terminal.
- **Git:** control de versiones.
- **GitHub:** alojamiento y colaboración en el repositorio.

---

Desarrollado como un proyecto de Python enfocado en el monitoreo de recursos del sistema y la creación de interfaces interactivas en consola.
