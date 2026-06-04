from fastapi import FastAPI, UploadFile, File, HTTPException

from app.storage import save_uploaded_pdf
from app.kafka_producer import publish_pdf_uploaded_event

from app.startup import initialize_app

initialize_app()
app = FastAPI(title="PDF Parser Pipeline")

@app.get("/")
def root():
    return {
        "message": "PDF Parser Pipeline API is running",
        "docs": "/docs",
        "health": "/health"
    }


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/upload")
def upload_pdf(file: UploadFile = File(...)):
    if file.content_type != "application/pdf":
        raise HTTPException(
            status_code=400,
            detail="Only PDF files are allowed"
        )

    saved_file = save_uploaded_pdf(file)

    event = {
        "file_id": saved_file["file_id"],
        "original_filename": saved_file["original_filename"],
        "file_path": saved_file["file_path"],
        "status": "uploaded"
    }

    publish_pdf_uploaded_event(event)

    return {
        "message": "PDF uploaded and sent to Kafka",
        "file_id": saved_file["file_id"],
        "status": "queued"
    }