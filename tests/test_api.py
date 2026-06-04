from io import BytesIO
from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_health():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_root():
    response = client.get("/")

    assert response.status_code == 200


def test_upload_invalid_file():
    response = client.post(
        "/upload",
        files={
            "file": (
                "arquivo.txt",
                BytesIO(b"not a pdf"),
                "text/plain"
            )
        }
    )

    assert response.status_code == 400