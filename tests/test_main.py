import os
from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

def test_serve_index_page():
    response = client.get("/")
    assert response.status_code == 200
    assert response.headers["content-type"] == "text/html; charset=utf-8"

def test_serve_merge_page():
    response = client.get("/merge")
    assert response.status_code == 200
    assert response.headers["content-type"] == "text/html; charset=utf-8"
    
def test_serve_split_page():
    response = client.get("/split")
    assert response.status_code == 200
    assert response.headers["content-type"] == "text/html; charset=utf-8"

def test_merge_pdfs():
    # Simula una carga de archivos para fusionar
    files = [
        ("pdf_files", ("test1.pdf", open("tests/test_files/test1.pdf", "rb"), "application/pdf")),
        ("pdf_files", ("test2.pdf", open("tests/test_files/test2.pdf", "rb"), "application/pdf"))
    ]

    response = client.post("/merge_pdfs/", files=files)

    # Verifica que la respuesta tenga el código 200
    assert response.status_code == 200
    # Verifica que la respuesta sea un archivo PDF
    assert response.headers["content-type"] == "application/pdf"

def test_split_pdf():
    # Simula la carga de un archivo para dividir
    file = [
        ("pdf_file", ("test3.pdf", open("tests/test_files/test3.pdf", "rb"), "application/pdf"))
    ]

    response = client.post("/split_pdf/", files=file)

    # Verifica que la respuesta tenga el código 200
    assert response.status_code == 200
    # Verifica que la respuesta sea un archivo zip
    assert response.headers["content-type"] == "application/zip"
    

