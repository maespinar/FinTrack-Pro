# FinTrack Pro - Sistema de Auditoría Financiera

![Python Version](https://img.shields.io/badge/Python-3.14.5%2B-blue)
![Architecture](https://img.shields.io/badge/Architecture-Modular-success)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)

FinTrack Pro es una aplicación de consola de nivel empresarial desarrollada en Python, diseñada para registrar, auditar y consolidar activos financieros internacionales. 
Este proyecto demuestra la aplicación de principios sólidos de ingeniería de software, enfocándose en la escalabilidad, la protección de datos y una experiencia de usuario robusta en terminal.

## Características Principales:

* **Arquitectura Modular (Paquetes y Módulos):** Separación estricta de responsabilidades entre la capa de presentación (CLI) y la lógica de negocio, facilitando el mantenimiento y la escalabilidad.
* **Programación Orientada a Objetos Avanzada:** Implementación de herencia, polimorfismo y encapsulamiento estricto (`@property` y `@setter`) para garantizar la integridad de los datos financieros.
* **Programación Defensiva y Manejo de Errores:** Uso de excepciones personalizadas (`TickerDuplicadoError`) y bloques `try-except` para prevenir caídas del sistema ante entradas de datos corruptas o inválidas.
* **Formatos Dinámicos de Reportes:** Generación de tablas ASCII elegantes y formateo de divisas dinámico utilizando la librería externa `tabulate`.

## Arquitectura del Proyecto

El proyecto sigue una estructura limpia de separación por paquetes:
```text
fintrack_pro/
├── app.py                  # Controlador principal  
├── requirements.txt        # Manifiesto de dependencias
└── finanzas/               # Paquete de lógica de negocio
    ├── __init__.py         # Definición de la API Pública del paquete 
    ├── activos.py          # Modelado de datos 
    └── portafolio.py       # Motor de almacenamiento, filtrado y cálculos matemáticos
```

# Instalación y Configuración:
Sigue estos pasos para desplegar el proyecto en tu entorno local de forma aislada (Bash)

1. Clonar el repositorio
   ```text
   git clone [https://github.com/TU_USUARIO/fintrack_pro.git](https://github.com/TU_USUARIO/fintrack_pro.git)
   cd fintrack_pro
   ```
3. Crear y activar el entorno virtual
    ```text
    # Windows
    python -m venv venv
    venv\Scripts\activate
    # Mac/Linux
    python -m venv venv
    source venv/bin/activate
    ```
5. Instalar dependencias
    ```text
    pip install -r requirements.txt
    ```
7. Ejecutar el sistema
    ```text
    python app.py
    ```

# Conceptos Técnicos Aplicados

Integración entre Diccionarios y Objetos: Transformación dinámica de instancias de clase a diccionarios en tiempo de ejecución para la generación de reportes matriciales.
F-Strings Avanzados: Formateo de datos numéricos flotantes a estándares monetarios internacionales ($1,500.00).
Control de Flujo Optimizado: Uso de la estructura match-case de Python 3.14.5+ para un enrutamiento de menú rápido y legible.

Desarrollado con 💻 y buenas prácticas de Clean Code.
