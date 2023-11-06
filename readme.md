# PDF Tools

This project is a FastAPI-based API that provides operations for merging and splitting PDF files. It also includes a simple web interface for interacting with the API.

## Usage Instructions

1. Make sure you have Python and the dependencies installed by running `pip install -r requirements.txt`.
2. Run the server using the command `./start_server.sh`.
3. Access the web interface in your browser by visiting `http://localhost:8080`.

## Supported Operations

### Merge PDFs

1. Go to the merge page on the web interface.
2. Select the PDF files you want to merge.
3. Click the "Merge PDFs" button.
4. The merged file will be downloaded automatically.

### Split PDFs

1. Go to the split page on the web interface.
2. Select the PDF file you want to split.
3. Click the "Split PDF" button.
4. A ZIP file with individual pages will be generated and downloaded automatically.

## Tests

To run the tests, use the command `make test` or run `./run_tests.sh`.

## Running with Docker

1. Make sure you have Docker installed on your system.
2. Open a terminal and navigate to the project directory.
3. Build the Docker image using the following command:

   ```bash
   docker-compose build

4. Run the Docker container with the following command:

   ```bash
   docker-compose up

