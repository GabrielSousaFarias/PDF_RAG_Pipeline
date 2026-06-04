from app.config import settings

def test_kafka_configuration():
    assert settings.kafka_bootstrap_servers
    assert settings.pdf_topic