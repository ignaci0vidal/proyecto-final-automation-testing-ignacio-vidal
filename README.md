# Proyecto Final de Automation Testing

Proyecto final desarrollado en Python para automatizar pruebas web y pruebas de API.

El framework incluye pruebas con Selenium, Pytest, Requests y Behave, utilizando Page Object Model, datos externos, reportes y ejecución automática con GitHub Actions.

## Tecnologías utilizadas

- Python
- Pytest
- Selenium WebDriver
- Requests
- Behave
- pytest-html
- GitHub Actions

## Aplicaciones utilizadas

### Pruebas web

Las pruebas de interfaz se realizan sobre SauceDemo:

`https://www.saucedemo.com/`

### Pruebas de API

Las pruebas de API se realizan sobre JSONPlaceholder:

`https://jsonplaceholder.typicode.com/`

## Funcionalidades automatizadas

### Pruebas UI

- Login exitoso.
- Login con usuario bloqueado.
- Login con contraseña incorrecta.
- Datos de prueba parametrizados desde CSV.
- Agregar un producto al carrito.
- Validar el contador del carrito.
- Eliminar un producto del carrito.
- Validar que el carrito quede vacío.

### Pruebas API

- Consulta de un recurso con GET.
- Creación de un recurso con POST.
- Actualización de un recurso con PATCH.
- Eliminación de un recurso con DELETE.

### BDD con Behave

Se incluyen escenarios de login escritos en Gherkin:

- Inicio de sesión exitoso.
- Inicio de sesión con usuario bloqueado.

## Estructura principal

```text
data/
    users.csv

features/
    steps/
    environment.py
    login.feature

pages/
    login_page.py
    inventory_page.py
    cart_page.py

tests/
    test_login.py
    test_cart.py

tests_api/
    test_jsonplaceholder_api.py

utils/
    data_reader.py
    driver_factory.py
    logger.py
    saucedemo_helpers.py
```

## Instalación

Clonar el repositorio:

```bash
git clone https://github.com/ignaci0vidal/proyecto-final-automation-testing-ignacio-vidal.git
```

Ingresar al proyecto:

```bash
cd proyecto-final-automation-testing-ignacio-vidal
```

Crear el entorno virtual:

```powershell
py -m venv .venv
```

Activarlo en Windows:

```powershell
.\.venv\Scripts\Activate.ps1
```

Instalar las dependencias:

```powershell
pip install -r requirements.txt
```

## Ejecución

Ejecutar todos los tests de Pytest:

```powershell
py -m pytest -v
```

Ejecutar solamente pruebas UI:

```powershell
py -m pytest -m ui -v
```

Ejecutar solamente pruebas API:

```powershell
py -m pytest -m api -v
```

Ejecutar los escenarios de Behave:

```powershell
py -m behave
```

## Reportes y evidencias

Pytest genera un reporte HTML en:

```text
reports/report.html
```

Los logs se guardan en:

```text
logs/
```

Ante un fallo de interfaz, se genera una captura de pantalla en:

```text
reports/screenshots/
```

## Integración continua

El proyecto utiliza GitHub Actions para ejecutar automáticamente:

- Tests de Pytest.
- Escenarios de Behave.
- Chrome en modo headless.
- Generación de reportes y logs.
- Carga de evidencias como artifacts.

## Resultado actual

```text
Pytest: 10 tests aprobados
Behave: 2 escenarios aprobados
GitHub Actions: pipeline aprobado
```

## Autor

Ignacio Vidal
