# TelegramBotMonitor

Bot de Telegram que monitorea cambios en sitios web y envía notificaciones cuando encuentra texto específico. Diseñado específicamente para monitorear la página de Mifuturo.cl en busca de actualizaciones sobre datos de matrícula del año 2025.

## Requisitos

- Python 3.12 (requerido por compatibilidad con las dependencias)
- Token de Bot de Telegram
- Acceso a internet para realizar scraping web

## Estructura del Proyecto

### Archivos Principales

- **bot.py**: Punto de entrada principal. Configura y ejecuta el bot de Telegram con sus comandos y tareas programadas.
- **scrapper.py**: Contiene la lógica para realizar scraping web y buscar texto específico en la página objetivo.
- **users.py**: Gestiona el almacenamiento persistente de IDs de chat de usuarios registrados para recibir notificaciones.

### Archivos de Configuración

- **requirements.txt**: Lista todas las dependencias de Python necesarias para el proyecto.
- **Dockerfile**: Configuración para crear una imagen Docker del bot usando Python 3.12.
- **.gitignore**: Configuración para excluir archivos específicos del control de versiones (incluye configuraciones de Fly.io).
- **fly.toml**: Configuración para el despliegue en Fly.io (no incluido en el repositorio).

## Funcionalidades

- **Registro de Usuarios**: Los usuarios pueden registrarse enviando cualquier mensaje o usando el comando `/start`.
- **Cancelación de Registro**: Los usuarios pueden dejar de recibir notificaciones con el comando `/stop`.
- **Monitoreo Automático**: El bot verifica la página web cada N minutos.
- **Notificaciones**: Envía alertas a todos los usuarios registrados cuando encuentra el texto especificado en la página.
- **Mensajes Diarios**: Envía un mensaje diario a las 13:00 UTC (9:00 AM CL) para confirmar que el bot sigue activo.

## Almacenamiento de Datos

Los IDs de chat de los usuarios se almacenan en un archivo de texto persistente ubicado en `/data/users.txt`.

## Despliegue

El proyecto está configurado para ser desplegado en Fly.io utilizando Docker. El contenedor Docker incluye:

- Imagen base de Python 3.12 slim
- Volumen persistente para almacenar los datos de usuarios
- Exposición del puerto 8080 para posibles funcionalidades web futuras

## Variables de Entorno

- `BOT_TOKEN`: Token de autenticación para el bot de Telegram

## Ejecución Local

1. Clonar el repositorio
2. Crear un archivo `.env` con la variable `BOT_TOKEN`
3. Instalar dependencias: `pip install -r requirements.txt`
4. Ejecutar: `python bot.py`

## Ejecución en Docker

```bash
docker build -t botmonitor .
docker run -v ./data:/data -e BOT_TOKEN=your_token botmonitor
```
