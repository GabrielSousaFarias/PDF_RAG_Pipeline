from pathlib import Path

from app.config import settings

def initialize_app():

    required_dirs = [
        settings.upload_dir,
        settings.result_dir
    ]

    for directory in required_dirs:

        Path(directory).mkdir(
            parents=True,
            exist_ok=True
        )