<div align="center">
    <h1>backend | CRM</h1>
    <p align="center">
        backend para el proyeto CRM.
    </p>
</div>

## Endpoints

`http://localhost:8000/app`.

## Postman
Documentación(Users y Auth): https://documenter.getpostman.com/view/32158417/2s9YsGjDgn
Documentación (Cliente y Ventas): https://documenter.getpostman.com/view/23822071/2s9YsKfXXa
---

## Módulos
- Módulo de Autenticación

## Tecnologías

Este proyecto utiliza las siguientes tecnologías:

- Django 3.2.23
- djangorestframework
- Python 3.11.0 importante tener esta version
- https://www.python.org/downloads/release/python-3110/

## Cómo levantar el proyecto en WINDOWS

1. Clona el repositorio.

```bash
git clone https://github.com/SistemaCRM-ConsigueVentas/CRM_Backend
```

```bash
cd CRM_Backend
```
2. Crea y activa el entorno virtual.

```bash
python -m venv myenv
```
```bash
myenv\Scripts\Activate
```

3. Instala las dependencias.

```bash
pip install -r requirements.txt
```

4. Ejecuta el comando `python manage.py runserver` para iniciar el servidor.


## Cómo levantar el proyecto en LINUX

1. Clona el repositorio.

```bash
git clone https://github.com/SistemaCRM-ConsigueVentas/CRM_Backend
```

```bash
cd CRM_Backend
```
2. Crea y activa el entorno virtual.

```bash
python3 -m venv myenv
```
```bash
source myenv/bin/activate
```

3. Instala las dependencias.

```bash
pip install -r requirements.txt
```

4. Ejecuta el comando `python3 manage.py runserver` para iniciar el servidor.