from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from typing import List 
from src.pdf_operations import merge_pdfs, split_pdf
import os
from datetime import datetime
from zipfile import ZipFile
import shutil

app = FastAPI()

# Agrega una ruta estática para servir archivos CSS o JavaScript (opcional)
app.mount("/static", StaticFiles(directory="src/static"), name="static")

# Ruta para servir la web
@app.get("/", response_class=HTMLResponse)
async def serve_merge_page():
    with open("src/templates/index.html", "r") as file:
        content = file.read()
    return HTMLResponse(content)

# Ruta para servir la página de fusión
@app.get("/merge", response_class=HTMLResponse)
async def serve_merge_page():
    with open("src/templates/merge.html", "r") as file:
        content = file.read()
    return HTMLResponse(content)

# Ruta para servir la página de división
@app.get("/split", response_class=HTMLResponse)
async def serve_split_page():
    with open("src/templates/split.html", "r") as file:
        content = file.read()
    return HTMLResponse(content)

@app.post("/merge_pdfs/")
async def merge_uploaded_pdfs(pdf_files: List[UploadFile] = File(...)):
    # Guarda los PDFs subidos temporalmente
    temp_paths = []
    os.makedirs("temp", exist_ok=True)
    for pdf_file in pdf_files:
        temp_path = f"temp/{pdf_file.filename}"
        with open(temp_path, "wb") as temp_pdf:
            temp_pdf.write(pdf_file.file.read())
        temp_paths.append(temp_path)
        
    # Genera un nombre único basado en el timestamp
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    output_filename = f"output/mergepdf_{timestamp}.pdf"
        
    # Realiza la operación de fusión
    try:
        os.makedirs("output", exist_ok=True)
        merge_pdfs(temp_paths, output_filename)
        response = FileResponse(output_filename, headers={"Content-Disposition": f"attachment; filename=mergepdf_{timestamp}.pdf"})
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        # Elimina los archivos temporales
        for temp_path in temp_paths:
            os.remove(temp_path)


@app.post("/split_pdf/")
async def split_uploaded_pdf(pdf_file: UploadFile = File(...)):
    # Guarda el PDF subido temporalmente
    os.makedirs("temp", exist_ok=True)
    temp_path = f"temp/{pdf_file.filename}"
    with open(temp_path, "wb") as temp_pdf:
        temp_pdf.write(pdf_file.file.read())
        
    # Genera un nombre único para los archivos resultantes
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    output_folder = f"temp/split_{timestamp}"
    os.makedirs(output_folder, exist_ok=True)

    # Realiza la operación de división
    try:
        split_pdf(temp_path, output_folder)
        # Combina los archivos resultantes en un archivo ZIP
        result_files = os.listdir(output_folder)
        zip_filename = f"output/split_{timestamp}.zip"
        os.makedirs("output", exist_ok=True)

        with ZipFile(zip_filename, 'w') as zipf:
            for file in result_files:
                zipf.write(os.path.join(output_folder, file), arcname=file)

        # Retorna el archivo ZIP como una respuesta de archivo
        return FileResponse(zip_filename, media_type='application/zip', headers={"Content-Disposition": f'attachment; filename=split_{timestamp}.zip'})
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
    # Elimina los archivos temporales
        os.remove(temp_path)
        shutil.rmtree(output_folder)  # Elimina la carpeta de archivos resultantes
