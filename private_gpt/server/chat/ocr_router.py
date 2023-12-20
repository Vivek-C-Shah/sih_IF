from fastapi import APIRouter, UploadFile, File
import shutil
from pathlib import Path
from ocr import extract_text_from_image  # assuming you have ocr.py file with the function

router = APIRouter()

@router.post("/uploadfile/")
async def create_upload_file(file: UploadFile = File(...)):
    temp_file = Path(f"/temp/{file.filename}")
    with temp_file.open("wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    
    text = extract_text_from_image(temp_file)
    
    return {"filename": file.filename, "text": text}