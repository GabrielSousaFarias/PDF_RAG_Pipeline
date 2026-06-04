from pathlib import Path


def test_upload_directory_exists():
    upload_dir = Path("data/uploads")

    assert upload_dir.exists()