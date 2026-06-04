import json
from pathlib import Path
import pymupdf

from app.config import settings

def parse_pdf(file_path: str) -> dict:
    doc = pymupdf.open(file_path)

    pages = []

    for page_number, page in enumerate(doc, start=1):
        text = page.get_text("text", sort=True)

        pages.append({
            "page": page_number,
            "text": text
        })

    return {
        "total_pages": len(doc),
        "pages": pages
    }


def save_result(file_id: str, result: dict) -> str:
    
    output_path = Path(settings.result_dir) / f"{file_id}.json"

    with open(output_path, "w", encoding="utf-8") as file:
        json.dump(result, file, ensure_ascii=False, indent=2)

    return str(output_path)