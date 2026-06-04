from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8"
    )

    kafka_bootstrap_servers: str
    pdf_topic: str
    log_level: str
    upload_dir: str = "data/uploads"
    result_dir: str = "data/results"
    
settings = Settings()