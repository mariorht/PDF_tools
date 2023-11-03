import os
from fastapi.testclient import TestClient
from main import app
client = TestClient(app)

def test_merge_pdfs():
    # Simula una carga de archivos para fusionar
    files = [
        ("pdf_files", ("test1.pdf", open("tests/test_files/test1.pdf", "rb"), "application/pdf")),
        ("pdf_files", ("test2.pdf", open("tests/test_files/test2.pdf", "rb"), "application/pdf"))
    ]

    response = client.post("/merge_pdfs/", files=files)

    assert response.status_code == 200
    # assert os.path.exists("output.pdf")

def test_split_pdf():
    # Simula la carga de un archivo para dividir
    file = [
        ("pdf_file", ("test3.pdf", open("tests/test_files/test3.pdf", "rb"), "application/pdf"))
    ]

    response = client.post("/split_pdf/", files=file)

    assert response.status_code == 200
    # assert os.path.exists("output/page_1.pdf")
    # assert os.path.exists("output/page_2.pdf")
