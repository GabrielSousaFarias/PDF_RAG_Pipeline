from pathlib import Path
from uuid import uuid4

from fastapi import UploadFile

from app.config import settings


def save_uploaded_pdf(file: UploadFile) -> dict:

    file_id = str(uuid4())
    file_path = Path(settings.upload_dir) / f"{file_id}.pdf"

    with open(file_path, "wb") as buffer:
        buffer.write(file.file.read())

    return {
        "file_id": file_id,
        "original_filename": file.filename,
        "file_path": str(file_path)
    }