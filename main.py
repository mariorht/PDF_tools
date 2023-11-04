from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from typing import List 
from pdf_operations import merge_pdfs, split_pdf
import os
from datetime import datetime


app = FastAPI()

# Agrega una ruta estática para servir archivos CSS o JavaScript (opcional)
app.mount("/static", StaticFiles(directory="static"), name="static")

# Ruta para servir la interfaz web
@app.get("/", response_class=HTMLResponse)
async def serve_merge_page():
    with open("templates/merge.html", "r") as file:
        content = file.read()
    return HTMLResponse(content)

@app.post("/merge_pdfs/")
async def merge_uploaded_pdfs(pdf_files: List[UploadFile] = File(...)):
    # Guarda los PDFs subidos temporalmente
    temp_paths = []
    for pdf_file in pdf_files:
        temp_path = f"temp/{pdf_file.filename}"
        with open(temp_path, "wb") as temp_pdf:
            temp_pdf.write(pdf_file.file.read())
        temp_paths.append(temp_path)
        
    # Genera un nombre único basado en el timestamp
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    output_filename = f"temp/mergepdf_{timestamp}.pdf"
        
    # Realiza la operación de fusión
    try:
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
    temp_path = f"temp/{pdf_file.filename}"
    with open(temp_path, "wb") as temp_pdf:
        temp_pdf.write(pdf_file.file.read())

    # Realiza la operación de división
    try:
        output_folder = "temp"
        os.makedirs(output_folder, exist_ok=True)
        split_pdf(temp_path, output_folder)
        return {"message": "PDF dividido correctamente"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        # Elimina el archivo temporal
        os.remove(temp_path)
