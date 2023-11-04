# PDF Tools

Este proyecto es una API basada en FastAPI que proporciona operaciones para fusionar y dividir archivos PDF. También incluye una interfaz web simple para interactuar con la API.

## Instrucciones de Uso

1. Asegúrate de tener Python y las dependencias instaladas ejecutando `pip install -r requirements.txt`.
2. Ejecuta el servidor con el comando `./start_server.sh`.
3. Accede a la interfaz web en tu navegador visitando `http://localhost:8000`.

## Operaciones Soportadas

### Fusionar PDFs

1. Accede a la página de fusión en la interfaz web.
2. Selecciona los archivos PDF que deseas fusionar.
3. Haz clic en el botón "Fusionar PDFs".
4. El archivo fusionado se descargará automáticamente.

### Dividir PDFs

1. Accede a la página de división en la interfaz web.
2. Selecciona el archivo PDF que deseas dividir.
3. Haz clic en el botón "Dividir PDF".
4. Se generará un archivo ZIP con las páginas individuales y se descargará automáticamente.

## Tests

Para ejecutar los tests, utiliza el comando `make test` o ejecuta `./run_tests.sh`.
